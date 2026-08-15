from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Photos
from hotel_management_system.models import Booking
# Create your views here.


@login_required(login_url="/login/")
def members_View(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        location = request.POST.get('location', '').strip()
        description = request.POST.get('description', '').strip()
        photo = request.FILES.get('photo')

        if not title:
            messages.error(request, 'Empty Title.')
        elif not location:
            messages.error(request, 'Empty location.')
        elif not description:
            messages.error(request, 'Empty description.')
        elif not photo:
            messages.error(request, 'Photo file is required.')
        else:
            Photos.objects.create(
                title=title, location=location,
                description=description, file=photo, user=request.user
            )
            messages.success(request, 'Photo uploaded successfully!')
            return redirect('members')

    data = Photos.objects.filter(user=request.user)
    booking = Booking.objects.filter(user=request.user).select_related('room', 'room__Category')
    return render(request, 'members.html', {"photoData": data, "booking": booking})

