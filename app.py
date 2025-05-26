from flask import Flask, render_template, request, redirect, url_for, flash
# Import necessary Flask modules:
# - Flask: The main class to create the application.
# - render_template: Used to render HTML templates.
# - request: Handles incoming HTTP requests (e.g., form data).
# - redirect: Redirects the user to another route.
# - url_for: Dynamically generates URLs for routes.
# - flash: Displays temporary messages to the user.

app = Flask(__name__)  # Create an instance of the Flask application.
app.secret_key = 'your_secret_key'  # Set a secret key for securely using flash messages.

todos = []  #create an empty list to store tasks (to-do items).
@app.route('/') 
def index():
    flash('', 'clear')  # Clear any existing flash messages when the page is loaded.
    todos_with_ids = []
    for i, todo in enumerate(todos):
        task_with_id = {'id': i}
        task_with_id.update(todo)
        todos_with_ids.append(task_with_id)
@app.route('/add', methods=['POST']) 
def add():
    task = request.form.get('task')  # Retrieve the task content from the submitted form.
    if not task:  # Check if the task is empty.
        flash('Task cannot be empty!', 'error') 
    elif any(todo['task'] == task for todo in todos):  # Check if the task already exists in the list.
        flash('Task already exists!', 'error')  # Display an error message if the task is a duplicate.
    else:
        todos.append({'task': task, 'done': False})  # Add the new task to the list with 'done' set to False.
    return redirect(url_for('index'))  # Redirect the user back to the home page.

@app.route('/complete/<int:task_id>')  # Define the route for toggling the completion status of a task.
def complete(task_id):
    if 0 <= task_id < len(todos):  # Ensure the task_id is valid (within the bounds of the list).
        todos[task_id]['done'] = not todos[task_id]['done']  # Toggle the 'done' status of the task.
    return redirect(url_for('index'))  # Redirect the user back to the home page.

@app.route('/delete/<int:task_id>')  # Define the route for deleting a task.
def delete(task_id):
    if 0 <= task_id < len(todos):  # Ensure the task_id is valid (within the bounds of the list).
        todos.pop(task_id)  # Remove the task at the specified task_id from the list.
    return redirect(url_for('index'))  # Redirect the user back to the home page.

if __name__ == '__main__':  # Ensure the app runs only when the script is executed directly.
    app.run(debug=True)  # Start the Flask development server with debugging enabled.
