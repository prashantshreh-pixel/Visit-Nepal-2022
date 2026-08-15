from django.urls import path

from .views import RoomList_View, BookingList_View, BookingView, seperateromView, room_catView

app_name = 'hotel'

urlpatterns = [
    path('booking_list/', BookingList_View.as_view(template_name='booking_list.html'),
         name='booking_list'),
    # path('book/', BookingView.as_view(template_name='booking.html'),
    #      name='book'),
    path('seperateroom/<str:Category>',
         BookingView.as_view(template_name='seperateroom.html'), name='room_seperate'),
    path('room_cat', room_catView, name='room_cat'),
]
