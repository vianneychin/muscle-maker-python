from peewee import *
from flask_bcrypt import generate_password_hash
from flask_login import UserMixin

import config


DATABASE = SqliteDatabase( 'muscle_maker.sqlite' )

class User(UserMixin, Model):
    username    = CharField(unique=True)
    email       = CharField(unique=True)
    password    = CharField() 

    class Meta:
        database = DATABASE

    @classmethod
    def create_user(cls, username, email, password, **kwargs):
        email = email.lower()
        try:
            cls.select().where(
                (cls.email==email)
            ).get()
        except cls.DoesNotExist:
            user = cls(username=username, email=email)
            user.password = generate_password_hash(password)
            
            user.save()
            return user
        else:
             return 'User With that email already exists'


class Workout(Model):
    muscle       = CharField()
    workout_name = CharField()
    equipment    = CharField()
    weight       = CharField()
    sets         = CharField()
    reps         = CharField()
    created_by   = ForeignKeyField(User, related_name = 'workouts')

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables( [User, Workout], safe=True )
    DATABASE.close()