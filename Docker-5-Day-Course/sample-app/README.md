# Sample app — Campus Hello

Tiny static site served by **nginx**. Used on Days 2–5.

```bash
cd Docker-5-Day-Course/sample-app
docker build -t campus-hello:1.0 .
docker run -d -p 8080:80 --name hello campus-hello:1.0
```

Open http://localhost:8080

Stop:

```bash
docker stop hello && docker rm hello
```

Or with Compose:

```bash
docker compose up -d --build
docker compose down
```
