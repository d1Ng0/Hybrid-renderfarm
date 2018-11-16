import requests

class Scheduler():
    """
    BAREBONE WIP: The first thing a scheduler should do is to keep an updated list of jobs to dispatch
    Then, based on the number of jobs and number of available blades, the scheduler should know where to dispatch the new tasks
    """
     
    resp = requests.get('http://localhost:8000/api/jobs/') #temp address Connect to the server API
    if resp.status_code != 200:
        # This means something went wrong.
        raise Exception('GET /jobs/ {}'.format(resp.status_code))
    data = resp.json()
    for obj in data['objects']:
        print(obj)

    # check how many free procs there are on local renderfarm
    # check if other (cloud) renderfarm is available
    # submit job (submit class should be abstract, each renderfarm should have an implementation to make it simple to switch between rendering farm options)


if __name__ == '__main__':
    app = Scheduler()







