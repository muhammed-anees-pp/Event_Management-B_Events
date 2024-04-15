from django.db import models


# Model created for events
class Event(models.Model):
    img = models.ImageField(upload_to="photos")
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=250)

    def __str__(self):
        return self.name  #for showing the name on the booking


# Model created for booking
class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    name = models.ForeignKey(Event,on_delete=models.CASCADE)   #connected the model event and booking with foreignkey
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.customer_name