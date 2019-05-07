from django.conf.urls import include, url
from django.contrib import admin

from . import views
urlpatterns = [
    url('^$', views.DayView.as_view(), name='day'),
    url('^photos/(?P<day>.*)/(?P<page>\d+)$', views.PhotosView.as_view(), name='photos'),
    url('^photo/(?P<image_id>\w+)', views.PhotoView.as_view(), name='photo'),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)