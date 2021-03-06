import sqlite3, time

from monocker_registry import settings

#==============================================================================
# creates the database and registry table
#==============================================================================
def createRegistryDB():
  conn = sqlite3.connect(settings.REGISTRY_DB_PATH)
  c = conn.cursor()
  c.execute(settings.REGISTRY_DB_CREATION_SQL)
  conn.commit()
  conn.close()
#==============================================================================


#==============================================================================
# gets a connection object for the registry db.
#
# if a database does not yet exist, one is created first and a conneciton
# to the newly created db is returned.
#==============================================================================
def getConnection():
  try:
    #Using a URI so that the conn throws an error if the db doesn't exist
    conn = sqlite3.connect(settings.REGISTRY_DB_URI, uri=True)
  except sqlite3.OperationalError as e:
    #to get here, db doesn't exist. Create it then try again.
    print("========================================")
    print(e)
    print("Creating database and retrying now")
    print("========================================")
    createRegistryDB()
    conn = getConnection()

  return conn
#==============================================================================


#==============================================================================
# Returns all models that have been registered in the last
# settings.REGISTRATION_FREQUENCY seconds
#==============================================================================
def getFreshModels():
  # calculate freshness cutoff
  now = int(time.time())
  cutoff = now - settings.REGISTRATION_FREQUENCY

  # get connection and cursor
  conn = getConnection()
  c = conn.cursor()

  # execute selection
  freshModels_raw = c.execute(
      settings.REGISTRY_SELECTION_SQL + str(cutoff)
    ).fetchall()
  conn.close()

  # convert tuples list to dicts list
  freshModels = []
  for model in freshModels_raw:
    freshModels.append({
      'model_name': model[0],
      'ip_address': model[1],
      'port':       model[2]
    })

  # return fresh models
  return freshModels
#==============================================================================


#==============================================================================
# Inserts model into the registry db with a registration_time of now
#==============================================================================
def registerModel(model):
  # get insertable tuple of the model
  insertable = (
    model['model_name'], 
    model['ip_address'], 
    model['port'], 
    int(time.time())
  )

  # get connection and cursor
  conn = getConnection()
  c = conn.cursor()

  # execute insertion
  c.execute(settings.REGISTRY_INSERTION_SQL, insertable)
  conn.commit()
  conn.close()
#==============================================================================