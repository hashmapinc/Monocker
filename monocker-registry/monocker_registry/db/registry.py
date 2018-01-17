import sqlite3, time

from monocker_registry import settings

#==============================================================================
# Helper functions
#==============================================================================
def createRegistryDB():
  conn = sqlite3.connect(settings.REGISTRY_DB_PATH)
  conn.execute(settings.REGISTRY_DB_CREATE)

def getFreshModels():
  now = int(time.time())
  return ["model_0", "model_1", "model_2"]

def registerModel(model, now=int(time.time())):
  try:
    model.registration_time = now
    print(model)
    conn = sqlite3.connect(settings.REGISTRY_DB_PATH)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO monocker_models VALUES (?,?,?,?)", model)
    conn.commit()
    conn.close()
  except sqlite3.OperationalError as e:
    createRegistryDB()
    registerModel(model)
#==============================================================================