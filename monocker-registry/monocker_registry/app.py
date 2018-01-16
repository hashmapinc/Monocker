from flask import Flask, request
from flask_restplus import Api

from monocker_registry import settings
from monocker_registry.api.models import api as models_api

#==============================================================================
# App 
#==============================================================================
# Setup flask
app = Flask(__name__)
api = Api(
  app, 
  version='0.1.0', 
  title='Monocker Registry API',
  description='A simple Monocker Registry API for managing Monocker Models in the Registry',
)

#add models api
api.add_namespace(models_api)

# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
#==============================================================================