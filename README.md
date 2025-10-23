# FastAPI Web Application with PostgreSQL and Website Monitoring

This project demonstrates a containerized FastAPI web application integrated with PostgreSQL database and automated website availability monitoring system. The implementation showcases modern DevOps practices including containerization, environment variable configuration, and automated health checking.

## Project Overview

The application consists of three main components:
- FastAPI Web Service: A Python-based REST API with database connectivity
- PostgreSQL Database: Containerized relational database for data persistence
- Website Monitoring Script: Bash-based automated health checking system for external websites

## Tech Stack

- Backend: FastAPI (Python web framework)
- Database: PostgreSQL 16
- ORM: SQLAlchemy
- Containerization: Docker & Docker Compose
- Web Server: Uvicorn (ASGI server)
- Monitoring: Bash scripting with curl
- Configuration: Environment variables

## Architecture

The project utilizes Docker Compose for orchestration, providing a complete development and deployment environment. The FastAPI application connects to PostgreSQL through environment variables, ensuring configuration flexibility and security.

## Prerequisites

- Docker and Docker Compose installed on your system
- Git for repository cloning

## Installation and Deployment

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-name>
```

2. Start the application stack:
```bash
docker-compose up --build
```

3. Access the services:
   - **FastAPI Application**: http://localhost:8000
   - **PostgreSQL Database**: localhost:5432

4. Stop the services:
```bash
docker-compose down
```

## Website Monitoring System

The project includes an automated website availability monitoring script that performs HTTP health checks on a predefined list of websites and logs the results.

### Usage

```bash
chmod +x scripts/website_availability_healthcheck.sh
./scripts/website_availability_healthcheck.sh
```

### Functionality

- Performs HTTP status code validation for each target website
- Logs results to `website_status.log` file
- Provides completion status notification

### Sample Output

```
<https://google.com> is UP
<https://facebook.com> is UP
<https://example.org> is DOWN
```

## Configuration

The application uses environment variables for database connectivity:

- `DATABASE_USER`: PostgreSQL username (default: postgres)
- `DATABASE_PASSWORD`: PostgreSQL password (default: 567234)
- `DATABASE_HOST`: Database hostname (default: postgres_db)
- `DATABASE_NAME`: Database name (default: hw02)

## Project Structure

```
simple_fastapi-setup/
├── docker-compose.yaml          # Container orchestration
├── fast-api/                    # FastAPI application
│   ├── Dockerfile              # Application container
│   ├── main.py                 # Application entry point
│   ├── conf/db.py              # Database configuration
│   └── requirements.txt        # Python dependencies
└── scripts/                     # Monitoring utilities
    └── website_availability_healthcheck.sh
```
