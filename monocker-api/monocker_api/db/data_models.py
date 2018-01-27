from flask_restplus import fields

from monocker_api.api.restplus import restplus_api


#==============================================================================
# Define data models
#==============================================================================
# Monocker Model object
MonockerModel = restplus_api.model('MonockerModel', {
  'model_name': fields.String(required=True, 
    description='Name of individual model'),
  'ip_address': fields.String(required=True, 
    description='IP address used to send requests to the model'),
  'port':       fields.Integer(required=True, 
    description='Port number used to send requests to the model')
})

# list of Monocker Models
MonockerModelList = restplus_api.model('MonockerModelList', {
  'models': fields.List(
    fields.Nested(MonockerModel), 
    required=True, 
    description='List of 1 or more Monocker Models'
  )
})

# prediction request object
PredictionRequest = restplus_api.model('PredictionRequest', {
  'model_name': fields.String(required=True, 
    description='Name of model to send predict request to.'),
  'model_signature': fields.String(required=True,
    description='Signature name used to define inputs/outputs of the model. ' +
    'This value was set when the model was saved for tf serving deployment.'),
  'model_input': fields.Raw(required=True,
    description="Input to the model. It is the caller's responsibility " +
    "to ensure that this input matches the model's requirements."),
  'model_input_shape': fields.List(fields.Integer(), required=True,
    description="Shape of the model input. For example, input=[[13,43]] would have a " +
    "shape of [1,2].")
  })
#==============================================================================