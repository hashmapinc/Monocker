from flask_restplus import Resource, abort
import requests

from monocker_api.api.restplus import restplus_api
from monocker_api.db.data_models import MonockerModelList

def getFreshModels():
  model0 = {
    'model_name': 'MNIST',
    'ip_address': 'monocker_model.service',
    'port':        80
  }
  model1 = {
    'model_name': 'INCEPTION',
    'ip_address': 'monocker_model.service',
    'port':        80
  }
  return [model0, model1]

#==============================================================================
# Models API 
#==============================================================================
#define namespace
api = restplus_api.namespace(
  'models', 
  description="Operations related to getting and posting models"
)

# Define /models route handlers
@api.route('/')
class Models(Resource):
  @api.response(404, 'Model not found.')
  @api.response(201, 'Successfully retrieved model(s).')
  @api.marshal_with(MonockerModelList)
  def get(self):
    # TODO: actually implement logic to call monocker-registry 
    models = getFreshModels()
    return {'models': models}
#==============================================================================