from time import time

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/test")
def test():
    user_input = request.args.get("input").lower()

    import time
    time.sleep(4.5)

    if "student" in user_input:
        return jsonify({
            "tables": [
                "Students(id, name, email)",
                "Courses(id, title)",
                "Enrollments(student_id, course_id)"
            ],
            "relationships": [
                "Students enroll in Courses"
            ],
            "sql": [
                "CREATE TABLE Students (...);",
                "CREATE TABLE Courses (...);",
                "CREATE TABLE Enrollments (...);"
            ],
            "queries": [
                "SELECT * FROM Students;",
                "SELECT * FROM Courses;"
            ]
        })

    elif "ecommerce" in user_input or "shop" in user_input:
        return jsonify({
            "tables": [
                "Users(id, name)",
                "Products(id, price)",
                "Orders(id, user_id)"
            ],
            "relationships": [
                "Users place Orders"
            ],
            "sql": [
                "CREATE TABLE Users (...);",
                "CREATE TABLE Orders (...);"
            ],
            "queries": [
                "SELECT * FROM Orders;"
            ]
        })

    else:
        return jsonify({
            "tables": ["Entity(id, name)"],
            "relationships": ["Generic relationship"],
            "sql": ["CREATE TABLE Entity (...);"],
            "queries": ["SELECT * FROM Entity;"]
        })

if __name__ == "__main__":
    app.run(debug=True)