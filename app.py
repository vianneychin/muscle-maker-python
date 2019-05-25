import models
from flask              import Flask, g
from resources.workouts import workouts_api

DEBUG = True
PORT = 8000

app = Flask( __name__ )

#change this route later
app.register_blueprint( workouts_api, url_prefix = '/api/v1' )


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request( response ):
    g.db.close()
    return response



@app.route( '/' )
def index():
    return 'hi'

if __name__ == '__main__':
    models.initialize()
    app.run( debug = DEBUG, port = PORT )