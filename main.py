from flask import Flask, render_template, request, redirect
from datetime import datetime
import json
import os

app = Flask(__name__)

TASKS_FILE = 'tasks.json'


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []


def save_tasks():
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


tasks = load_tasks()


@app.route('/')
def index():
    filter_status = request.args.get('filter')
    filtered_tasks = tasks

    if filter_status:
        filtered_tasks = [task for task in tasks if task['status'] == filter_status]

    return render_template('index.html', tasks=filtered_tasks, filter_status=filter_status)


@app.route('/add', methods=['POST'])
def add():
    task_name = request.form.get('task')
    due_date = request.form.get('due_date')
    status = request.form.get('status', 'In Progress')
    date_added = datetime.now().strftime('%A, %B %d')

    task = {
        'name': task_name,
        'due_date': due_date,
        'status': status,
        'date_added': date_added
    }
    tasks.append(task)
    save_tasks()
    return redirect('/')


@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
        save_tasks()
    return redirect('/')


@app.route('/update_status/<int:task_id>', methods=['POST'])
def update_status(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['status'] = request.form.get('status')
        save_tasks()
    return redirect('/')


@app.route('/update_due_date/<int:task_id>', methods=['POST'])
def update_due_date(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['due_date'] = request.form.get('due_date')
        save_tasks()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
