import os
import requests
import socket
import time

#==============================================================================
# Define global vars
#==============================================================================
# TODO: Add actual logic to get this information from k8s env vars
REGISTRY_HOSTNAME = "monocker.registry" # this maybe shouldn't be hardcoded
REGISTRY_IP = 10010 # this maybe shouldn't be hardcoded
REGISTRY_ROUTENAME = "models" # this maybe shouldn't be hardcoded

LOCAL_IP = socket.gethostbyname(socket.gethostname())
TF_SERVING_PORT = 9000

REGISTRATION_FREQUENCY = 60 #default
#Get environment-set frequency if it exists
try:
  REGISTRATION_FREQUENCY = int(os.environ['REGISTRATION_FREQUENCY'])
except Exception as e:
  print(e)
  print("Using default registration frequency: " + 
    str(REGISTRATION_FREQUENCY)) + " SECONDS"
#==============================================================================


#==============================================================================
# Define helper functions
#==============================================================================
# This function detects all running models and generates a payload for
# registering these models with the monocker-registry
def getModels():
  # TODO: Implement this for real
  model = ({
    "model_name": "mnist",
    "ip_address": LOCAL_IP,
    "port"      : TF_SERVING_PORT
  })
  models = [model]
  return models


# This function registers all local models with the monocker-registry
def register():
  payload = {'models': getModels()}
  target  = (
    "http://" + 
    REGISTRY_HOSTNAME +
    ':' + 
    str(REGISTRY_IP) +
    '/' + 
    REGISTRY_ROUTENAME
  ) 
  requests.post(target, data=payload)
#==============================================================================


#==============================================================================
# Register local models every <REGISTRATION_FREQUENCY> seconds
#==============================================================================
while True:
  try:
    register()
  except Exception as e:
    print('\n')
    print(e)
    print('\n')
  
  time.sleep(REGISTRATION_FREQUENCY)
#==============================================================================