from .routes import Routes

from app.internal.routes import user

__routes__ = Routes(routers=(user.router,))
