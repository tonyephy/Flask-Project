from flask import Flask, render_template, request, redirect, url_for, flash 
from flask_pymongo import PyMongo
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Set a secret key for session management
app.secret_key = '244b39dc516ae585bca489f1263d95a8'  # Use a secure key in production

# Initialize MongoDB
mongo = PyMongo(app)

# Initialize Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to login page if unauthorized access

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, user_id):
        self.id = str(user_id)

# User loader function
@login_manager.user_loader
def load_user(user_id):
    user_data = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if user_data:
        return User(user_data["_id"])
    return None

# Home route that displays tasks and requires login
@app.route('/')
@login_required
def home():
    pending_tasks = mongo.db.tasks.find({"user_id": current_user.id, "completed": False})  # Fetch only pending tasks
    completed_tasks = mongo.db.tasks.find({"user_id": current_user.id, "completed": True})  # Fetch only completed tasks
    return render_template('home.html', pending_tasks=pending_tasks, completed_tasks=completed_tasks)

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the username already exists
        if mongo.db.users.find_one({"username": username}):
            flash("Username already exists!", "danger")
            return redirect(url_for('register'))

        # Validate password length
        if len(password) < 6:
            flash("Password must be at least 6 characters long.", "danger")
            return redirect(url_for('register'))

        # Hash the password before storing it
        hashed_password = generate_password_hash(password)

        # Insert the new user into the users collection
        mongo.db.users.insert_one({"username": username, "password": hashed_password})
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user_data = mongo.db.users.find_one({"username": username})

        if user_data:
            stored_password = user_data['password']

            # Check if the password is valid
            if check_password_hash(stored_password, password):
                user = User(user_data["_id"])
                login_user(user)  # Log the user in
                flash("Login successful!", "success")
                return redirect(url_for('home'))  # Redirect to home after login
            else:
                flash("Invalid password!", "danger")
        else:
            flash("Invalid username!", "danger")

    return render_template('login.html')

# Route to add a task
@app.route('/add_task', methods=['POST'])
@login_required
def add_task():
    task_name = request.form.get('task_name')
    task_description = request.form.get('task_description')

    # Insert the new task into the tasks collection
    mongo.db.tasks.insert_one({
        "name": task_name,
        "description": task_description,
        "user_id": current_user.id,  # Link the task to the logged-in user
        "completed": False  # Initialize task as not completed
    })
    flash("Task added successfully!", "success")
    return redirect(url_for('home'))

# Route to mark a task as complete
@app.route('/mark_complete/<task_id>', methods=['POST'])
@login_required
def mark_complete(task_id):
    # Update the task to mark it as completed
    mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": {"completed": True}})
    flash("Task marked as complete!", "success")
    return redirect(url_for('home'))

# Logout route
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
