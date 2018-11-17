from tastypie.resources import ModelResource
from api.models import Jobs
from tastypie.authorization import Authorization


class JobsResource(ModelResource):
    """
    Creates an API resource at the following address: http://localhost:8000/api/jobs/
    """
    class Meta:
        queryset = Jobs.objects.all() # pylint: disable=no-member
        resource_name = 'jobs'
        authorization = Authorization()
        # fields = ['job_id', 'name'] # to limit the resources
        always_return_data = True
