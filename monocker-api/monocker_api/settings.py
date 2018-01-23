import os, traceback

#==============================================================================
# Define global configs
#==============================================================================
#Get environment-set global configs
try:
  REGISTRY_HOSTNAME =   os.environ['REGISTRY_HOSTNAME']
  REGISTRY_PORT =   int(os.environ['REGISTRY_PORT'])
  REGISTRY_ROUTE =      os.environ['REGISTRY_ROUTE']

except Exception as e:
  print("===========================================================")
  print("          MISSING REQUIRED ENVIRONMENT VARIABLES!          ")
  print("Error:")
  print(e)
  traceback.print_exc()
  print("===========================================================")
  exit(1)

#==============================================================================