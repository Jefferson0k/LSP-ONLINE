from django.urls import re_path
from your_app_name import consumers

websocket_urlpatterns = [
    re_path(r'ws/some_path/$', consumers.YourConsumer.as_asgi()),
]
