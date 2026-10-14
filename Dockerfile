FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
WORKDIR /source
COPY global.json ./
COPY src/Hub.Api/Hub.Api.csproj src/Hub.Api/
RUN dotnet restore src/Hub.Api/Hub.Api.csproj
COPY src/Hub.Api/ src/Hub.Api/
RUN dotnet publish src/Hub.Api/Hub.Api.csproj -c Release --no-restore -o /app/publish /p:UseAppHost=false

FROM mcr.microsoft.com/dotnet/aspnet:10.0 AS final
WORKDIR /app
ENV ASPNETCORE_HTTP_PORTS=8080
EXPOSE 8080
COPY --from=build /app/publish ./
USER $APP_UID
ENTRYPOINT ["dotnet", "Hub.Api.dll"]
