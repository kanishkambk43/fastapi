# FastAPI Learning Repository

A collection of my FastAPI learning notes, code examples, backend concepts, and practical implementations using Python.

## 📌 About

This repository documents my journey of learning **FastAPI and backend development**. It covers fundamental concepts, REST API development, database integration, asynchronous programming, testing, and containerization.

The goal is to understand how modern backend applications are designed, developed, tested, and deployed.

## 🛠️ Technologies Covered

- **Python** — Backend programming
- **FastAPI** — Building REST APIs
- **Pydantic** — Request validation and data serialization
- **SQLAlchemy** — Database ORM and asynchronous database operations
- **PostgreSQL** — Relational database management
- **Redis** — Caching and fast data access
- **Uvicorn** — ASGI server
- **Docker & Docker Compose** — Containerization and service management
- **Pytest** — Automated testing
- **Swagger UI / OpenAPI** — API documentation and testing
- **Git & GitHub** — Version control

## 📚 Topics Covered

### 1. FastAPI Fundamentals
- Introduction to FastAPI
- Creating API endpoints
- Path and query parameters
- Request bodies
- HTTP methods and status codes
- Response models
- Pydantic validation
- Error handling using `HTTPException`

### 2. Backend Concepts
- REST API principles
- CRUD operations
- Dependency injection
- Middleware
- CORS
- Asynchronous programming with `async` and `await`
- Environment variables and configuration

### 3. Database Integration
- PostgreSQL integration
- SQLAlchemy ORM
- Database models
- Database sessions
- Asynchronous database operations
- Creating, reading, updating, and deleting records

### 4. Performance and Security
- Redis caching
- API rate limiting
- Input validation
- Environment variable management
- Health check endpoints

### 5. Testing and Deployment
- Automated API testing using Pytest
- Interactive API documentation
- Dockerfile creation
- Docker Compose
- Running multiple services together

## 🚀 Practical Project: URL Shortener

A URL Shortener built using FastAPI, PostgreSQL, and Redis.

### Features
- Convert long URLs into short URLs
- Generate short codes using Base62 encoding
- Support custom aliases
- Redirect users to the original URL
- Set URL expiration
- Track link clicks and statistics
- Cache frequently accessed URLs using Redis
- Apply API rate limiting
- Provide a health check endpoint
- Interactive API documentation through Swagger UI
- Simple frontend using HTML, CSS, and JavaScript

### Architecture

```text
          Client / Frontend
                  |
                  v
             FastAPI API
                  |
           +------+------+
           |             |
           v             v
        Redis         PostgreSQL
        Cache         Persistent
                       Storage
```

**PostgreSQL** stores URL records and click statistics, while **Redis** caches frequently accessed short URLs to improve redirect performance.

## ⚙️ Getting Started

### Prerequisites
- Python
- pip
- PostgreSQL
- Redis
- Docker Desktop (optional, for containerized execution)

### Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd <your-repository-name>
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure the required environment variables in a `.env` file according to your application's configuration.

Start the FastAPI application:

```bash
uvicorn app.main:app --reload
```

Open the interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

**Note:** Database and Redis services must be configured and running. If the project uses Docker Compose, use the repository's Compose configuration to start the required services.

## 🧪 Testing

Run automated tests using:

```bash
pytest
```

## 🎯 Learning Objectives

- Build REST APIs using FastAPI.
- Understand backend architecture and request processing.
- Integrate relational databases and caching systems.
- Work with asynchronous Python.
- Implement validation, error handling, and rate limiting.
- Test APIs and run applications using Docker.

## 📈 Progress

This repository serves as a practical reference for my ongoing backend development journey, with an emphasis on understanding concepts through implementation.


