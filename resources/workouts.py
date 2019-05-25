from flask import jsonify, Blueprint
from flask_restful import Resource, Api

import models


class WorkoutList(Resource):
    def get(self):
        return jsonify({'workouts': [{'muscle': 'glutes'}]})

class Workout(Resource):
    def get(self, id):
        return jsonify({'muscle': 'glutes'})

    def put(self, id):
        return jsonify({'muscle': 'glutes'})

    def delete(self, id):
        return jsonify({'muscle': 'glutes'})

workouts_api = Blueprint('resources.workouts',__name__)
api = Api(workouts_api)
api.add_resource(
    WorkoutList, 
    '/workouts',
    endpoint='workouts'
)
api.add_resource(
    Workout,
    '/workouts/<int:id>',
    endpoint='workout'
)
    