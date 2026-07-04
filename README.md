# FocusFlow API 

A productivity tracking backend built with FastAPI, PostgreSQL, and JWT authentication.
It allows users to track tasks, log productivity sessions, and analyze study/work patterns through analytics endpoints.

---

## Features

### Authentication
- User registration
- Login system
- JWT-based authentication
- Protected routes

### Task Management
- Create / update / delete tasks
- Mark tasks as complete
- Assign categories
- Filter tasks by:
  - completion status
  - priority
  - category

### Categories
- CRUD for task grouping
- Examples: University, Work, Gym

### Productivity Sessions
- Track time spent on tasks
- Store session duration + date
- Linked to both user and task

### Analytics
- Total study/work hours
- Category breakdown
- Weekly productivity tracking
- Productivity streak calculation

---

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic (migrations)
- JWT (python-jose)
- Passlib (bcrypt hashing)

---

## Project Structure

```
app/
├── models/          # Database models
├── routers/         # API endpoints
├── services/        # Business logic
├── schemas/         # Pydantic DTOs
├── security/        # Auth + JWT
└── database/        # DB connection
```

---

## Authentication Flow

1. User registers
2. Password is hashed (bcrypt)
3. User logs in
4. JWT token is generated
5. Token is sent in headers:
   ```
   Authorization: Bearer <token>
   ```
6. Protected routes validate token

---

## Example API Endpoints

### Auth
```
POST /auth/register
POST /auth/login
```

### Tasks
```
GET    /tasks
POST   /tasks
PUT    /tasks/{id}
DELETE /tasks/{id}
```

### Categories
```
GET  /categories
POST /categories
```

### Sessions
```
POST /sessions
GET  /sessions
```

### Analytics
```
GET /analytics/study-hours
GET /analytics/categories
GET /analytics/weekly
GET /analytics/streak
```

---

## Running the Project

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup database
Create a PostgreSQL database and update `.env`:

```
DATABASE_URL=postgresql://user:password@localhost:5432/focusflow
```

### 3. Run migrations
```bash
alembic upgrade head
```

### 4. Start server
```bash
uvicorn app.main:app --reload
```