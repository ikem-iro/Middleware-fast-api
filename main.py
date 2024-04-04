import uvicorn
from fastapi import FastAPI
from routes import home_route, upload_routes
from middlewares.middleware import log_middleware
from starlette.middleware.base import BaseHTTPMiddleware




app = FastAPI()




Host = "127.0.0.1"
Port = 8000

app.add_middleware(BaseHTTPMiddleware, dispatch= log_middleware)
app.include_router(home_route.router)
app.include_router(upload_routes.router, prefix="/v1")

if __name__ == "__main__":

    uvicorn.run("main:app", host=Host, port=Port, reload=True)