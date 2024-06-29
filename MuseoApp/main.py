from flask import Flask
from src.routes.routes import bp_routes  # Importa el blueprint de rutas

app = Flask(__name__)

# Registrar el blueprint de rutas
app.register_blueprint(bp_routes)

if __name__ == '__main__':
    app.run(debug=True)
