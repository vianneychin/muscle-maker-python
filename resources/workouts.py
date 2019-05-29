from flask import jsonify, Blueprint, abort
from flask_restful import (Resource, Api, reqparse, fields,                             marshal, marshal_with, url_for)

from flask_login import login_required, current_user
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
            help='No workout name provided',
            location=['form', 'json']
        )

        self.reqparse.add_argument(
            'equipment',
            required=False,
            help='No equiptment provided',
            location=['form', 'json']
        )

        self.reqparse.add_argument(
            'weight',
            required=False,
            help='No weight provided',
            location=['form', 'json']
        )

        self.reqparse.add_argument(
            'sets',
            required=False,
            help='No sets provided',
            location=['form', 'json']
        )

        self.reqparse.add_argument(
            'reps',
            required=False,
            help='No reps provided',
            location=['form', 'json']
        )

        super().__init__()

    def get(self):
        all_workouts = [marshal(workout, workout_fields) for workout in models.Workout]
        return all_workouts

    @marshal_with(workout_fields)
    def post(self):
        args = self.reqparse.parse_args()
        print(args, '<----args (req.body)')
        workout = models.Workout.create(**args)
        return (workout, 201)

class Workout(Resource):
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
    #this is the show route

    @marshal_with(workout_fields)
    def get(self, id):
        try:
            workout = models.Workout.get(models.Workout.id==id)
        except models.Workout.DoesNotExist:
            abort(404)
        else:
            return(workout, 200)

    #this is the edit route
    @marshal_with(workout_fields)
    def put(self, id):
        args = self.reqparse.parse_args()
        query = models.Workout.update(**args).where(models.Workout.id==id)
        query.execute()
        return (models.Workout.get(models.Workout.id==id), 200)


    #this is the delete route
    # @marshal_with(workout_fields)
    def delete(self, id):
        query = models.Workout.delete().where(models.Workout.id==id)
        query.execute()
        return {'message': 'This workout has been deleted'}

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