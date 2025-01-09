from flask import Blueprint, current_app
from src.controllers.taskController import get_all_tasks, get_task_by_id, create_task, update_task, delete_task

task_blueprint = Blueprint('tasks', __name__)

@task_blueprint.route('/', methods=['GET'])
def get_tasks():
    return get_all_tasks(current_app.mongo)

@task_blueprint.route('/<task_id>', methods=['GET'])
def get_task(task_id):
    return get_task_by_id(current_app.mongo, task_id)

@task_blueprint.route('/', methods=['POST'])
def create_new_task():
    return create_task(current_app.mongo)

@task_blueprint.route('/<task_id>', methods=['PUT'])
def update_existing_task(task_id):
    return update_task(current_app.mongo, task_id)

@task_blueprint.route('/<task_id>', methods=['DELETE'])
def delete_existing_task(task_id):
    return delete_task(current_app.mongo, task_id)