"""Validate draft schemas, examples and evidence invariants, including negative cases.

Run: python scripts/validate-contracts.py
Dependencies: scripts/requirements-contracts.txt
This is not runtime authorization, provider integration or AI semantic verification.
"""
import json
from copy import deepcopy
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker, ValidationError
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / 'docs' / 'contracts' / 'schemas'
EXAMPLES = ROOT / 'docs' / 'contracts' / 'examples'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_bundle(bundle):
    registry = {item['ref_id']: item for item in bundle['evidence_registry']}
    require(len(registry) == len(bundle['evidence_registry']), 'Duplicated registry refs')
    require(all(item['project_id'] == bundle['project_id'] for item in registry.values()),
            'Cross-project registry item')
    seen = set()

    def register(item, kind, expected_ref):
        ref = item['ref_id']
        require(ref == expected_ref, 'Noncanonical evidence identity')
        require(ref not in seen, 'Duplicate evidence item')
        seen.add(ref)
        require(ref in registry and registry[ref]['kind'] == kind, 'Missing/wrong registry kind')
        if 'observed_at' in item:
            require(registry[ref].get('observed_at') == item['observed_at'],
                    'Registry observation mismatch')

    sources = {s['ref_id'] for s in bundle['sources']}
    events = {e['ref_id'] for e in bundle['events']}
    tickets = {t['ref_id'] for t in bundle['tickets']}
    for item in bundle['sources']:
        require(item['project_id'] == bundle['project_id'], 'Cross-project source')
        register(item, 'SOURCE', 'source:' + item['source_id'])
    for item in bundle['events']:
        require(item['project_id'] == bundle['project_id'], 'Cross-project event')
        require(item['review_status'] == 'APPROVED', 'Unapproved synthesis event')
        require(item['source_refs'] and all(ref in sources for ref in item['source_refs']),
                'Event provenance does not resolve to included sources')
        register(item, 'EVENT', 'event:' + item['event_id'])
        require(registry[item['ref_id']].get('review_status') == 'APPROVED',
                'Registry event review mismatch')
    for item in bundle['tickets']:
        require(item['project_id'] == bundle['project_id'], 'Cross-project ticket')
        locator = item['jira_instance_key'] + ':' + item['issue_key']
        register(item, 'JIRA_ISSUE', 'jira:' + locator)
        excerpts = [('DESCRIPTION', e) for e in [item.get('description_excerpt')] if e]
        excerpts += [('HISTORY', e) for e in item.get('history', [])]
        excerpts += [('COMMENT', e) for e in item.get('comments', [])]
        for kind, excerpt in excerpts:
            prefix = 'jira-excerpt:' + locator + ':' + kind + ':'
            require(excerpt['ref_id'].startswith(prefix) and
                    len(excerpt['ref_id']) > len(prefix), 'Excerpt identity mismatch')
            register(excerpt, 'JIRA_EXCERPT', excerpt['ref_id'])
    mapping_keys = set()
    mapping_ids = set()
    for item in bundle['event_ticket_links']:
        require(item['event_ref'] in events and item['jira_ref'] in tickets,
                'Mapping endpoint missing or wrong type')
        require(item['verification_status'] == 'CONFIRMED', 'Unconfirmed synthesis mapping')
        key = (item['event_ref'], item['jira_ref'], item['relationship_type'])
        require(key not in mapping_keys and item['mapping_id'] not in mapping_ids,
                'Duplicate mapping')
        mapping_keys.add(key)
        mapping_ids.add(item['mapping_id'])
    for item in bundle['jira_links']:
        instance = item['jira_instance_key']
        require(all('jira:' + instance + ':' + item[k] in tickets
                    for k in ('from_issue_key', 'to_issue_key')), 'Missing Jira link endpoint')
        ref = ':'.join(['jira-link', instance, item['from_issue_key'],
                        item['relation_type'], item['to_issue_key']])
        register(item, 'JIRA_LINK', ref)
    require(seen == set(registry), 'Orphan registry evidence')
    require(bundle['usage']['tickets_retrieved'] == len(tickets), 'Incorrect ticket count')
    for actual, maximum in [('traversal_depth_reached', 'max_depth'),
                            ('tickets_retrieved', 'max_tickets'),
                            ('external_calls_used', 'max_external_calls')]:
        require(bundle['usage'][actual] <= bundle['policy'][maximum], 'Exceeded ' + maximum)


def validate_result(result, bundle):
    require(result['request_id'] == bundle['request_id'], 'Wrong result request ID')
    refs = {item['ref_id'] for item in bundle['evidence_registry']}
    ids = set()
    for claim in result['claims']:
        require(claim['claim_id'] not in ids, 'Duplicate claim ID')
        ids.add(claim['claim_id'])
        require(all(ref in refs for ref in claim['evidence_refs']), 'Unknown claim reference')
        require(claim['claim_type'] != 'FACT' or claim['evidence_refs'], 'Unreferenced FACT')


def main():
    schemas = {p.name: json.loads(p.read_text(encoding='utf-8'))
               for p in sorted(SCHEMAS.glob('*.schema.json'))}
    for schema in schemas.values():
        Draft202012Validator.check_schema(schema)
    registry = Registry().with_resources(
        (s['$id'], Resource.from_contents(s)) for s in schemas.values())

    def validate(name, document):
        Draft202012Validator(schemas[name + '.schema.json'], registry=registry,
                             format_checker=FormatChecker()).validate(document)

    examples = {}
    for file in sorted(EXAMPLES.glob('*.example.json')):
        name = file.name.removesuffix('.example.json')
        examples[name] = json.loads(file.read_text(encoding='utf-8'))
        validate(name, examples[name])
    bundle = examples['context-bundle']
    validate_bundle(bundle)
    validate_result(examples['investigation-result'], bundle)

    def check_bundle(document):
        validate('context-bundle', document)
        validate_bundle(document)

    # In-memory mutations: never rewrite the canonical positive examples.
    cases = [
        ('duplicate registry', lambda b: b['evidence_registry'].append(deepcopy(b['evidence_registry'][0]))),
        ('cross-project registry', lambda b: b['evidence_registry'][0].update(project_id='99999999-9999-4999-8999-999999999999')),
        ('source-less event', lambda b: b['events'][0].update(source_refs=[])),
        ('wrong provenance type', lambda b: b['events'][0].update(source_refs=[b['tickets'][0]['ref_id']])),
        ('pending event', lambda b: b['events'][0].update(review_status='PENDING_REVIEW')),
        ('rejected event', lambda b: b['events'][0].update(review_status='REJECTED')),
        ('duplicate mapping', lambda b: b['event_ticket_links'].append(deepcopy(b['event_ticket_links'][0]))),
        ('wrong mapping endpoint', lambda b: b['event_ticket_links'][0].update(jira_ref=b['sources'][0]['ref_id'])),
        ('proposed association', lambda b: b['event_ticket_links'][0].update(verification_status='PROPOSED')),
        ('missing Jira endpoint', lambda b: b['jira_links'][0].update(to_issue_key='MISSING-1')),
        ('false ticket count', lambda b: b['usage'].update(tickets_retrieved=0)),
        ('budget exceeded', lambda b: b['usage'].update(external_calls_used=999)),
        ('excerpt observation mismatch', lambda b: b['tickets'][0]['comments'][0].update(observed_at='2026-01-01T00:00:00Z')),
        ('too many comments', lambda b: b['tickets'][0].update(comments=b['tickets'][0]['comments'] * 11)),
    ]
    negative_count = 0

    def rejects(label, check, document):
        nonlocal negative_count
        try:
            check(document)
        except (ValueError, ValidationError):
            negative_count += 1
            return
        raise ValueError('Invalid case accepted: ' + label)

    for label, mutate in cases:
        candidate = deepcopy(bundle)
        mutate(candidate)
        rejects(label, check_bundle, candidate)
    for label, mutate in [
        ('unknown claim ref', lambda r: r['claims'][0].update(evidence_refs=['event:missing'])),
        ('unreferenced fact', lambda r: r['claims'][0].update(evidence_refs=[])),
        ('wrong request', lambda r: r.update(request_id='99999999-9999-4999-8999-999999999999')),
    ]:
        candidate = deepcopy(examples['investigation-result'])
        mutate(candidate)
        rejects(label, lambda r: validate_result(r, bundle), candidate)
    source = deepcopy(examples['source'])
    del source['external_source_id']
    rejects('ID-less intake', lambda s: validate('source', s), source)
    extraction = deepcopy(examples['extraction-output'])
    del extraction['events'][0]['occurred_at_precision']
    rejects('missing time precision', lambda e: validate('extraction-output', e), extraction)
    print(f'PASS: {len(schemas)} schemas; {len(examples)} examples; '
          f'bundle/result invariants; {negative_count} negative cases')


if __name__ == '__main__':
    main()
