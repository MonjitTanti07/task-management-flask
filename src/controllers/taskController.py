from flask import jsonify, request
from bson import ObjectId

def get_all_tasks(mongo):
    query = (request.args.to_dict())
    custom_query = {}
    if query and query.get("status") != None:
        custom_query["status"] = (query.get("status") == "true") if True else False
    tasks = mongo.db.tasks.find(custom_query)
    task_list = [{"id": str(task["_id"]), "name": task["name"], "status": task["status"]} for task in tasks]
    return jsonify(task_list), 200

def get_task_by_id(mongo, task_id):
    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    if task:
        return jsonify({"id": str(task["_id"]), "name": task["name"], "status": task["status"]}), 200
    return jsonify({"error": "Task not found"}), 404

def create_task(mongo):
    data = request.json
    print('Data',data)
    if not data.get("name") or data.get("status") == None:
        return jsonify({"error": "Name and status are required"}), 400
    
    task_id = mongo.db.tasks.insert_one({"name": data["name"], "status": data["status"]}).inserted_id
    return jsonify({"message": "Task created", "id": str(task_id)}), 201

def update_task(mongo, task_id):
    data = request.json
    updated_task = mongo.db.tasks.find_one_and_update(
        {"_id": ObjectId(task_id)},
        {"$set": {"name": data.get("name"), "status": data.get("status")}},
        return_document=True
    )
    if updated_task:
        return jsonify({"message": "Task updated"}), 200
    return jsonify({"error": "Task not found"}), 404

def delete_task(mongo, task_id):
    result = mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count > 0:
        return jsonify({"message": "Task deleted"}), 200
    return jsonify({"error": "Task not found"}), 404