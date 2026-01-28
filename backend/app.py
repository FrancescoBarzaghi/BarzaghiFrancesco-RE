from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from DatabaseWrapper import DatabaseWrapper

import os 

load_dotenv()
db = DatabaseWrapper(
    host=os.getenv("dbhost"),
    user=os.getenv("dbuser"),
    password=os.getenv("dbpassword"),
    database=os.getenv("dbdatabase"),
    port= int(os.getenv("dbport"))
)


app = Flask(__name__)

CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
    
    