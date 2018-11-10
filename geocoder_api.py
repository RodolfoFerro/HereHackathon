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


def geocoder_api(YOUR_APP_ID, YOUR_APP_CODE, QUERY):
    """Function to test Here Geocoder API."""

    # Set base url with metadata:
    base_url = """https://geocoder.api.here.com/6.2/geocode.json"""
    base_url += "?app_id={}".format(YOUR_APP_ID)
    base_url += "&app_code={}".format(YOUR_APP_CODE)
    base_url += "&searchtext={}".format(QUERY)

    # Consume Here API to gather info:
    response = requests.get(base_url)

    info = response.json()
    return info


if __name__ == '__main__':
    # Set credentials and metadata:
    YOUR_APP_ID = 'YOUR_APP_ID_GOES_HERE'
    YOUR_APP_CODE = 'YOUR_APP_CODE_GOES_HERE'
    QUERY = 'YOUR_QUERY_GOES_HERE'

    # Consume API:
    response = geocoder_api(YOUR_APP_ID, YOUR_APP_CODE, QUERY)
    pprint.pprint(response)

    # Parse response:
    # TODO
