from flask import (
    Blueprint, 
    render_template,
    jsonify, 
    request,
    redirect,
    url_for
)

bp = Blueprint('control', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('control/index.html')

@bp.route('/hidden', methods=['GET'])
def hidden():
    return render_template('hidden.html')

@bp.route('/hidden_forward', methods=['GET', 'POST'])
def hidden_forward():
    print('hidden_forward() !')

    if request.method == "POST":
        print('post!')
        return render_template('hidden.html')
    
    return redirect(url_for('portfolio.index'))

@bp.route('/hidden_stop', methods=['GET', 'POST'])
def hidden_stop():
    print('hidden_stop() !')

    if request.method == "POST":
        print('post!')
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