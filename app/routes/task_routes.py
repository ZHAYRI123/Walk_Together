#Defines the routes related to task management.

from flask import render_template, request, redirect, url_for, flash
from . import task_bp
from ..models import Task
from ..extensions import db

@task_bp.route('/tasks', methods=['GET'])
def view_tasks():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

@task_bp.route('/task/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        # Handle adding a new task
        pass
    return render_template('add_task.html')