#Adding comment in test branch
from fastapi import FastAPI
from app.utils.db import Base, engine
from app.controllers import task_controller
from app.utils.exception_handler import global_exception_handler

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(task_controller.router)

app.add_exception_handler(Exception, global_exception_handler)