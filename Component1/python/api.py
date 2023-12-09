"""
This is the introduction for api.py
It contains classes and functions for monitoring FitHub system.
"""

from flask import Flask, jsonify
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

class ClassInfo:
    """
    This class integrates information about a class.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, class_id, time, instructor) -> None:
        self.class_id = class_id
        self.time = time
        self.instructor = instructor

class UserInfo:
    """
    This class integrates information about a user.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, user_id, schedule) -> None:
        self.user_id = user_id
        self.schedule = schedule

classes = [ClassInfo(1, "20:00", "Tommy")]
users = [UserInfo(1, [])]

@app.route('/classes/get', methods=['GET'])
def get_available_classes():
    """
    Get information about available classes.
    
    Returns:
    A list of classes with detailed information.
    """
    show_class = [{'class_id': c.class_id, 'time': c.time,
                   'instructor': c.instructor} for c in classes]
    return jsonify(show_class), 200

@app.route('/classes/<int:user_id>/<int:class_id>/book', methods=['POST'])
def book_class(user_id, class_id):
    """
    Booking classes function implementation.
    
    Returns:
    A class schedule of a user.
    """
    user = [u for u in users if u.user_id == user_id]
    cla = [c for c in classes if c.class_id == class_id]
    if user == [] or cla == []:
        return jsonify("Not exist User/class"), 404
    for i in user:
        i.schedule.append(class_id)
        schedule = i.schedule
    return jsonify(schedule), 200

@app.route('/classes/<int:user_id>/<int:class_id>/cancel', methods=['DELETE'])
def cancel_class(user_id, class_id):
    """
    Canceling classes function implementation.
    
    Returns:
    A class schedule of a user.
    """
    user = [u for u in users if u.user_id == user_id]
    cla = [c for c in classes if c.class_id == class_id]
    if user == [] or cla == []:
        return jsonify("Not exist User/class"), 404
    for i in user:
        i.schedule.remove(class_id)
        schedule = i.schedule
    return jsonify(schedule), 200

@app.route('/classes/<int:user_id>/schedule', methods=['GET'])
def get_schedule(user_id):
    """
    Getting schedule function implementation.
    
    Returns:
    A class schedule of a user.
    """
    user = [u for u in users if u.user_id == user_id]
    if user == []:
        return jsonify("Not exist User"), 404
    for i in user:
        schedule = i.schedule
    return jsonify(schedule), 200

@app.route('/classes/<int:class_id>/<string:class_time>/<string:class_instructor>/publish',
           methods=['POST'])
def publish_class(class_id, class_time, class_instructor):
    """
    Publishing new classes function implementation.
    
    Returns:
    A class list.
    """
    cla = [c for c in classes if c.class_id == class_id]
    if cla != []:
        return jsonify("Already exist class"), 404
    classes.append(ClassInfo(class_id, class_time, class_instructor))
    show_class = [{'class_id': c.class_id, 'time': c.time,
                   'instructor': c.instructor} for c in classes]
    return jsonify(show_class), 201

