from flask import request
from flask_restplus import Resource

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

  @api.response(201, 'Model successfully registered.')
  @api.expect(MonockerModelList, validate=True)
  def post(self):
    return request.json
#==============================================================================