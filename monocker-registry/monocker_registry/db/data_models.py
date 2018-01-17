from flask_restplus import fields

from monocker_registry.api.restplus import restplus_api

#==============================================================================
# Define data models
#==============================================================================
# Monocker Model object
MonockerModel = restplus_api.model('MonockerModel', {
  'model_name': fields.String,
  'ip_address': fields.String,
  'port':       fields.Integer
})

# list of Monocker Models
MonockerModelList = restplus_api.model('MonockerModelList', {
  'models': fields.List(fields.Nested(MonockerModel)),
})
#==============================================================================