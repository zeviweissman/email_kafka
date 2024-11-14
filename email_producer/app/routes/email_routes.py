from flask import Blueprint, request, jsonify
import email_producer.app.service.email_service as email_service


email_blueprint = Blueprint('email', __name__)


@email_blueprint.route('/', methods=['POST'])
def new_email():
    email = request.json
    email_service.produce_email(email)
    return jsonify("email recived"), 200
