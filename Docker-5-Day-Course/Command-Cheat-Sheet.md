# Docker Command Cheat Sheet

Keep this open in class. Commands assume **Docker Desktop** or Docker Engine.

---

## Day 1 — Run containers

| Command | What it does |
| ------- | ------------ |
| `docker version` | Client and engine version |
| `docker info` | Engine status |
| `docker pull nginx` | Download image |
| `docker images` | List local images |
| `docker run -d -p 8080:80 --name mynginx nginx` | Run in background, map port, name it |
| `docker ps` | Running containers |
| `docker ps -a` | All containers (including stopped) |
| `docker stop mynginx` | Stop |
| `docker start mynginx` | Start a stopped container |
| `docker rm mynginx` | Remove a stopped container |
| `docker rmi nginx` | Remove an image |

---

## Day 2 — Build images

| Command | What it does |
| ------- | ------------ |
| `docker build -t hello:1.0 .` | Build from Dockerfile in this folder |
| `docker history hello:1.0` | Show layers |
| `docker inspect hello:1.0` | JSON details |

**Dockerfile words:** `FROM`, `WORKDIR`, `COPY`, `RUN`, `EXPOSE`, `CMD` / `ENTRYPOINT`.

---

## Day 3 — Inspect, data, network

| Command | What it does |
| ------- | ------------ |
| `docker logs mynginx` | Container stdout/stderr |
| `docker logs -f mynginx` | Follow logs |
| `docker exec -it mynginx bash` | Shell inside container (`sh` on Alpine) |
| `docker inspect mynginx` | Config, IP, mounts |
| `docker run -v pgdata:/var/lib/postgresql/data ...` | Named volume |
| `docker volume ls` | List volumes |
| `docker network ls` | List networks |
| `docker network create appnet` | Create user network |
| `docker run --network appnet --name api ...` | Attach to network |

Port flag: `-p HOST:CONTAINER` → `-p 8080:80`.

---

## Day 4 — Compose and registry

| Command | What it does |
| ------- | ------------ |
| `docker compose up -d` | Start stack in background |
| `docker compose ps` | Status |
| `docker compose logs -f` | All service logs |
| `docker compose down` | Stop and remove containers |
| `docker compose down -v` | Also remove volumes |
| `docker tag hello:1.0 USER/hello:1.0` | Name for Hub |
| `docker login` | Sign in to Hub |
| `docker push USER/hello:1.0` | Upload |
| `docker pull USER/hello:1.0` | Download |

---

## Day 5 — Ops

| Command | What it does |
| ------- | ------------ |
| `docker stats` | Live CPU/memory |
| `docker system df` | Disk used by Docker |
| `docker system prune` | Remove unused data (ask first) |
| `docker compose restart web` | Restart one service |

---

## Safety rules

- `docker rm` / `prune` delete **your** containers and unused images — check names first.
- Do not put secrets (passwords, Hub tokens) in a Dockerfile.
- Map only the ports you need.
- Prefer named volumes for databases.
