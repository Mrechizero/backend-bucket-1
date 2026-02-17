from fastapi import FastAPI, UploadFile, File, HTTPException
import boto3
import os
from dotenv import load_dotenv

# Cargar .env (ruta absoluta en Windows)
load_dotenv(dotenv_path=r"C:\Users\User\Documents\Desarrollo\bucket-pruebas\backend\.env")

app = FastAPI()

# Leer variables (nombres correctos)
BUCKET_NAME = os.getenv("BUCKET_NAME")
AWS_REGION = os.getenv("AWS_REGION")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

print("BUCKET:", BUCKET_NAME)

# Validación para no fallar con 500 raro
if not BUCKET_NAME:
    raise RuntimeError("BUCKET_NAME no está configurado en .env")
if not AWS_REGION:
    raise RuntimeError("AWS_REGION no está configurado en .env")
if not AWS_ACCESS_KEY_ID or not AWS_SECRET_ACCESS_KEY:
    raise RuntimeError("Credenciales AWS no están configuradas en .env")

# Cliente S3
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
    if not BUCKET_NAME:
        raise HTTPException(500, "BUCKET_NAME es None")

    s3.upload_fileobj(file.file, BUCKET_NAME, file.filename)
    return {"message": "Archivo subido correctamente", "filename": file.filename}
