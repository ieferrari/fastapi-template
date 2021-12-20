# html rendering example
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from fastapi import APIRouter
from aux.read_file import openfile
import markdown

router = APIRouter()



templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def landing_page(request: Request):
    date = str(datetime.now()).split('.')[0]
    return templates.TemplateResponse("index.html",{"request": request, "date": date})

@router.get("/a")
async def landing():
    return {"msg": "landing"}
