import fitz
import os

from typing import Optional

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

print(fitz.__doc__)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
document_files = os.listdir("documents")

@app.get("/", response_class=HTMLResponse)
def document_index(request: Request):    
    return templates.TemplateResponse("doc_index.html", {"request": request, "document_files": document_files})

@app.get("/docs/{doc_filename}")
def doc_information(doc_filename: str):
    doc = fitz.open("documents/" + doc_filename)
    return {"Name": doc.name,
            "Page Count": doc.page_count,
            "Metadata": doc.metadata,
            "Table of Contents": doc.get_toc()}

@app.get("/docs/{doc_filename}/pages", response_class=HTMLResponse)
async def doc_pages_index(request: Request, doc_filename: str):
    doc = fitz.open("documents/" + doc_filename)
    return templates.TemplateResponse("doc.html", {"request": request, "metadata": doc.metadata, "name": doc.name, "page_count": doc.page_count})

@app.get("/docs/{doc_filename}/pages/{page_no}", response_class=HTMLResponse)
async def read_doc_page(doc_filename: str, page_no: int, format: Optional[str] = ""):    
    doc = fitz.open("documents/" + doc_filename)
    page = doc.load_page(page_no)
    text = page.get_text(format)
    return text