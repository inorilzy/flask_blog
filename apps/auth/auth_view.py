from flask import jsonify, render_template
from . import auth_blueprint

@auth_blueprint.route('/hello/')
def hello():
    return render_template('hello.html')

