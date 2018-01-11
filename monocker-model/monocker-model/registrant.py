import os
import requests
import socket
import time

#==============================================================================
# Define global vars
#==============================================================================
# get local ip address
LOCAL_IP = socket.gethostbyname(socket.gethostname())

#Get environment-set global configs
try:
  TF_SERVING_PORT =         int(os.environ['REGISTRATION_FREQUENCY'])
  REGISTRATION_FREQUENCY =  int(os.environ['REGISTRATION_FREQUENCY'])
  REGISTRY_HOSTNAME =           os.environ['REGISTRY_HOSTNAME']
  REGISTRY_PORT =           int(os.environ['REGISTRY_PORT'])
  REGISTRY_ROUTE =              os.environ['REGISTRY_ROUTE']

except Exception as e:
  print(e)
  print("===========================================================")
  print("          MISSING REQUIRED ENVIRONMENT VARIABLES!          ")
  print("===========================================================")
  exit(1)
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
    "http://"+ REGISTRY_HOSTNAME +':'+ str(REGISTRY_PORT) +'/'+ REGISTRY_ROUTE
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