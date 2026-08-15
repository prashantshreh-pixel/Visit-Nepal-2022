from django.urls import path
from .views import BookingList_View, BookingView, room_catView

app_name = 'hotel'

urlpatterns = [
    path('booking_list/', BookingList_View.as_view(template_name='booking_list.html'), name='booking_list'),
    path('seperateroom/<str:Category>', BookingView.as_view(), name='room_seperate'),
    path('seperateroom/<str:Category>/', BookingView.as_view(), name='room_seperate_slash'),
    path('room_cat', room_catView, name='room_cat'),
    path('room_cat/', room_catView, name='room_cat_slash'),
]
