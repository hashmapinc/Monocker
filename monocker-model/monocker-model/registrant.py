import os
import requests
import socket
import time

#==============================================================================
# Define global vars
#==============================================================================
# TODO: Add actual logic to get this information from k8s env vars
REGISTRY_HOSTNAME = ""
REGISTRY_IP = 10010
REGISTRY_ROUTENAME = "models" # this maybe shouldn't be hardcoded

LOCAL_IP = socket.gethostbyname(socket.gethostname())
TF_SERVING_PORT = 9000
#==============================================================================


#==============================================================================
# Define helper functions
#==============================================================================
# This function detects all running models and generates a payload for
# registering these models with the monocker-registry
def getModels():
  # TODO: Implement this for real
  model = {
    'model_name': "mnist",
    'ip_address': LOCAL_IP,
    'port'      : TF_SERVING_PORT
  }
  models = [].append(model)
  return models


# This function registers all local models with the monocker-registry
def register():
  payload = {'models': getModels()}
  target  = REGISTRY_HOSTNAME + ':' + REGISTRY_IP + '/' + REGISTRY_ROUTENAME
  println("target = " + target)
  println("payload:")
  println(payload)
  requests.post(target, data=payload)
#==============================================================================


#==============================================================================
# Register local models every 60 seconds
#==============================================================================
while True:
  register()
  time.sleep(60)
#==============================================================================