from django.urls import path
from pages.views import explore, culture, natural, sport, gallary
urlpatterns = [
    path('', explore, name='explore'),
    path('culture', culture, name='culture'),
    path('natural', natural, name='natural'),
    path('sport', sport, name='sport'),
    path('gallary', gallary, name='gallary'),
]
