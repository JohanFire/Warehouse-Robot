import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SENDGRID_KEY=os.environ.get('SENDGRID_KEY')
    )

    from . import control

    app.register_blueprint(control.bp)

    return app