import uuid
import datetime
import os
import json
import requests
import api_connector

"""
Simple interface for REST API. 
This methods should be assembled inside a UI once the API calls are defined. 
The UI should be agnostic to which render-farm interface the process will be executed on. This is why we use a REST API.
"""

class Interface():

    def __init__(self):
        # ESTABLISH CONNECTION WITH SCHEDULER-API
        base_url = 'http://localhost:8000/api/'
        self.connector = api_connector.API(base_url=base_url)

    def post_job(self):
        
        # POST A NEW JOB
        name = 'Test job'
        user = os.getlogin() 
        timestamp = str(datetime.datetime.now())  # should be a DATETIMEField
        params = dict()
        params['scene_file'] = '/filer/maya/test_project/scenes/test.mb'
        params['out_path'] = '/filer/maya/test_project/images/'
        params['renderer'] = 'arnold'
        params['frange'] = '1-100'
        params['step'] = '1'
        params['chunk_size'] = '2'
        params['xres'] = '640'
        params['yres'] = '480'
        params['camera'] = 'camera1'

        r = self.connector.post_job(name=name, user=user, params=params, timestamp=timestamp) # TODO: this is not working yet

    def get_jobs(self):

        # GET JOBS
        """
        Retrive all jobs from the scheduler
        r.headers['content-type']
        r.encoding
        r.text
        """
        r = self.connector.get_jobs()
        for n, job in enumerate(r['objects']):
            print("JOB:{} >>> DATA: {}".format(n, job))


if __name__ == '__main__':
    app = Interface()
    app.post_job()
    app.get_jobs()




