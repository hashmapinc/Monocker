from flask import request
from flask_restplus import fields, Namespace, Resource
import os, sqlite3, time

from monocker_registry import settings

#==============================================================================
# Helper functions
#==============================================================================
def createRegistryDB():
  conn = sqlite3.connect(settings.REGISTRY_DB_PATH)
  conn.execute(settings.REGISTRY_DB_CREATE)

def getFreshModels():
  now = int(time.time())
  return ["model_0", "model_1", "model_2"]

def registerModel(model, now=int(time.time())):
  try:
    model.registration_time = now
    print(model)
    conn = sqlite3.connect(settings.REGISTRY_DB_PATH)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO monocker_models VALUES (?,?,?,?)", model)
    conn.commit()
    conn.close()
  except sqlite3.OperationalError as e:
    createRegistryDB()
    registerModel(model)
#==============================================================================


#==============================================================================
# Models API 
#==============================================================================
#define namespace
api = Namespace(
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
@api.route('/')
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
#==============================================================================