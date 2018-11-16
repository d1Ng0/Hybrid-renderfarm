import uuid
import datetime
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notable_django.settings')
django.setup()
from api.models import Jobs

"""
Simple script to generate a job in the DB.
"""

job_id = str(uuid.uuid4()) # will implement proper UUID later in the model
name = 'test job name'
user = 'dtrazzi'
cmd = 'mayabatch test cmd -f 1-100' 
timestamp = str(datetime.datetime.now())  # should be a DATETIMEField

new_job = Jobs(job_id=job_id, name=name, user=user, cmd=cmd, timestamp=timestamp)
new_job.save()

print("{}".format(Jobs.objects.all())) # pylint: disable=no-member