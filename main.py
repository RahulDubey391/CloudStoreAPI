import os,sys
from flask import Flask
from api import CloudStoreEnd
sys.path.append(os.getcwd())

app = Flask(__name__)

#app.from_object(Config)
app.register_blueprint(CloudStoreEnd)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get("PORT",5050)),host='0.0.0.0')