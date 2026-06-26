# Contoso Tasks — Java Sample

A minimal Spring Boot (Maven, JDK 17) API used by the Azure DevOps 6-Day Course.

## Requirements

- JDK 17+.
- Maven 3.6+ (or use the bundled wrapper if you add one).

## Run Locally

```bash
mvn spring-boot:run
# Listens on http://localhost:8080
```

Try the endpoints:

```bash
curl http://localhost:8080/
curl http://localhost:8080/health
curl http://localhost:8080/tasks
curl -X POST http://localhost:8080/tasks -H "Content-Type: application/json" -d '{"title":"My task"}'
```

## Build & Test

```bash
mvn package          # compiles, runs tests, and builds the JAR in target/
mvn test             # just run the tests
```

The built JAR is `target/contoso-tasks-1.0.0.jar`; run it with `java -jar target/contoso-tasks-1.0.0.jar`.

## Project Structure

```
Java/
├── pom.xml
├── src/main/java/com/contoso/tasks/
│   ├── ContosoTasksApplication.java   # Spring Boot entry point
│   └── TaskController.java            # REST endpoints
├── src/main/resources/application.properties
├── src/test/java/com/contoso/tasks/
│   └── TaskControllerTest.java        # MockMvc tests
├── .gitignore
└── azure-pipelines.yml                # Maven build + JUnit results + artifact
```

## CI Pipeline

`azure-pipelines.yml` runs `mvn package`, publishes JUnit results, and uploads the JAR as an artifact. See [Day 3](../../Day-03-Azure-Pipelines/) and the [Day 6 project](../../Day-06-Real-Time-Project/).

## Endpoints

| Method | Path | Description |
| ------ | ---- | ----------- |
| GET | `/` | Welcome message |
| GET | `/health` | `{ "status": "ok" }` |
| GET | `/tasks` | List tasks |
| POST | `/tasks` | Add a task (`{ "title": "..." }`) |
