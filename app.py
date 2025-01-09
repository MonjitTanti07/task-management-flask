from flask import Flask
from flask_pymongo import PyMongo
from src.routes.taskRoutes import task_blueprint

app = Flask(__name__)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb+srv://monjit:monjit12@assignment-2-db.lnjk6.mongodb.net/task_management?retryWrites=true&w=majority&appName=Assignment-2-db"
mongo = PyMongo(app)

# Pass Mongo instance to routes
app.mongo = mongo

# Register Blueprints
app.register_blueprint(task_blueprint, url_prefix='/api/tasks')

if __name__ == '__main__':
    app.run(debug=True)