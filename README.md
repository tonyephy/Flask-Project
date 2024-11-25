# Flask-Project


# Task Flow App

This is a basic Flask-based task flow application, enabling users to add, update, delete, mark tasks as completed, and view tasks. It uses MongoDB for data storage, allowing users to organize their tasks and manage their productivity effectively.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Future Enhancements](#future-enhancements)

## Features
- **User Authentication**: Registration and login options for users, enabling secure task management.
- **Task Management**: Create, view, edit, delete, and mark tasks as completed.
- **Responsive UI**: Simple, responsive user interface to view and manage tasks easily.

## Technologies Used
- **Backend**: Flask (Python)
- **Database**: MongoDB
- **Frontend**: HTML/CSS with responsive design
- **Other Libraries**: bcrypt (for password hashing), Flask’s Jinja2 for templating, body-parser for JSON parsing.

## Setup
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   ```
2. **Navigate into the project directory**:
   ```bash
   cd task-manager-app
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```
4. **Activate the virtual environment**:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
6. **Start the MongoDB server**:
   - Make sure MongoDB is running on `localhost:27017`.
   
7. **Run the app**:
   ```bash
   python app.py
   ```

## Usage
1. **Sign Up**: Register a new account with a unique username and password.
2. **Log In**: Access your account to manage tasks.
3. **Task Operations**: Add, edit, view, delete, and mark tasks as completed from the dashboard.

## API Endpoints
- **`/signup`**: Registers a new user.
- **`/login`**: Authenticates a user.
- **`/tasks`**: Adds, updates, deletes, and marks tasks as completed.
- **`/tasks/<task_id>`**: Performs actions on a specific task.

## Future Enhancements
- **Task Filtering**: Allow users to filter tasks by priority or due date.
- **Task Reminders**: Add reminders for upcoming tasks.
- **User Profiles**: Add profile settings to personalize the app experience.

---

This app provides a basic foundation for a task management system with secure user access, CRUD operations, and the ability to mark tasks as completed, helping users stay organized and on track with their goals.ecure user access and CRUD operations for task management.
