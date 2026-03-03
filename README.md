# Task Manager - Distributed Systems & Cloud Computing

**Repository:** [https://github.com/kamillamee/00015829_DSCC](https://github.com/kamillamee/00015829_DSCC)

A Django web application for managing projects and tasks. Users can create projects, add tasks with tags, and track progress. The app is containerized with Docker and deployed via GitHub Actions CI/CD pipeline.

**Student ID:** 00015829

## Features

- **User Authentication**: Login, logout, registration
- **Projects & Tasks**: Create, read, update, delete projects and tasks
- **Database Models**: Project (many-to-one User), Task (many-to-one Project, many-to-many Tag), Tag
- **Admin Panel**: Full Django admin configuration
- **5+ Functional Pages**: Home, Login, Register, Project List, Project Detail, Task CRUD

## Technologies Used

- **Backend**: Django 4.2, Python 3.11
- **Database**: PostgreSQL 15
- **Web Server**: Nginx, Gunicorn
- **Containerization**: Docker, Docker Compose
- **CI/CD**: GitHub Actions

## Local Setup

### Prerequisites

- Python 3.11+
- Docker & Docker Compose
- PostgreSQL (or use Docker)

### Development without Docker

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

pip install -r requirements.txt
copy .env.example .env   # Windows
# Edit .env - set USE_SQLITE=True for local dev without PostgreSQL

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Development with Docker

```bash
copy .env.example .env   # Windows
# Set DOCKERHUB_USERNAME=00015829 in .env

docker compose up --build
# Access at http://localhost
```

### Run Tests

```bash
pytest tasks/ -v
```

## Deployment

### Server Setup (Azure / Eskiz / Ubuntu)

1. Create VM (Azure: Ubuntu 22.04, open ports 22, 80, 443)
2. Install Docker: `curl -fsSL https://get.docker.com | sh`
3. Clone repository: `git clone https://github.com/kamillamee/00015829_DSCC.git /opt/cloudcomputing`
3. Configure `.env` with production values
4. Configure UFW: `ufw allow 22,80,443`
5. For HTTPS: Use Let's Encrypt (certbot) and place certs in `nginx/ssl/`

### GitHub Actions Deployment

1. Create a repository on Docker Hub named `cloudcomputing` (or your preferred name)
2. In GitHub: **Settings → Secrets and variables → Actions**, add:

| Secret | Value | Description |
|--------|-------|-------------|
| DOCKERHUB_USERNAME | `00015829` | Your Docker Hub username |
| DOCKERHUB_TOKEN | Access Token from Docker Hub | Account Settings → Security → New Access Token |
| SSH_HOST | Server IP | (Add when you have a server) |
| SSH_USERNAME | `root` | (Add when you have a server) |
| SSH_PRIVATE_KEY | Your private SSH key | (Add when you have a server) |
| DEPLOY_PATH | `/opt/cloudcomputing` | Optional, default path on server |

Pipeline triggers on push to `main` branch. Build and push work without server; deploy needs SSH secrets.

### Manual Deployment

```bash
# On server
cd /opt/cloudcomputing
git pull
docker compose pull
docker compose up -d
docker compose exec web python manage.py migrate --noinput
docker compose exec web python manage.py collectstatic --noinput
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| SECRET_KEY | Django secret key | (required) |
| DEBUG | Debug mode | False |
| ALLOWED_HOSTS | Comma-separated hosts | localhost |
| POSTGRES_DB | Database name | cloudcomputing_db |
| POSTGRES_USER | DB user | postgres |
| POSTGRES_PASSWORD | DB password | (required) |
| POSTGRES_HOST | DB host | db (Docker) |
| DOCKERHUB_USERNAME | For image tagging / pull | 00015829 |
| USE_SQLITE | Use SQLite instead of PostgreSQL (local dev) | False |

## Project Structure

```
├── config/          # Django settings
├── tasks/           # Main application
├── nginx/           # Nginx configuration
├── .github/         # GitHub Actions workflows
├── Dockerfile       # Multi-stage build
├── docker-compose.yml
└── requirements.txt
```

## Screenshots

*(Add screenshots of your running application here)*

## License

Educational project - WIUT DSCC Coursework.

---
