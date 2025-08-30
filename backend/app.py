from flask import Flask, jsonify, request, redirect, url_for, render_template_string
from flask_cors import CORS
import json
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # Allow frontend requests

# MongoDB Atlas connection
client = MongoClient("mongodb+srv://rajuofficialk:cxIog0GaYUm0kqnO@cluster0.y0i7moy.mongodb.net/")
db = client["my_database"]
collection = db["my_collection"]

# API: read data.json and return list
@app.route('/api', methods=['GET'])
def get_data():
    with open("data.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

# API: form submission
@app.route('/submit', methods=['POST'])
def submit_data():
    try:
        data = request.json  # JSON from frontend
        collection.insert_one(data)  # Insert into MongoDB
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# Render To-Do Page
@app.route('/todo')
def todo_page():
    items = list(collection.find())
    return render_template("todo.html", items=items)

if __name__ == '__main__':
    app.run(debug=True)
