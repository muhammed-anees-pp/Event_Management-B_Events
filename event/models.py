from django.db import models


#Model created for events
class Event(models.Model):
    img = models.ImageField(upload_to="photos")
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=250)
