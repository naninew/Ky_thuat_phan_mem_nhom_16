from fastapi import FastAPI
from nicegui import app as nicegui_app, ui, html
from Pages.Login_page import Login_page

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@ui.page("/login")
def login():
    Login_page()


# Integrate with your FastAPI Application
ui.run_with(
    app=app,
    storage_secret="pick your private secret here",
)
