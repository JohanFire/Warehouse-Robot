from flask import (
    Blueprint, 
    render_template,
    jsonify, 
    request,
    redirect,
    url_for
)
import json
import os

bp = Blueprint('control', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('control/index.html')

@bp.route('/hidden', methods=['GET'])
def hidden():
    return render_template('hidden.html')

def change_json(change_to: bool):
    # json_path = './database.json'
    json_path = os.path.abspath('app/database.json')

    with open(json_path, 'r') as file:
        # load JSON in a dict
        data = json.load(file)

        print(data)

    # True or False
    data['instruction'] = change_to

    with open(json_path, 'w') as file:
        json.dump(data, file, indent=4)

    print(f'json content: {json_path} modified succesfully.')

@bp.route('/hidden_forward', methods=['GET', 'POST'])
def hidden_forward():
    print('hidden_forward() !')

    if request.method == "POST":
        change_json(True)
        return render_template('hidden.html')
    
    return redirect(url_for('portfolio.index'))

@bp.route('/hidden_stop', methods=['GET', 'POST'])
def hidden_stop():
    print('hidden_stop() !')

    if request.method == "POST":
        change_json(False)
        return render_template('hidden.html')
    
    return redirect(url_for('portfolio.index'))








@bp.route("/forward/", methods=['POST'])
def move_forward():
    #Moving forward code
    forward_message = "Moving Forward..."
    return render_template('index.html', forward_message=forward_message);



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