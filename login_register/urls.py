from django.urls import path
from login_register.views import login_View, register_View, logout_View, delete_useruploads
urlpatterns = [
    path('login/', login_View, name='login'),
    path('register/', register_View, name='register'),
    path('logout/', logout_View, name='logout'),
    path('delete/', delete_useruploads, name='delete'),
]
