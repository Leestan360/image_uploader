from fastapi import FastAPI
from fastapi.routing import APIRoute
from user_router import user_router
from image_router import image_router
import uvicorn


app = FastAPI()

app.include_router(user_router)
app.include_router(image_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)