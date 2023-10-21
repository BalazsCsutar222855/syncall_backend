import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import editor_core.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'syncall_backend.settings')

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
    URLRouter(
      editor_core.routing.websocket_urlpatterns
    )
  )
})