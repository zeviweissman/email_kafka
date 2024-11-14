from flask import Blueprint, request, jsonify



email_blueprint = Blueprint('menu', __name__)


@gym_blueprint.route('/', methods=['POST'])
def new_email():
    email = request.json
    print(email)
    return jsonify("email recived"), 200


