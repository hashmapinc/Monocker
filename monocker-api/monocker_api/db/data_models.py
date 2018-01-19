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
#==============================================================================