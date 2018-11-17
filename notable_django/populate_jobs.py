import uuid
import datetime
import os
import django
import json
import requests
# DJANGO SETUP
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notable_django.settings')
django.setup()
from api.models import Jobs
###

"""
Simple script to generate a job on the DB. 
"""

name = 'Test job'
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

new_job = Jobs(job_id=job_id, name=name, user=user, params=params, timestamp=timestamp)
new_job.save()

print("{}".format(params))  # pylint: disable=no-member

# base_url = 'http://localhost:8000/api/'
# connector = api_connector.API(base_url=base_url)
# connector.get_jobs()

# logger.info("Connected to TESTNET")
# # order = self.bitmex.Order.Order_new(symbol=settings.SYMBOL, side='Buy', orderQty=100, ordType='Market').result()
# order = self.bitmex.Order.Order_new(symbol=settings.SYMBOL, side='Buy', orderQty=100, ordType='Limit', execInst='ParticipateDoNotInitiate', price='8700').result()
