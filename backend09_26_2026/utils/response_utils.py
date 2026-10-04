from flask import jsonify

def error_response(message, status_code):
    return jsonify({
        "message": message
    }), status_code