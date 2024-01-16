import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django_asgi_app = get_asgi_application()

import chat.routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": URLRouter(chat.routing.websocket_urlpatterns),
})
