# First, we import our models tools
from django.db import models

# Remember: models are classes, so they must be defined with capital letters
class Crime(models.Model):
    # Documentation on all field types (CharField, DateTimeField, etc.) can be found here:
    # https://docs.djangoproject.com/en/dev/ref/models/fields/
    incident_num = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    apt_lot = models.CharField(max_length=20, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    # We're using this to hook up to the crime_data table we already created
    class Meta:
        db_table = 'crime_data'

    # The __unicode__ method defines how an individual instance of this class
    # will represent itself as a string.
    def __unicode__(self):
        return self.incident_num