# 🚀 Task Management API with FastAPI

This project is a **Task Management API** built with **FastAPI** and **PostgreSQL**. It features **authentication**, **role-based access control**, and **CRUD operations** for managing users and tasks. Additionally, the API sends email notifications for task-related events.

### ✨ Features

- User registration and login with JWT authentication.
- Role-based access control (`admin` and `user` roles).
- CRUD operations for managing tasks.
- Email notifications for task creation, updates, and deletion.
- PostgreSQL integration for database storage.

## 🛠️ Tech Stack

- **FastAPI**: Python web framework for building APIs.
- **SQLAlchemy**: ORM for interacting with the PostgreSQL database.
- **PostgreSQL**: Relational database system.
- **JWT**: Token-based authentication.
- **Pydantic**: Data validation using Python type hints.
- **SMTP**: Email notifications.

## 📂 Project Structure

. ├── main.py ├── models.py ├── schemas.py ├── crud.py ├── auth.py ├── email_utils.py ├── database.py ├── .env ├── .gitignore ├── README.md └── requirements.txt

## ⚙️ Setup

### Prerequisites

Ensure you have the following installed:

- Python 3.10 or later
- PostgreSQL
- Git

### Step 1: Clone the repository

````bash
git clone https://github.com/yourusername/fastapi-task-manager.git
cd fastapi-task-manager

Step 2: Set up a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

Step 3: Install dependencies
pip install -r requirements.txt

Step 4: Configure environment variables
Create a .env file in the root directory and add your sensitive variables:
DATABASE_URL=postgresql://username:password@localhost:5432/task_db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Email settings
SMTP_SERVER=smtp.your-email-provider.com
SMTP_PORT=587
SMTP_USERNAME=your-email@example.com
SMTP_PASSWORD=your-email-password
EMAIL_FROM=your-email@example.com
EMAIL_FROM_NAME=Task Manager

Step 5: Set up the database
Ensure PostgreSQL is running and create a database:

Certainly! Below is the README.md file written in Markdown format, ready for you to copy and paste:

markdown
Copy code
# 🚀 Task Management API with FastAPI

This project is a **Task Management API** built with **FastAPI** and **PostgreSQL**. It features **authentication**, **role-based access control**, and **CRUD operations** for managing users and tasks. Additionally, the API sends email notifications for task-related events.

### ✨ Features

- User registration and login with JWT authentication.
- Role-based access control (`admin` and `user` roles).
- CRUD operations for managing tasks.
- Email notifications for task creation, updates, and deletion.
- PostgreSQL integration for database storage.

## 🛠️ Tech Stack

- **FastAPI**: Python web framework for building APIs.
- **SQLAlchemy**: ORM for interacting with the PostgreSQL database.
- **PostgreSQL**: Relational database system.
- **JWT**: Token-based authentication.
- **Pydantic**: Data validation using Python type hints.
- **SMTP**: Email notifications.

## 📂 Project Structure

. ├── main.py ├── models.py ├── schemas.py ├── crud.py ├── auth.py ├── email_utils.py ├── database.py ├── .env ├── .gitignore ├── README.md └── requirements.txt

bash
Copy code

## ⚙️ Setup

### Prerequisites

Ensure you have the following installed:

- Python 3.10 or later
- PostgreSQL
- Git

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/fastapi-task-manager.git
cd fastapi-task-manager
Step 2: Set up a virtual environment
bash
Copy code
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Step 3: Install dependencies
bash
Copy code
pip install -r requirements.txt
Step 4: Configure environment variables
Create a .env file in the root directory and add your sensitive variables:

env
Copy code
DATABASE_URL=postgresql://username:password@localhost:5432/task_db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Email settings
SMTP_SERVER=smtp.your-email-provider.com
SMTP_PORT=587
SMTP_USERNAME=your-email@example.com
SMTP_PASSWORD=your-email-password
EMAIL_FROM=your-email@example.com
EMAIL_FROM_NAME=Task Manager
Step 5: Set up the database
Ensure PostgreSQL is running and create a database:

sql
CREATE DATABASE task_db;

Step 6: Run database migrations
If you are using Alembic or any migration tool, initialize and run migrations. Otherwise, you can manually create the tables.

Step 7: Start the server
uvicorn main:app --reload
The API will be available at: http://127.0.0.1:8000

🔥 API Endpoints
Authentication
Method	Endpoint	Description
POST	/register	Register a new user
POST	/login	Login and get JWT token
User Management (Admin only)
Method	Endpoint	Description
GET	/users	List all users
DELETE	/users/{id}	Delete a user
Task Management
Method	Endpoint	Description
POST	/tasks	Create a new task
GET	/tasks	Get tasks for the logged-in user
GET	/tasks/admin	Get all tasks (Admin only)
PUT	/tasks/{id}	Update a task
DELETE	/tasks/{id}	Delete a task (Admin only)


🛡️ Role-Based Access Control
Admin: Can view all users, create tasks for any user, and delete any user or task.
User: Can only view their own tasks and update the status of tasks assigned to them.
📧 Email Notifications
Email notifications are sent for the following events:

Task creation
Task update
Task deletion
Make sure your SMTP email configuration in the .env file is correct.

🧪 Testing the API
You can use tools like Postman or cURL to test the endpoints.

Example cURL Request
bash
Copy code
# Register a new user
curl -X 'POST' \
  'http://127.0.0.1:8000/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "email": "user@example.com",
    "full_name": "John Doe",
    "password": "password123",
    "role": "user"
  }'

# Login to get JWT token
curl -X 'POST' \
  'http://127.0.0.1:8000/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "username": "user@example.com",
    "password": "password123"
  }'


🐛 Known Issues
Ensure your PostgreSQL service is running before starting the server.
Email notifications may not work if the SMTP configuration is incorrect.
📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
````
