from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pages_content.views import post_view

urlpatterns = [
    path('post', post_view, name='post_view')
]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
