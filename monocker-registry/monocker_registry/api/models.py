from flask_restplus import Resource, abort

from monocker_registry.api.restplus import restplus_api
from monocker_registry.db.data_models import MonockerModelList
from monocker_registry.db.registry import getFreshModels, registerModel

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
    models = getFreshModels()
    return {'models': models}

  @api.response(202, 'No models found.')
  @api.response(201, 'Model(s) successfully registered.')
  @api.expect(MonockerModelList, validate=True, required=True)
  def post(self):
    # get models from request
    models = restplus_api.payload['models']

    # handle an empty models list
    if not len(models):
      return None, 202

    # save models in the registry db
    list(map(registerModel, models))#flask-restplus will Except any errors here
    return None, 201
#==============================================================================