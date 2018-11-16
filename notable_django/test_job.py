import uuid
import datetime
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notable_django.settings')
django.setup()
from api.models import Jobs
import json
import requests

"""
Simple script to generate a job POST on the scheduler DB. This job should be assembled with a UI. The UI should be agnostic to which render-farm interface the process will be executed on
"""

name = 'Test job 2'
user = os.getlogin() 
timestamp = str(datetime.datetime.now())  # should be a DATETIMEField
job_id = uuid.uuid4() # the job id should be returned by the server once entered in the DB to avoid clashing

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

new_job = Jobs(job_id=job_id, name=name, user=user, cmd=params, timestamp=timestamp)
new_job.save()

print("{}".format(params))  # pylint: disable=no-member