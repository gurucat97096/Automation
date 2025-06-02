from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/greet", response_class=HTMLResponse)
async def greet_user(request: Request, name: str = Form(None)):
    message = f"Hello, {name}"
    return templates.TemplateResponse("index.html", {"request": request, "greeting": message})