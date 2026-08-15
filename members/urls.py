from django.urls import path
from members.views import members_View
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('members', members_View, name='members'),
]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
