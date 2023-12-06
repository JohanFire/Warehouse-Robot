from flask import (
    Blueprint, 
    render_template
)

bp = Blueprint('control', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('control/index.html')

@bp.route('/hidden', methods=['GET'])
def hidden():
    return render_template('hidden.html')



def funcion_uno():
    # Lógica para la función uno
    return "Función Uno ejecutada"

def funcion_dos():
    # Lógica para la función dos
    return "Función Dos ejecutada"