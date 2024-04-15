from django import forms
from . models import Booking


# for geting date field
class Dateinput(forms.DateInput):
    input_type = 'date'


# form for booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'booking_date':Dateinput(),
        }
        labels= {
            'customer_name':'Customer Name:',
            'email':'Email:',
            'phone':'Phone:',
            'name':'Event Name:',
            'booking_date':'Booking Date:',
        }
