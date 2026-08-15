from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Photos
from hotel_management_system .models import Booking
# Create your views here.


@login_required(login_url="/login/")
def members_View(request):
    user_post = Photos.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        title = request.POST['title'].strip()
        location = request.POST['location'].strip()
        description = request.POST['description'].strip()
        photo = request.FILES['photo']

        if title == '':
            messages.add_message(request, messages.ERROR, 'Empty Title.')
            return render(request, 'members.html', {})

        if location == '':
            messages.add_message(request, messages.ERROR, 'Empty location.')
            return render(request, 'members.html', {})

        if description == '':
            messages.add_message(request, messages.ERROR, 'Empty description.')
            return render(request, 'members.html', {})

        Photos.objects.create(title=title, location=location,
                              description=description, file=photo, user=request.user)

    data = Photos.objects.all().filter(user_id=request.user.id)
    print(data)
    booking = Booking.objects.all().filter(user=request.user.id)
    print(booking)
    return render(request, 'members.html', {"photoData": data, "booking": booking})
