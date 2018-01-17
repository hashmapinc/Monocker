from flask import Flask, Blueprint

from monocker_registry import settings
from monocker_registry.api.restplus import restplus_api
from monocker_registry.api.models import api as models_api

#==============================================================================
# App 
#==============================================================================
# Setup flask
app = Flask(__name__)

# register restplus with flask
blueprint = Blueprint('api', __name__)
restplus_api.init_app(blueprint)
restplus_api.add_namespace(models_api)
app.register_blueprint(blueprint)

# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
#==============================================================================