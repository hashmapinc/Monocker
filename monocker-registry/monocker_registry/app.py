from flask import Flask, request
from flask_restplus import Api, fields, Resource
import os, sqlite3, time

from monocker_registry import settings


#==============================================================================
# Helper functions
#==============================================================================
def createRegistryDB():
  conn = sqlite3.connect(REGISTRY_DB_PATH)
  conn.execute(REGISTRY_DB_CREATE)

def getFreshModels():
  now = int(time.time())
  return ["model_0", "model_1", "model_2"]

def registerModel(model, now=int(time.time())):
  try:
    model.registration_time = now
    print(model)
    conn = sqlite3.connect(REGISTRY_DB_PATH)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO monocker_models VALUES (?,?,?,?)", model)
    conn.commit()
    conn.close()
  except sqlite3.OperationalError as e:
    createRegistryDB()
    registerModel(model)
#==============================================================================


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

#define namespace
models_ns = api.namespace(
  'models', 
  description="Operations related to getting and posting models"
)

# Define models
MonockerModel = api.model('MonockerModel', {
  'model_name': fields.String,
  'ip_address': fields.String,
  'port':       fields.Integer
})

MonockerModelList = api.model('MonockerModelList', {
  'models': fields.List(fields.Nested(MonockerModel)),
})


# Define /models route handlers
@models_ns.route('/')
class Models(Resource):
  @api.response(404, 'Model not found.')
  @api.response(201, 'Successfully retrieved model(s).')
  @api.marshal_with(MonockerModelList)
  def get(self):
    models = getFreshModels()
    return {'models': models}

  @api.response(201, 'Model successfully registered.')
  @api.expect(MonockerModelList)
  def post(self):
    return request.json




# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
#==============================================================================