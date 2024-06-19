# src/app.py

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from src.database.config import CONNECTION_STRING
from src.persistence.ArtefactRepository import ArtefactRepository
from src.persistence.ExpositionRepository import ExpositionRepository

app = Flask(__name__)

# Configuración de la base de datos MySQL desde config.py
app.config['SQLALCHEMY_DATABASE_URI'] = CONNECTION_STRING
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Repositorios
artefact_repo = ArtefactRepository()
exposition_repo = ExpositionRepository()

# Rutas de la aplicación Flask

@app.route('/artefacts/exhibitions', methods=['GET'])
def get_artefacts_and_exhibitions():
    try:
        artefacts_exhibitions = artefact_repo.get_artefacts_and_exhibitions()
        return jsonify(artefacts_exhibitions.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/artefacts/<int:artefact_id>/exhibitions', methods=['GET'])
def get_artefacts_and_exhibitions_by_artefact_id(artefact_id):
    try:
        artefacts_exhibitions = artefact_repo.get_artefacts_and_exhibitions_by_artefact_id(artefact_id)
        return jsonify(artefacts_exhibitions.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/artefacts/exhibitions/between_dates', methods=['GET'])
def get_artefacts_and_exhibitions_between_dates():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    try:
        artefacts_exhibitions = artefact_repo.get_artefacts_and_exhibitions_between_dates(start_date, end_date)
        return jsonify(artefacts_exhibitions.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/artefacts/<int:artefact_id>/exhibitions/between_dates', methods=['GET'])
def get_artefacts_and_exhibitions_between_dates_by_artefact_id(artefact_id):
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    try:
        artefacts_exhibitions = artefact_repo.get_artefacts_and_exhibitions_between_dates_by_artefact_id(start_date, end_date, artefact_id)
        return jsonify(artefacts_exhibitions.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/artefacts/ordered_by_family_and_name', methods=['GET'])
def get_artefacts_ordered_by_family_and_name():
    try:
        artefacts_ordered = artefact_repo.get_artefacts_ordered_by_family_and_name()
        return jsonify(artefacts_ordered.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rutas para Exposiciones

@app.route('/expositions/artefacts', methods=['GET'])
def get_expositions_and_artefacts_ordered_by_start_date():
    try:
        expositions_artefacts = exposition_repo.get_expositions_and_artefacts_ordered_by_start_date()
        return jsonify(expositions_artefacts.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/expositions/tours', methods=['GET'])
def get_expositions_and_total_tours():
    try:
        expositions_tours = exposition_repo.get_expositions_and_total_tours()
        return jsonify(expositions_tours.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/expositions/tours/between_dates', methods=['GET'])
def get_expositions_and_total_tours_between_dates():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    try:
        expositions_tours = exposition_repo.get_expositions_and_total_tours_between_dates(start_date, end_date)
        return jsonify(expositions_tours.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/expositions/companies', methods=['GET'])
def get_expositions_and_visiting_companies():
    try:
        expositions_companies = exposition_repo.get_expositions_and_visiting_companies()
        return jsonify(expositions_companies.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
