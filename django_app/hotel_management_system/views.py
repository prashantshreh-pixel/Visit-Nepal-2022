from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Room, Booking, RoomCategory
from .forms import AvailabilityForm
from hotel_management_system.booking.avaibilities import check_availability


class RoomList_View(ListView):
    model = Room


class BookingList_View(ListView):
    model = Booking


@method_decorator(login_required(login_url="/login/"), name='dispatch')
class BookingView(FormView):
    template_name = 'seperateroom.html'
    form_class = AvailabilityForm

    def get_queryset(self):
        return self.kwargs.get("Category")

    def get_context_data(self, **kwargs):
        category_name = self.get_queryset()
        category = get_object_or_404(RoomCategory, Category=category_name)
        rooms = Room.objects.filter(Category=category).select_related('Category').order_by('Room_number')
        
        # User existing bookings
        user_bookings = Booking.objects.filter(user=self.request.user).select_related('room', 'room__Category')
        booked_room_ids = [b.room.id for b in user_bookings]

        context = super().get_context_data(**kwargs) if hasattr(super(), 'get_context_data') else {}
        context.update({
            'category': category,
            'rooms': rooms,
            'form': self.get_form(),
            'booked_room_ids': booked_room_ids,
        })
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        category_name = self.get_queryset()
        category = get_object_or_404(RoomCategory, Category=category_name)
        room_list = Room.objects.filter(Category=category).select_related('Category')

        # Optional: Specific room selection if submitted
        room_id = self.request.POST.get('room_id')
        if room_id:
            try:
                selected_room = Room.objects.get(pk=room_id, Category=category)
                if check_availability(selected_room, data['check_in'], data['check_out']):
                    Booking.objects.create(
                        user=self.request.user,
                        room=selected_room,
                        check_in=data['check_in'],
                        check_out=data['check_out']
                    )
                    messages.success(self.request, f'🎉 Room {selected_room.Room_number} ({category_name}) booked successfully!')
                    return redirect('members')
                else:
                    messages.error(self.request, f'Room {selected_room.Room_number} is already booked for these dates. Please choose another date or room.')
                    return redirect('hms:room_seperate', Category=category_name)
            except Room.DoesNotExist:
                pass

        # Fallback to any available room in this category
        available_rooms = [r for r in room_list if check_availability(r, data['check_in'], data['check_out'])]
        if available_rooms:
            booked_room = available_rooms[0]
            Booking.objects.create(
                user=self.request.user,
                room=booked_room,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            messages.success(self.request, f'🎉 Room {booked_room.Room_number} ({category_name}) booked successfully!')
            return redirect('members')
        else:
            messages.error(self.request, f'All {category_name} rooms are currently booked for the selected dates. Please try other dates.')
            return redirect('hms:room_seperate', Category=category_name)

    def form_invalid(self, form):
        category_name = self.get_queryset()
        messages.error(self.request, 'Please provide valid Check-in and Check-out dates and times.')
        return redirect('hms:room_seperate', Category=category_name)


@login_required(login_url="/login/")
def room_catView(request):
    categories = RoomCategory.objects.all()
    # Map sample room images for categories
    category_cards = []
    for cat in categories:
        sample_room = Room.objects.filter(Category=cat).first()
        min_price = Room.objects.filter(Category=cat).order_by('Price').first()
        category_cards.append({
            'category': cat,
            'image': sample_room.image.url if (sample_room and sample_room.image) else '',
            'min_price': min_price.Price if min_price else 4000,
            'room_count': Room.objects.filter(Category=cat).count(),
        })
    return render(request, 'room_cat.html', {'categories': category_cards})
