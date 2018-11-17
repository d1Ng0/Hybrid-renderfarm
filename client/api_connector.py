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

    def post_job(self,name, user, params, timestamp):
        """Post a new job."""
        path = 'jobs/'
        url = self.base_url + path
        # verb = 'POST'
        # data = {'name': name, 'user': user, 'params': params, 'timestamp': timestamp}
        # r = requests.request(verb, url, data=data)
        r = requests.put(url, data = {'key':'value'})
        return

    def test(self):
        r = requests.request('GET','http://localhost:8000/api/jobs/')
        # r = requests.get('http://localhost:8000/api/jobs/', auth=('user', 'pass'))
        print(r.status_code)
        print(r.headers['content-type'])
        print(r.encoding)
        print(r.text)
        print(r.json())

    def _curl(self, path, query=None, postdict=None, timeout=None, verb=None, rethrow_errors=False, max_retries=None):
        """Send a request to Servers"""
        # Handle URL
        url = self.base_url + path

        if timeout is None:
            timeout = self.timeout

        # Default to POST if data is attached, GET otherwise
        if not verb:
            verb = 'POST' if postdict else 'GET'

        # By default don't retry POST or PUT. Retrying GET/DELETE is okay because they are idempotent.
        # In the future we could allow retrying PUT, so long as 'leavesQty' is not used (not idempotent),
        # or you could change the clOrdID (set {"clOrdID": "new", "origClOrdID": "old"}) so that an amend
        # can't erroneously be applied twice.
        if max_retries is None:
            max_retries = 0 if verb in ['POST', 'PUT'] else 3


        def exit_or_throw(e):
            if rethrow_errors:
                raise e
            else:
                exit(1)

        def retry():
            self.retries += 1
            if self.retries > max_retries:
                raise Exception("Max retries on %s (%s) hit, raising." % (path, json.dumps(postdict or '')))
            return self._curl_bitmex(path, query, postdict, timeout, verb, rethrow_errors, max_retries)

        # Make the request
        response = None
        try:
            req = requests.Request(verb, url, json=postdict, params=query)
            prepped = self.session.prepare_request(req)
            response = self.session.send(prepped, timeout=timeout)
            # Make non-200s throw
            response.raise_for_status()

        except requests.exceptions.HTTPError as e:
            if response is None:
                raise e

            # 401 - Auth error. This is fatal.
            if response.status_code == 401:
                exit(1)

            # 404, can be thrown if order canceled or does not exist.
            elif response.status_code == 404:
                exit(1)

            # 429, ratelimit; cancel orders & wait until X-RateLimit-Reset
            elif response.status_code == 429:
                exit(1)

            # If we haven't returned or re-raised yet, we get here.

        except requests.exceptions.Timeout as e:
            # Timeout, re-run this request
            self.logger.warning("Timed out on request: %s (%s), retrying..." % (path, json.dumps(postdict or '')))
            return retry()

        except requests.exceptions.ConnectionError as e:
            self.logger.warning("Unable to contact the API (%s). Please check the URL. Retrying. " +
                                "Request: %s %s \n %s" % (e, url, json.dumps(postdict)))
            time.sleep(1)
            return retry()

        # Reset retry counter on success
        self.retries = 0

        return response.json()