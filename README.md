# Synapse

Synapse — an app for finding study partners. 🎓

### Technology stack

- Python
- Fastapi
- SqlAlchemy
- Vue
- TypeScript

### Run backend


1. Go to `.docker/`:

```bash
cd .docker
```
2. Create file .docker/.env using template .docker/.env.example

3. From backend root run
```bash 
docker compose -f .docker/docker-compose.yml up --build -d

docker compose -f .docker/docker-compose.yml exec backend alembic upgrade head
```
---
Swagger located at: ```/docs```, ReDoc at ```/redoc```.

### Run frontend


```cd frontend/synapse```

```npm i```

```npm run dev ```
