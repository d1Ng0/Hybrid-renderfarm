from django.db import models

class Jobs(models.Model):
    
    """
    Models defines the data generated in the DB. We setup a table to keep track of all the jobs dispatched to the farm.
    Running Django migrations will setup these tables in the DB
    @TODO: defines the colums of the table. The current type is set to text but could use 
    better types for IDs and other fields
    https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.TextField
    """

    job_id = models.CharField(max_length=30) # should be a UUIDField
    name = models.CharField(max_length=200)
    user = models.CharField(max_length=30) 
    params = models.TextField() 
    timestamp = models.CharField(max_length=200)  # should be a DATETIMEField
    
    def __str__(self):
        s = "{} {} {} {} {}".format(self.job_id, self.name, self.user, self.cmd, self.timestamp)
        return s