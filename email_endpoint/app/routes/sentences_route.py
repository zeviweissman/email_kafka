from flask import Blueprint, request, jsonify
import email_endpoint.app.service.sentence_service as sentence_service


sentences_blueprint = Blueprint('sentences', __name__)


@sentences_blueprint.route('/common_word', methods=['GET'])
def get_most_common_word():
    common_word = sentence_service.get_most_common_word()
    return jsonify(common_word), 200
