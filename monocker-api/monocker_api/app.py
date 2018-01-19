from flask import Flask, Blueprint

from monocker_api import settings
from monocker_api.api.restplus import restplus_api

#==============================================================================
# App 
#==============================================================================
# Setup flask
app = Flask(__name__)

# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
#==============================================================================