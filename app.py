from flask import Flask, escape, request, jsonify

app = Flask(__name__)

students = []
classes = []
last_student_id = 1234455
last_class_id = 1122333


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/student')
def get_student():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: Please provide student ID"

    for student in students:
        if student['id'] == id:
            return jsonify(student)


@app.route('/class')
def get_class():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: Please provide class ID"

    for classs in classes:
        if classs['id'] == id:
            return jsonify(classs)


@app.route('/add_student', methods=['POST'])
def add_student():
    global last_student_id
    if not request.is_json:
        return "Please pass JSON object"
    content = request.get_json()
    last_student_id += 1
    students.append({'id': last_student_id, 'name': content["name"]})
    return jsonify(students)


@app.route('/add_class', methods=['POST'])
def add_class():
    global last_class_id
    if not request.is_json:
        return "Please pass JSON object"
    content = request.get_json()
    last_class_id += 1
    classes.append({'id': last_class_id, 'name': content["name"]})
    return jsonify(classes)

@app.route('/student_class', methods=['PATCH'])
def add_student_to_class():
    global last_class_id
    if not request.is_json:
        return "Please pass JSON object"
    content = request.get_json()
    last_class_id += 1
    classes.append({'id': last_class_id, 'name': content["name"]})
    return jsonify(classes)

app.run()
