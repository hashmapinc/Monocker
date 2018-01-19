import os

#==============================================================================
# Define global configs
#==============================================================================
#Get environment-set global configs
try:
  REGISTRY_HOSTNAME =   os.environ['REGISTRY_HOSTNAME']
  REGISTRY_PORT =   int(os.environ['REGISTRY_PORT'])
  REGISTRY_ROUTE =      os.environ['REGISTRY_ROUTE']

except Exception as e:
  print(e)
  print("===========================================================")
  print("          MISSING REQUIRED ENVIRONMENT VARIABLES!          ")
  print("===========================================================")
  exit(1)

#==============================================================================