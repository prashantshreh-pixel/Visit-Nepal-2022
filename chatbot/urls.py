from django.urls import path, include
from . import views

urlpatterns = [
	path('chatbotinterface', views.index, name='chatbotinterface')
]