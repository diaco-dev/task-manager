# Task Manager with FastAPI, MongoDB, JWT, Celery

A simple and asynchronous Task Manager API built using **FastAPI**, **MongoDB**, **JWT** for authentication, and **Celery** for background tasks like push notifications.

## 🚀 Features

- **User authentication** using JWT
- **Task management**: Create, retrieve tasks
- **Push Notifications** (using Celery for background processing)
- **MongoDB** as the data store

## 🛠️ Technologies

- **FastAPI**: Web framework for building APIs
- **Poetry**: dependency management and packaging tool for Python
- **MongoDB**: NoSQL database
- **JWT**: Authentication
- **Celery**: Asynchronous task queue
- **Redis**: Celery broker (for background tasks)
- **Docker**: server 

## 📁 Project Structure

- `app/`: FastAPI application
- `celeryconfig.py`: Celery configuration
- `models.py`: MongoDB models
- `crud.py`: Database CRUD operations
- `tasks.py`: Task-related logic
- `dependencies.py`: JWT authentication logic

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/task-manager.git

### Poetry
   ```bash
      poetry init
      poetry add fastapi
      poetry install
