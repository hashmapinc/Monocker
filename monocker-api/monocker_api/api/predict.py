from grpc.beta import implementations
import numpy
import tensorflow as tf

from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2

from flask_restplus import Resource, abort
import requests, traceback

from monocker_api.api.restplus import restplus_api
from monocker_api.db.data_models import MonockerModel
from monocker_api import settings

#==============================================================================
# helper functions
#==============================================================================
def getMonockerModelConnection(host, port):
  try:
    channel = implementations.insecure_channel(host, int(port))
    conn = prediction_service_pb2.beta_create_PredictionService_stub(channel)
  except Exception as e:
    print("===========================================================")
    print("Encountered error while requesting gRPC connection.")
    print("Error: ")
    print(e)
    traceback.print_exc()
    print("===========================================================")
    models = []
  return conn
#==============================================================================


#==============================================================================
# Models API 
#==============================================================================
# define namespace
api = restplus_api.namespace(
  'predict', 
  description="Operations related to requesting model evaluations"
)

# Define /models route handlers
@api.route('/')
class Models(Resource):
  @api.response(404, 'Model not found.')
  @api.response(201, 'Successfully retrieved model(s).')
  @api.expect(MonockerModelList, validate=True, required=True)
  def post(self):
    return {'models': getFreshModels()}
#==============================================================================