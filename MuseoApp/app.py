# src/app.py

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from src.database.config import CONNECTION_STRING
from src.persistence.ArtefactRepository import ArtefactRepository
from src.persistence.ExpositionRepository import ExpositionRepository
from src.persistence.ThemeRepository import ThemeRepository
from src.persistence.VisitorRepository import VisitorRepository

app = Flask(__name__)

# Configuración de la base de datos MySQL desde config.py
app.config['SQLALCHEMY_DATABASE_URI'] = CONNECTION_STRING
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Repositorios
artefact_repo = ArtefactRepository()
exposition_repo = ExpositionRepository()
theme_repo = ThemeRepository()
visitor_repo = VisitorRepository()

# Rutas de la aplicación Flask

@app.route('/artefacts', methods=['GET'])
def get_artefacts():
    try:
        artefacts = artefact_repo.get_artefacts()
        return jsonify(artefacts.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


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

@app.route('/expositions_and_artefacts_ordered_by_start_date', methods=['GET'])
def get_expositions_and_artefacts_ordered_by_start_date():
    try:
        expositions_artefacts = exposition_repo.get_expositions_and_artefacts_ordered_by_start_date()
        return jsonify(expositions_artefacts.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/expositions_and_total_tours', methods=['GET'])
def get_expositions_and_total_tours():
    try:
        expositions_tours = exposition_repo.get_expositions_and_total_tours()
        return jsonify(expositions_tours.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/expositions_and_total_tours_between_dates', methods=['GET'])
def get_expositions_and_total_tours_between_dates():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    try:
        expositions_tours = exposition_repo.get_expositions_and_total_tours_between_dates(start_date, end_date)
        return jsonify(expositions_tours.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/expositions_and_visiting_companies', methods=['GET'])
def get_expositions_and_visiting_companies():
    try:
        expositions_companies = exposition_repo.get_expositions_and_visiting_companies()
        return jsonify(expositions_companies.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/themes_and_expositions', methods=['GET'])
def get_themes_and_expositions():
    try:
        themes_expositions = theme_repo.get_themes_and_expositions()
        return jsonify(themes_expositions.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/visitors_and_exhibition_between_dates_ordered_by_start_date', methods=['GET'])
def get_visitors_and_exhibition_between_dates_ordered_by_start_date():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    try:
        visitors_exhibitions = visitor_repo.get_visitors_and_exhibition_between_dates_ordered_by_start_date(start_date, end_date)
        return jsonify(visitors_exhibitions.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/visitors_by_date_range', methods=['GET'])
def get_visitors_by_date_range():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    periodo = request.args.get('periodo', 'day')
    
    try:
        visitors_range = visitor_repo.get_visitors_by_date_range(start_date, end_date, periodo)
        return jsonify(visitors_range.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/visitors_by_year_month', methods=['GET'])
def get_visitors_by_year_month():
    try:
        visitors_year_month = visitor_repo.get_visitors_by_year_month()
        return jsonify(visitors_year_month.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/visitors_ordered_by_number_of_attendances', methods=['GET'])
def get_visitors_ordered_by_number_of_attendances():
    try:
        visitors_ordered = visitor_repo.get_visitors_ordered_by_number_of_attendances()
        return jsonify(visitors_ordered.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para obtener todos los datos
@app.route('/all_data', methods=['GET'])
def get_all_data():
    try:
        # Obtener los datos de todos los repositorios
        artefacts_exhibitions = artefact_repo.get_artefacts_and_exhibitions()
        artefacts_ordered = artefact_repo.get_artefacts_ordered_by_family_and_name()
        expositions_artefacts = exposition_repo.get_expositions_and_artefacts_ordered_by_start_date()
        expositions_tours = exposition_repo.get_expositions_and_total_tours()
        themes_expositions = theme_repo.get_themes_and_expositions()
        visitors_between_dates = visitor_repo.get_visitors_and_exhibition_between_dates_ordered_by_start_date('2023-01-01', '2023-12-31')
        visitors_by_date_range = visitor_repo.get_visitors_by_date_range('2023-01-01', '2023-12-31', periodo='month')
        visitors_by_year_month = visitor_repo.get_visitors_by_year_month()
        visitors_ordered = visitor_repo.get_visitors_ordered_by_number_of_attendances()
        
        # Combinar los resultados en un diccionario
        all_data = {
            'artefacts_exhibitions': artefacts_exhibitions.to_dict(orient='records'),
            'artefacts_ordered': artefacts_ordered.to_dict(orient='records'),
            'expositions_artefacts': expositions_artefacts.to_dict(orient='records'),
            'expositions_tours': expositions_tours.to_dict(orient='records'),
            'themes_expositions': themes_expositions.to_dict(orient='records'),
            'visitors_between_dates': visitors_between_dates.to_dict(orient='records'),
            'visitors_by_date_range': visitors_by_date_range.to_dict(orient='records'),
            'visitors_by_year_month': visitors_by_year_month.to_dict(orient='records'),
            'visitors_ordered': visitors_ordered.to_dict(orient='records')
        }
        
        return jsonify(all_data), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
