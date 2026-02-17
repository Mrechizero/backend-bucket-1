from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware   # 👈 IMPORTANTE
import boto3
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=r"C:\Users\User\Documents\Desarrollo\bucket-pruebas\backend\.env")

app = FastAPI()

# 🔓 CONFIGURAR CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # 👈 tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Variables
BUCKET_NAME = os.getenv("BUCKET_NAME")
AWS_REGION = os.getenv("AWS_REGION")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

if not BUCKET_NAME:
    raise RuntimeError("BUCKET_NAME no está configurado en .env")

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)

@app.get("/")
def root():
    return {"message": "API funcionando correctamente 🚀"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    s3.upload_fileobj(file.file, BUCKET_NAME, file.filename)
    return {"message": "Archivo subido correctamente", "filename": file.filename}