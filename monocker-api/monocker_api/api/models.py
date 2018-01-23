from flask_restplus import Resource, abort
import requests, traceback

from monocker_api.api.restplus import restplus_api
from monocker_api.db.data_models import MonockerModelList
from monocker_api import settings

#==============================================================================
# helper functions
#==============================================================================
# TODO: actually implement logic to call monocker-registry 
def getFreshModels():
  target  = (
    "http://"+ settings.REGISTRY_HOSTNAME +':'+ str(settings.REGISTRY_PORT) + 
    '/' + settings.REGISTRY_ROUTE + '/'
  ) 
  try:
    response = requests.get(target).json()
    models = response['models']
  except Exception as e:
    print("===========================================================")
    print("Encountered error while requesting models.")
    print("Error: ")
    print(e)
    traceback.print_exc()
    print("===========================================================")
    models = []
  return models
#==============================================================================


#==============================================================================
# Models API 
#==============================================================================
# define namespace
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
    return {'models': getFreshModels()}
#==============================================================================