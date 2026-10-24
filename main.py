
from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Practica CI/CD en AWS - Version 2 - Despliegue automatico exitoso"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
