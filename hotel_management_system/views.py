from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView
from .models import Room, Booking, RoomCategory
from .forms import AvailabilityForm
from hotel_management_system.booking.avaibilities import check_availability

# Create your views here.


class RoomList_View(ListView):
    model = Room


class BookingList_View(ListView):
    model = Booking


class BookingView(FormView):
    form_class = AvailabilityForm

    def form_valid(self, form):
        print(form)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data)
        cid = RoomCategory.objects.get(Category=self.get_queryset())
        room_list = Room.objects.filter(Category=cid)
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)
        if len(available_rooms) > 0:
            booking = Booking.objects.create(
                user=self.request.user,
                room=room,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()
            return render(booking)
        else:
            return HttpResponse("All the rooms are booked!!!")

    def get_queryset(self):
        return self.kwargs.get("Category")

    def get_context_data(self, **kwargs):
        Category = self.get_queryset()
        booking = Booking.objects.all().filter(user=self.request.user.id)
        book = []
        for b in booking:
            book.append(b.room.id)
        cid = RoomCategory.objects.get(Category=Category)
        room = Room.objects.filter(Category=cid)
        return {'room': room, "form": self.form_class, 'book': book}


def seperateromView(request, Category):
    cid = RoomCategory.objects.get(Category=Category)
    room = Room.objects.filter(Category=cid)
    return render(request, 'seperateroom.html', {"room": room})


def room_catView(request):
    return render(request, 'room_cat.html', {})
