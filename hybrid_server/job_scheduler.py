import requests

"""
The first thing a scheduler should do is to keep an updated list of jobs to dispatch
Based on the number of jobs and available blades, the scheduler should know where to dispatch the new tasks
"""

"""
Connect to the server API 
"""

class APIError(Exception):
    """An API Error Exception"""

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "APIError: status={}".format(self.status)


resp = requests.get('http://localhost:8000/api/') #temp address
if resp.status_code != 200:
    # This means something went wrong.
    raise APIError('GET /jobs/ {}'.format(resp.status_code))
for todo_item in resp.json():
    print('{} {}'.format(todo_item['name'], todo_item['summary']))




