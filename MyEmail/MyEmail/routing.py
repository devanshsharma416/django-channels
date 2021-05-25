from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import Sendmail.routing 


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            Sendmail.routing.websocket_urlpatterns

        )
    ),
    # (your routes here)
})