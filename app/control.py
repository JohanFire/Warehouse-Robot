from flask import (
    Blueprint, 
    render_template,
    jsonify, 
    request
)

bp = Blueprint('control', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('control/index.html')

@bp.route('/hidden', methods=['GET'])
def hidden():
    return render_template('hidden.html')


#background process happening without any refreshing
@bp.route('/background_process_test')
def background_process_test():
    print ("Helloooo")
    return ("nothing")

# Ruta para cambiar el contenido del JSON a "Nuevo Contenido Uno"
@bp.route('/cambiar_contenido_uno', methods=['POST'])
def cambiar_contenido_uno():

    print('cambiar_contenido_uno()')

    nuevo_contenido = "Nuevo Contenido Uno"
    with open('datos.json', 'w') as file:
        file.write(f'{{"contenido": "{nuevo_contenido}"}}')

    return jsonify({'resultado': 'OK', 'nuevo_contenido': nuevo_contenido})

# Ruta para cambiar el contenido del JSON a "Nuevo Contenido Dos"
@bp.route('/cambiar_contenido_dos', methods=['POST'])
def cambiar_contenido_dos():
    nuevo_contenido = "Nuevo Contenido Dos"
    with open('datos.json', 'w') as file:
        file.write(f'{{"contenido": "{nuevo_contenido}"}}')
    return jsonify({'resultado': 'OK', 'nuevo_contenido': nuevo_contenido})