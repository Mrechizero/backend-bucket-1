🪣 Bucket App

A simple backend application for managing file uploads and storage using a bucket-based system (S3 compatible).

🚀 Features

Upload files to a bucket

List stored files

Download files

Delete files

Bucket creation and validation

CORS enabled for frontend integration

Environment-based configuration

🏗️ Tech Stack

Backend: FastAPI

Storage: AWS S3 / S3-compatible service

Server: Uvicorn

Environment Config: Python dotenv

📁 Project Structure
bucket-app/
│
├── main.py
├── services/
│   └── storage.py
├── routers/
│   └── files.py
├── .env
├── requirements.txt
└── README.md

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/yourusername/bucket-app.git
cd bucket-app

2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

🔐 Environment Variables

Create a .env file in the root directory:

AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=us-east-1
BUCKET_NAME=your_bucket_name


If using a custom S3-compatible service:

S3_ENDPOINT_URL=https://your-storage-endpoint.com

▶️ Run the Application
uvicorn main:app --reload


The API will be available at:

http://127.0.0.1:8000


Swagger Docs:

http://127.0.0.1:8000/docs

📡 API Endpoints
Method	Endpoint	Description
POST	/upload	Upload file
GET	/files	List files
GET	/download/{id}	Download file
DELETE	/delete/{id}	Delete file
🛡️ CORS Configuration

CORS is enabled to allow frontend applications to connect.
Modify allowed origins in main.py:

origins = [
    "http://localhost:3000",
]

🧪 Example Upload (cURL)
curl -X POST "http://127.0.0.1:8000/upload" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@example.pdf"

📦 Deployment

You can deploy using:

Docker

AWS EC2

Railway

Render

Any VPS

📝 License

MIT License

If you want, I can also:

Generate a README specifically for your FastAPI + S3 project

Create a Docker-ready README

Adapt it for production environment

Or tailor it to your GitHub repo structure** 🚀
