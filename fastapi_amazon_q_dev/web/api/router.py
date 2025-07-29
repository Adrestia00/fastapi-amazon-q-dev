from fastapi.routing import APIRouter

from fastapi_amazon_q_dev.web.api import dummy, echo, monitoring
from fastapi_amazon_q_dev.web.api.library import views as library

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(dummy.router, prefix="/dummy", tags=["dummy"])
api_router.include_router(library.router, prefix="/library", tags=["library"])
