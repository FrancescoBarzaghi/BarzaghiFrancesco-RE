from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from DatabaseWrapper import DatabaseWrapper
import os

# Carica le variabili d'ambiente dal file .env
load_dotenv()

# Inizializza il database e crea le tabelle
db = DatabaseWrapper(
    host=os.getenv("dbhost"),
    user=os.getenv("dbuser"),
    password=os.getenv("dbpassword"),
    database=os.getenv("dbdatabase"),
    port=int(os.getenv("dbport"))
)
db.initialize()  # Tutto il setup del DB è qui dentro

# Inizializza Flask
app = Flask(__name__)
CORS(app)  # Abilita CORS per tutte le origini

@app.route("/grades", methods=["GET"])
def get_grades():
    """
    Endpoint che restituisce tutti i voti in formato JSON
    """
    try:
        grades = db.execute_query("SELECT * FROM grades ORDER BY grade_date DESC")
        return jsonify({"success": True, "grades": grades}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
