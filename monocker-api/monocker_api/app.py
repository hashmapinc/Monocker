from flask import Flask, Blueprint, url_for

from monocker_api import settings
from monocker_api.api.restplus import restplus_api
from monocker_api.api.models import api as models_api
from monocker_api.api.index import bp as index_blueprint

#==============================================================================
# App 
#==============================================================================
# Setup flask
app = Flask(__name__)

# register restplus with flask
blueprint = Blueprint('api', __name__)
restplus_api.init_app(blueprint)
restplus_api.add_namespace(models_api)
app.register_blueprint(blueprint, url_prefix='/models')

# register index blueprint
app.register_blueprint(index_blueprint)

# Run app
if __name__ == '__main__':
  app.jinja_env.auto_reload = True
  app.run(host='0.0.0.0', port=80, debug=True)
#==============================================================================