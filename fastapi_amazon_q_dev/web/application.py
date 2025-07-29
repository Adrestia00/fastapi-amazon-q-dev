from importlib import metadata

from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from fastapi_amazon_q_dev.web.api.router import api_router
from fastapi_amazon_q_dev.web.lifespan import lifespan_setup


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(
        title="fastapi_amazon_q_dev",
        version=metadata.version("fastapi_amazon_q_dev"),
        lifespan=lifespan_setup,
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    # Main router for the API.
    app.include_router(router=api_router, prefix="/api")

    return app
