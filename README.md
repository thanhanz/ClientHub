# ClientHub

.NET 10 backend for the PO–Client Communication Hub. The API currently contains the starter weather forecast endpoint; see [product scope](docs/product/goal.md) for the planned MVP.

See the [milestone roadmap and review gates](harness/README.md) for the fake-data MVP plan, separate design/implementation checklists, and Runner-owned execution state. Start with the 001 design review; the executable Runner is not yet implemented.

## Prerequisites

Install the .NET 10 SDK. Docker commands require Docker with Linux containers and the Compose plugin. `global.json` allows stable .NET 10 SDK feature-band updates.

## Local development

```powershell
dotnet restore ClientHub.slnx
dotnet build ClientHub.slnx -c Release --no-restore
dotnet test ClientHub.slnx -c Release --no-build
dotnet run --project src/Hub.Api --launch-profile http
```

Open http://localhost:5198/weatherforecast or http://localhost:5198/openapi/v1.json. For HTTPS, run `dotnet dev-certs https --trust` and use `--launch-profile https` (port 7194).

## Docker

```powershell
docker compose up --build -d
docker compose logs -f api
```

Open http://localhost:8080/weatherforecast or http://localhost:8080/openapi/v1.json. Stop with `docker compose down`. Optionally copy `.env.example` to `.env` and change `API_PORT`. Compose runs in Development and binds only to localhost.

The multi-stage Dockerfile publishes a Release build and runs as the image's non-root app user. To run the image in Production:

```powershell
docker build -t clienthub-api:local .
docker run --rm -p 127.0.0.1:8080:8080 -e ASPNETCORE_ENVIRONMENT=Production clienthub-api:local
```

The container serves HTTP on port 8080. Production deployments should terminate HTTPS at an ingress or reverse proxy and configure forwarded headers before enabling HTTPS redirection. OpenAPI is exposed only in Development.

## Configuration and checks

Keep secrets out of tracked appsettings files. Use .NET user secrets locally (initialize with `dotnet user-secrets init --project src/Hub.Api`) or environment variables such as `ConnectionStrings__DefaultConnection`. Compose automatically reads `.env` for interpolation; it does not forward arbitrary entries to the API. Add required settings explicitly under the service's `environment` section.

Git ignores build output, IDE state, local environment files, and private key files. `.dockerignore` excludes those files from the build context. `.editorconfig` and `.gitattributes` define formatting and line endings. GitHub Actions restores, builds, tests, and builds the container on pushes and pull requests.
