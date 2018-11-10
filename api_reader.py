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

import requests
import pprint
import json


def get_json(url, filename):
    """
    Download JSON response url for testing.
    """

    # Get response:
    response = requests.get(url)

    # If response's status is 200:
    if response.status_code == requests.codes.ok:
        # Pretty print response:
        pprint.pprint(response.json())

        # Save response into a JSON file:
        with open(filename, 'wt') as output:
            output.write(response.text)
    return


def get_something(url, filename):
    """
    Download JSON response url for prediction.
    """

    # Set metadata:
    headers = {'Content-type': 'application/json'}
    input_values = {'origin': 'YOUR_ORIGIN_GOES_HERE',
                    'destiny': 'YOUR_DESTINY_GOES_HERE'}

    # Get response:
    response = requests.post(url, json=input_values, headers=headers)

    # If response's status is 200:
    if response.status_code == requests.codes.ok:
        # Pretty print response:
        pprint.pprint(response.json())

        # Save response into a JSON file:
        with open(filename, 'wt') as output:
            output.write(response.text)
    return


if __name__ == '__main__':
    # Try out our JSON response downloader:
    test_resp, some_resp = 'test_response.json', 'something_response.json'
    get_json('http://localhost:5000/api/v0.0', test_resp)
    get_something('http://localhost:5000/api/v0.0/do_something', some_resp)
