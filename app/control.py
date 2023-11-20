from flask import (
    Blueprint, 
    render_template
)

bp = Blueprint('control', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('control/index.html')