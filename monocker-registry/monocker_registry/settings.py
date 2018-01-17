import os

#==============================================================================
# Define global configs
#==============================================================================
#Get environment-set global configs
try:
  REGISTRATION_FREQUENCY =  int(os.environ['REGISTRATION_FREQUENCY'])
  REGISTRY_DB_PATH =            os.environ['REGISTRY_DB_PATH']
  REGISTRY_TABLE_NAME =         os.environ['REGISTRY_TABLE_NAME']

except Exception as e:
  print(e)
  print("===========================================================")
  print("          MISSING REQUIRED ENVIRONMENT VARIABLES!          ")
  print("===========================================================")
  exit(1)


# Generate derived global configs
REGISTRY_DB_URI = 'file:' + REGISTRY_DB_PATH + '?mode=rw'
REGISTRY_DB_CREATION_SQL = (
  "CREATE TABLE IF NOT EXISTS " + REGISTRY_TABLE_NAME + " ( " +
    "model_name, " +
    "ip_address, " +
    "port, " +
    "registration_time, " +
    "PRIMARY KEY (model_name, ip_address, port)" +
  ")"
)
REGISTRY_INSERTION_SQL = (
  "INSERT OR REPLACE INTO " + 
  REGISTRY_TABLE_NAME + 
  " VALUES " +
  "(?,?,?,?)"
)
#==============================================================================