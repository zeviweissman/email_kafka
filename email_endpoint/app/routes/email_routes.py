from flask import Blueprint, request, jsonify
import email_endpoint.app.service.email_service as email_service


email_blueprint = Blueprint('menu', __name__)


@email_blueprint.route('/<email>', methods=['GET'])
def get_info_by_email(email):
    email_info = email_service.get_email_info_by_email_address(email)
    return jsonify(email_info), 200
