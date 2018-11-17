import uuid
import datetime
import os
import json
import requests
import api_connector

"""
Simple script to interface with REST API. 
This methods should be assembled inside a UI once the API calls are defined. 
The UI should be agnostic to which render-farm interface the process will be executed on. This is why we use a REST API.
"""

# ESTABLISH CONNECTION WITH SCHEDULER-API
base_url = 'http://localhost:8000/api/'
connector = api_connector.API(base_url=base_url)

# GET JOBS
"""
Retrive all jobs from the scheduler
r.headers['content-type']
r.encoding
r.text
"""
# r = connector.get_jobs()
# for n, job in enumerate(r['objects']):
    # print("JOB:{} >>> DATA: {}".format(n, job))

# POST A NEW JOB
name = 'Test job 2'
user = os.getlogin() 
timestamp = str(datetime.datetime.now())  # should be a DATETIMEField
# job_id = uuid.uuid4() # the job id should be returned by the server once entered in the DB to avoid clashing

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

# posting a job should return the job id if successful ...(?)
print("posting job ....")
r = connector.post_job(name=name, user=user, params=params, timestamp=timestamp)
# print(r['objects'])



