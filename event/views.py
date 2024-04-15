from django.shortcuts import render, redirect
from . models import Event
from . forms import BookingForm


# views for home page
def index(request):
    return render(request,'index.html')

# views for about page
def about(request):
    return render(request,'about.html')

# views for events page
def events(request):
    dict_eve={
        'eve':Event.objects.all()
    }
    return render(request,'events.html',dict_eve)

# views for booking page
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    

    form = BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html', dict_form)

# views for contact page
def contact(request):
    return render(request,'contact.html')

