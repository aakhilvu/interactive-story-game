from fastapi import FastAPI,UploadFile,File,Form
import io
from fastapi.middleware.cors import CORSMiddleware
from PyPDF2 import PdfReader



app=FastAPI()


origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
async def receive_pdf(
    title: str = Form(None),
    file: UploadFile = File(None)
):
    if title:
        print("Title:", title)
    else:
        if file:
            print("File received:", file.filename)

            contents = await file.read()
            pdf = PdfReader(io.BytesIO(contents))

            extracted_text = ""

            for page in pdf.pages:
                extracted_text += page.extract_text() or ""

            print("\nExtracted Text:\n", extracted_text)

    return {"message": "success"}




