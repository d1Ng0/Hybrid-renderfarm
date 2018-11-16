import requests

"""
The first thing a scheduler should do is to keep an updated list of jobs to dispatch
Based on the number of jobs and available blades, the scheduler should know where to dispatch the new tasks
"""

"""
Connect to the server API 
"""

resp = requests.get('http://localhost:8000/api/') #temp address
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /jobs/ {}'.format(resp.status_code))
for todo_item in resp.json():
    print('{} {}'.format(todo_item['name'], todo_item['summary']))