from django.urls import re_path

from .consumers import TrackConsumer

websocket_urlpatterns = [
    re_path(r"ws/(?P<track_id>[-\w]+)/$", TrackConsumer.as_asgi()),
]
