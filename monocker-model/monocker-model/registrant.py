import os
import requests
import socket
import time
import traceback

#==============================================================================
# Define global vars
#==============================================================================
# get local ip address
LOCAL_IP = socket.gethostbyname(socket.gethostname())

# get environment-set global configs
try:
  TF_SERVING_PORT =         int(os.environ['TF_SERVING_PORT'])
  REGISTRATION_FREQUENCY =  int(os.environ['REGISTRATION_FREQUENCY'])
  REGISTRY_HOSTNAME =           os.environ['REGISTRY_HOSTNAME']
  REGISTRY_PORT =           int(os.environ['REGISTRY_PORT'])
  REGISTRY_ROUTE =              os.environ['REGISTRY_ROUTE']

except Exception as e:
  print("===========================================================")
  print("          MISSING REQUIRED ENVIRONMENT VARIABLES!          ")
  print("Error:")
  print(e)
  traceback.print_exc()
  print("===========================================================")
  exit(1)
#==============================================================================


#==============================================================================
# Define helper functions
#==============================================================================
# This function detects all running models and generates a payload for
# registering these models with the monocker-registry
def getModels():
  # list model serving directories
  modelsDir = '/monocker-model/models'
  model_names = [
    d for 
      d in os.listdir(modelsDir) 
    if 
      os.path.isdir(os.path.join(os.path.abspath(modelsDir), d))
  ]

  # create models array
  models = [
    ({
      "model_name": model_name,
      "ip_address": LOCAL_IP,
      "port"      : TF_SERVING_PORT
    })
    for model_name in model_names
  ]

  return models


# This function registers all local models with the monocker-registry
def register():
  payload = {'models': getModels()}
  target  = (
    "http://"+ REGISTRY_HOSTNAME +':'+ str(REGISTRY_PORT) +'/'+ REGISTRY_ROUTE + '/'
  ) 
  requests.post(target, json=payload)
#==============================================================================


#==============================================================================
# Register local models every <REGISTRATION_FREQUENCY> seconds
#==============================================================================
# sleep for 5 seconds to ensure things have settled before first registration
time.sleep(5)

# perpetually register
while True:
  try:
    register()
  except Exception as e:
    print('\n')
    print(e)
    print('\n')

  # sleep for 90% of the frequency.
  time.sleep(int(REGISTRATION_FREQUENCY * 0.9))
#==============================================================================