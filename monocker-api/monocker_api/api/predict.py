from grpc.beta import implementations
import numpy
import traceback

import tensorflow as tf

from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2

from flask_restplus import Resource, abort

from monocker_api.api.restplus import restplus_api
from monocker_api.api.models import getModel
from monocker_api.db.data_models import PredictionRequest
from monocker_api import settings

#==============================================================================
# helper functions
#==============================================================================
def getMonockerModelStub(host, port):
  try:
    channel = implementations.insecure_channel(host, int(port))
    stub = prediction_service_pb2.beta_create_PredictionService_stub(channel)
  except Exception as e:
    print("===========================================================")
    print("Encountered error while requesting gRPC connection.")
    print("Error: ")
    print(e)
    traceback.print_exc()
    print("===========================================================")
    stub = None
  return stub


def getServingRequest(model, payload):
  request = predict_pb2.PredictRequest()
  request.model_spec.name = model['model_name']
  request.model_spec.signature_name = model['model_signature']

  request.inputs['images'].CopyFrom(
    tf.contrib.util.make_tensor_proto(
      payload['model_input'], 
      shape=payload['model_input_shape']
    )
  )

  return request
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
  @api.response(501, 'Error in model computation')
  @api.response(403, 'Could not connect to tf serving server')
  @api.response(404, 'Model not found.')
  @api.response(201, 'Successfully retrieved model evaluation.')
  @api.expect(PredictionRequest, validate=False, required=True)
  def post(self):
    # get inputs
    payload = restplus_api.payload

    # get model
    model = getModel(payload['model_name'])
    if model is None:
      return 'Model not found.', 404

    # get request
    model['model_signature'] = payload['model_signature']
    serving_request = getServingRequest(model, payload)

    # get stub
    stub = getMonockerModelStub(model['ip_address'], model['port'])
    if stub is None:
      return 'Could not connect to tf serving server', 403

    # make grpc prediction request then return results
    try:
      prediction = stub.Predict(serving_request, 5.0)
      model_response = list(prediction.outputs['scores'].float_val)
      return {'model_response': model_response}, 201

    except Exception as e:
      return str(e), 501
      
#==============================================================================