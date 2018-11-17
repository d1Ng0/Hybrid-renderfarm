"""API Connector."""
# from __future__ import absolute_import
import requests
import time
import datetime
import json
import base64
import uuid
# import logging
# from market_maker.auth import APIKeyAuthWithExpires
# from market_maker.utils import constants, errors
# from market_maker.ws.ws_thread import BitMEXWebsocket

class API(object):

    """ API Connector."""

    def __init__(self, base_url=None, postOnly=False, timeout=7):
        """Init connector."""
        self.base_url = base_url
        self.postOnly = postOnly
        self.retries = 0  # initialize counter

        # Prepare HTTPS session
        self.session = requests.Session()
        # These headers are always sent
        # self.session.headers.update({'user-agent': 'liquidbot-' + constants.VERSION})
        # self.session.headers.update({'content-type': 'application/json'})
        # self.session.headers.update({'accept': 'application/json'})
        self.timeout = timeout

    #
    # Public methods
    #
    def get_jobs(self):
        """Get all jobs data."""
        path = 'jobs/'
        url = self.base_url + path
        verb = 'GET'
        r = requests.request(verb, url)
        return r.json()

    def post_job(self,name, user, params, timestamp): # TODO NOT WORKING YET
        """Post a new job."""
        path = 'jobs/'
        url = self.base_url + path
        data = {'name': name, 'user': user, 'params': params, 'timestamp': timestamp}
        headers = {'Content-type': 'application/json'}
        r = requests.post(url, json.dumps(data), headers=headers)
        # print(r.text) # prints the text contained in the message
        return r