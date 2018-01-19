from flask_restplus import Api

#==============================================================================
# Restplus setup 
#==============================================================================
# init restplus Api
restplus_api = Api(
  version='0.1.0', 
  title='Monocker API',
  description='A simple frontend and robust API for interacting with Monocker'
)
#==============================================================================