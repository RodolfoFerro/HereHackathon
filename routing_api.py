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


def routing_api(YOUR_APP_ID, YOUR_APP_CODE, ORIGIN, DESTINY):
    """Function to test Here Geocoder API."""

    # Set base url with metadata:
    base_url = """https://route.api.here.com/routing/7.2/calculateroute.json"""
    base_url += "?app_id={}".format(YOUR_APP_ID)
    base_url += "&app_code={}".format(YOUR_APP_CODE)
    base_url += "&waypoint0=geo!{}".format(ORIGIN)
    base_url += "&waypoint1=geo!{}".format(DESTINY)
    base_url += "&mode=fastest;bicycle"

    # Consume Here API to gather info:
    response = requests.get(base_url)

    info = response.json()
    return info


if __name__ == '__main__':
    YOUR_APP_ID = 'YOUR_APP_ID_GOES_HERE'
    YOUR_APP_CODE = 'YOUR_APP_CODE_GOES_HERE'
    ORIGIN = 'YOUR_ORIGIN_GOES_HERE'
    DESTINY = 'YOUR_DESTINY_GOES_HERE'
    response = routing_api(YOUR_APP_ID, YOUR_APP_CODE, ORIGIN, DESTINY)
    pprint.pprint(response)
