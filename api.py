# ===============================================================
# Author: Rodolfo Ferro
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro,
# for his talk in UTL Here Hackathon 2018 at Universidad
# Tecnológica de León. Any explicit usage of this script
# or its contents is granted according to the license
# provided and its conditions.
# ===============================================================

# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from routing_api import routing_api
from pprint import pprint
import requests

# Main app:
api = Flask(__name__)

# Global:
version = 'v0.0'


# API MAIN STRUCTURE:
@api.route('/api/' + version, methods=['GET'])
def test():
    """
    GET method to test the API.
    """

    # Output message:
    message = {"response": [{"text": "Hello world!"}]}
    return jsonify(message)


@api.route('/api/' + version + '/do_something', methods=['POST'])
def do_something():
    """
    POST method to predict with our classification model.
    """

    # Get data from JSON object in POST method:
    req_data = request.get_json()

    # Parse data from JSON:
    ORIGIN = req_data['origin']
    DESTINY = req_data['destiny']

    # Set keys:
    YOUR_APP_ID = 'YOUR_APP_ID_GOES_HERE'
    YOUR_APP_CODE = 'YOUR_APP_CODE_GOES_HERE'

    # Get Here API response:
    response = routing_api(YOUR_APP_ID, YOUR_APP_CODE, ORIGIN, DESTINY)
    pprint(response)

    # Output message:
    message = {"response": [
        {"input": {
            'origin': ORIGIN,
            'destiny': DESTINY
        }},
        {"here_response": response}]}
    return jsonify(message)


@api.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404

    return response


if __name__ == '__main__':
    api.run(debug=True, port=5000)
