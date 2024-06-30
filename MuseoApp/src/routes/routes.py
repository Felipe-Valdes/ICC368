from flask import Blueprint, jsonify, request
from src.persistence.ExpositionRepository import ExpositionRepository
from src.persistence.ArtefactRepository import ArtefactRepository
from src.persistence.ThemeRepository import ThemeRepository
from src.persistence.VisitorRepository import VisitorRepository
from src.business.VisitorService import VisitorService

# Crea un Blueprint para las rutas
bp_routes = Blueprint('routes', __name__)

# Inicializa los repositorios
exposition_repo = ExpositionRepository()
artefact_repo = ArtefactRepository()
theme_repo = ThemeRepository()
visitor_repo = VisitorRepository()

# Inicializa el servicio de visitantes
visitor_service = VisitorService()

# Usa CORS para permitir solicitudes desde cualquier origen
@bp_routes.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE')
    return response

# Requerimiento 1: Obtener la lista de visitantes y exposiciones entre dos fechas ordenadas por fecha de inicio de la exposición
@bp_routes.route('/visitors-and-exhibitions', methods=['GET'])
def get_visitors_and_exhibitions():
    try:
        start_date = request.args.get('start_date', type=str)
        end_date = request.args.get('end_date', type=str)

        if not start_date or not end_date:
            return jsonify({'error': 'start_date and end_date are required'}), 400

        # Obtener los datos desde el servicio de visitantes
        data = visitor_service.get_json_visitors_and_exhibition_between_dates_ordered_by_start_date(start_date, end_date)
        
        return jsonify(data), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Requerimiento 2: Obtener las exhibiciones junto con los artefactos que contienen, ordenados por fecha de inicio
@bp_routes.route('/expositions-and-artefacts', methods=['GET'])
def get_expositions_and_artefacts():
    try:
        # Obtener los datos desde el repositorio de exhibiciones
        data = exposition_repo.get_expositions_and_artefacts_ordered_by_start_date()
        
        return jsonify(data.to_dict(orient='records')), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Requerimiento 3: Obtener artefactos y las exhibiciones en las que han participado, con filtros opcionales
@bp_routes.route('/artefacts-and-expositions', methods=['GET'])
def get_artefacts_and_expositions():
    try:
        artefact_id = request.args.get('artefact_id', type=int)
        start_date = request.args.get('start_date', type=str)
        end_date = request.args.get('end_date', type=str)

        if artefact_id and start_date and end_date:
            # Filtro por ID de artefacto y rango de fechas
            data = artefact_repo.get_artefacts_and_exhibitions_between_dates_by_artefact_id(
                artefact_id=artefact_id,
                start_date=start_date,
                end_date=end_date
            )
        elif artefact_id:
            # Filtro por ID de artefacto
            data = artefact_repo.get_artefacts_and_exhibitions_by_artefact_id(artefact_id)
        elif start_date and end_date:
            # Filtro por rango de fechas
            data = artefact_repo.get_artefacts_and_exhibitions_between_dates(start_date, end_date)
        else:
            # Sin filtros
            data = artefact_repo.get_artefacts_and_exhibitions()

        return jsonify(data.to_dict(orient='records')), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Requerimiento 4: Obtener datos de visitantes por periodo de tiempo
@bp_routes.route('/visitors-by-date', methods=['GET'])
def get_visitors_graph():
    try:
        start_date = request.args.get('start_date', default=None, type=str)
        end_date = request.args.get('end_date', default=None, type=str)
        period = request.args.get('period', default='day', type=str)

        if not start_date or not end_date:
            return jsonify({'error': 'start_date and end_date are required'}), 400

        # Obtener los datos desde el repositorio de visitantes
        data = visitor_repo.get_visitors_by_date_range(start_date, end_date, period)
        
        return jsonify(data.to_dict(orient='records')), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Requerimiento 5: Obtener artefactos ordenados por familia y nombre
@bp_routes.route('/artefacts-by-family', methods=['GET'])
def get_artefacts_by_family():
    try:
        # Obtener los artefactos desde el repositorio
        artefacts = artefact_repo.get_artefacts_ordered_by_family_and_name()
        
        return jsonify(artefacts.to_dict(orient='records')), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Requerimiento 6: Obtener el porcentaje de crecimiento de visitantes por periodo de tiempo
@bp_routes.route('/visitors-growth-rate', methods=['GET'])
def get_visitors_growth_rate():
    try:
        # Obtener el porcentaje de crecimiento de visitantes
        growth_data = visitor_service.get_json_visitors_growth_percentage()
        print(growth_data)
        print(jsonify(growth_data), 200)
        return jsonify(growth_data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp_routes.route('/expositions-with-tours', methods=['GET'])
def get_expositions_with_tours():
    try:
        # Obtener todas las exposiciones con el total de recorridos
        expositions_with_tours = exposition_repo.get_expositions_and_total_tours()
        
        # Convertir el DataFrame a una lista de diccionarios
        expositions_list = expositions_with_tours.to_dict(orient='records')
        
        # Devolver la lista como JSON
        return jsonify(expositions_list), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Requerimiento 7: Obtener exposiciones con total de recorridos en un intervalo de fechas
@bp_routes.route('/expositions-with-tours-between-dates', methods=['GET'])
def get_expositions_with_tours_between_dates():
    try:
        # Obtener parámetros de la fecha de inicio y fecha de término desde la solicitud
        fecha_inicio = request.args.get('start_date', default=None, type=str)
        fecha_termino = request.args.get('end_date', default=None, type=str)

        if not fecha_inicio or not fecha_termino:
            return jsonify({'error': 'start_date and end_date are required'}), 400

        # Obtener las exposiciones con el total de recorridos en el intervalo de fechas especificado
        expositions_with_tours_between_dates = exposition_repo.get_expositions_and_total_tours_between_dates(fecha_inicio, fecha_termino)
        
        # Convertir el DataFrame a una lista de diccionarios
        expositions_list = expositions_with_tours_between_dates.to_dict(orient='records')
        
        # Devolver la lista como JSON
        return jsonify(expositions_list), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# Requerimiento 8: Obtener visitantes ordenados por cantidad de recorridos realizados
@bp_routes.route('/visitors-ordered-by-attendances', methods=['GET'])
def get_visitors_ordered_by_attendances():
    try:
        # Obtener los visitantes ordenados por cantidad de recorridos
        visitors_ordered = visitor_service.get_json_visitors_ordered_by_number_of_attendances()
        
        # Devolver la lista como JSON
        return jsonify(visitors_ordered), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Requerimiento 9: Obtener temas junto con las exposiciones que contienen
@bp_routes.route('/themes-with-expositions', methods=['GET'])
def get_themes_with_expositions():
    try:
        # Obtener los temas con las exposiciones que contienen
        themes_with_expositions = theme_repo.get_themes_and_expositions()
        
        # Convertir el DataFrame a una lista de diccionarios
        themes_list = themes_with_expositions.to_dict(orient='records')
        
        # Devolver la lista como JSON
        return jsonify(themes_list), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# Requerimiento 10: Obtener exposiciones junto con las empresas que las visitan
@bp_routes.route('/expositions-with-visiting-companies', methods=['GET'])
def get_expositions_with_visiting_companies():
    try:
        # Obtener las exposiciones con las empresas visitantes
        expositions_with_companies = exposition_repo.get_expositions_and_visiting_companies()
        
        # Convertir el DataFrame a una lista de diccionarios
        expositions_list = expositions_with_companies.to_dict(orient='records')
        
        # Devolver la lista como JSON
        return jsonify(expositions_list), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)
    app.register_blueprint(bp_routes)
    app.run(debug=True)
