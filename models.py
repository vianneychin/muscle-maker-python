from peewee import *

DATABASE = SqliteDatabase('muscle_maker.sqlite')

class Workout(Model):
    muscle = CharField()
    workout_name = CharField()
    equipment = CharField()
    weight = CharField()
    sets = CharField()
    reps =CharField()

    class Meta: 
        database = DATABASE 


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Workout], safe=True)
    DATABASE.close()