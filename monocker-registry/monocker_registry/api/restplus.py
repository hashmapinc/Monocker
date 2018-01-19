from flask_restplus import Api

#==============================================================================
# Restplus setup 
#==============================================================================
# init restplus Api
restplus_api = Api(
  version='0.1.0', 
  title='Monocker Registry API',
  description='A simple Monocker Registry API for managing Monocker Models in the Registry'
)
#==============================================================================