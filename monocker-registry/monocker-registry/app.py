from flask import Flask
from flask_restplus import Resource, Api, reqparse
import os, sqlite3, time


#==============================================================================
# Define global vars
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


REGISTRY_DB_CREATE = (
  "CREATE TABLE IF NOT EXISTS monocker_registry ( " +
    "model_name, ip_address, port, registration_time, " +
    "PRIMARY KEY (model_name, ip_address, port)" +
  ")"
)
#==============================================================================


#==============================================================================
# Helper functions
#==============================================================================
def createRegistryDB():
  conn = sqlite3.connect(REGISTRY_DB_PATH)
  conn.execute(REGISTRY_DB_CREATE)

def getFreshModels():
  now = int(time.time())
  return ["model_0", "model_1", "model_2"]

def registerModel(model, now=int(time.time())):
  try:
    model.registration_time = now
    conn = sqlite3.connect(REGISTRY_DB_PATH)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO monocker_models VALUES (?,?,?,?)", model)
    conn.commit()
    conn.close()
  except sqlite3.OperationalError as e:
    createRegistryDB()
    registerModel(model)
#==============================================================================


#==============================================================================
# Flask 
#==============================================================================
app = Flask(__name__)
api = Api(app)

@api.route('/models')
class Models(Resource):
    def get(self):
        model = ({
          "model_name": "mnist",
          "ip_address": "localhost",
          "port"      : 5000
        })
        return {'models': [model, model]}

    def post(self):
      map(registerModel, models)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
#==============================================================================