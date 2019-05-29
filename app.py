from flask import Flask, g
from flask_login import LoginManager
import models
from flask_cors import CORS
from resources.workouts import workouts_api
from resources.users import users_api
import config

login_manager = LoginManager()



app = Flask( __name__ )
app.secret_key = config.SECRET_KEY

login_manager.init_app(app)

@login_manager.user_loader
def load_users(userid):
    try:
        return models.User.get(models.User.id==userid)
    except models.DoesNotExist:
        return None

# #change this route later
# app.register_blueprint( workouts_api, url_prefix = '/api/v1' )

CORS(workouts_api, origins=['http://localhost:3000'], supports_credentials=True)
CORS(users_api, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(workouts_api, url_prefix='/api/v1')
app.register_blueprint(users_api, url_prefix='/users')



@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()
    # g.user = current_user

@app.after_request
def after_request( response ):
    g.db.close()
    return response



@app.route( '/' )
def index():
    return jsonfiy({'data': "I'm data"})

if __name__ == '__main__':
    models.initialize()
    app.run(debug=config.DEBUG, port=config.PORT)