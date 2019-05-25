from flask import jsonify, Blueprint
from flask_restful import (Resource, Api, reqparse, fields,                             marshal, marshal_with, url_for)

import models

workout_fields = {
    'id': fields.Integer,
    'muscle': fields.String,
    'workout_name': fields.String,
    'equipment': fields.String, 
    'weight': fields.Integer,
    'sets': fields.Integer,
    'reps': fields.Integer
}


class WorkoutList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()

        self.reqparse.add_argument(
            'muscle',
            required=False,
            help='No muscle name provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'workout_name',
            required=False,
            help='No muscle name provided',
            location=['form', 'json']
        )

        self.reqparse.add_argument(
            'equipment',
            required=False,
            help='No muscle name provided',
            location=['form', 'json']
        )

        self.reqparse.add_argument(
            'weight',
            required=False,
            help='No muscle name provided',
            location=['form', 'json']
        )

        self.reqparse.add_argument(
            'sets',
            required=False,
            help='No muscle name provided',
            location=['form', 'json']
        )

        self.reqparse.add_argument(
            'reps',
            required=False,
            help='No muscle name provided',
            location=['form', 'json']
        )

        super().__init__()

    def get(self):
        return jsonify({'workouts': [{'muscle': 'glutes'}]})

    def post(self):
        args = self.reqparse.parse_args()
        print(args, '<----args (req.body)')
        workout = models.Workout.create(**args)
        return jsonify({'workouts': [{'muscle': 'glutes'}]})
        
class Workout(Resource):
    #this is the show route
    def get(self, id):
        return jsonify({'muscle': 'glutes'})

    #this is the update route
    def put(self, id):
        return jsonify({'muscle': 'glutes'})

    #this is the delete route
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
    