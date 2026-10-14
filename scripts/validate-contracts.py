"""Validate versioned ClientHub JSON Schema examples plus core reference invariants.

Usage from repository root:
    py -m pip install -r scripts/requirements-contracts.txt
    py scripts/validate-contracts.py

This validates schema structure and synthetic fixture consistency, NOT product correctness,
provider compatibility, permissions or LLM semantic truth.
"""
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / 'docs' / 'contracts' / 'schemas'
EXAMPLES = ROOT / 'docs' / 'contracts' / 'examples'


def main():
    sources = []
    for file in sorted(SCHEMAS.glob('*.schema.json')):
        schema = json.loads(file.read_text(encoding='utf-8'))
        Draft202012Validator.check_schema(schema)
        sources.append((schema['$id'], Resource.from_contents(schema)))
    registry = Registry().with_resources(sources)
    n = 0
    for file in sorted(EXAMPLES.glob('*.example.json')):
        schema_file = SCHEMAS / file.name.replace('.example.json', '.schema.json')
        if not schema_file.exists():
            raise ValueError(f'Missing schema for {file.name}')
        schema = json.loads(schema_file.read_text(encoding='utf-8'))
        document = json.loads(file.read_text(encoding='utf-8'))
        Draft202012Validator(schema, registry=registry, format_checker=FormatChecker()).validate(document)
        n += 1

    bundle = json.loads((EXAMPLES / 'context-bundle.example.json').read_text(encoding='utf-8'))
    registry_items = {item['ref_id']: item for item in bundle['evidence_registry']}
    assert len(registry_items) == len(bundle['evidence_registry']), 'Duplicated refs'
    for kind in ('sources', 'events', 'tickets'):
        for item in bundle[kind]:
            assert item['project_id'] == bundle['project_id'], f'Cross-project item in {kind}'
            assert item['ref_id'] in registry_items, f'Missing ref for {kind}'
    for event in bundle['events']:
        assert all(ref in registry_items for ref in event['source_refs'])
    for jira_link in bundle['jira_links']:
        assert registry_items[jira_link['ref_id']]['kind'] == 'JIRA_LINK'
    for key, maximum in (
        ('traversal_depth_reached', 'max_depth'),
        ('tickets_retrieved', 'max_tickets'),
        ('external_calls_used', 'max_external_calls'),
    ):
        assert bundle['usage'][key] <= bundle['policy'][maximum], f'Exceeded {maximum}'
    print(f'PASS: {len(sources)} schemas; {n} examples; bundle registry and budgets')


if __name__ == '__main__':
    main()
