from . import bio_blueprint
from flask import render_template


@bio_blueprint.route('/')
def bio():
    return render_template('bio.html')
