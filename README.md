## Stack de Tecnología

- **Framework:** [Next.js](https://nextjs.org/)

##🪣 Bucket App

A production-ready FastAPI backend for managing file uploads and storage using AWS S3 or S3-compatible services.

- **🚀 Features

Upload files to bucket

List stored files

Download files

Delete files

Automatic bucket validation

CORS enabled for frontend integration

Environment-based configuration

Docker deployment ready


- **🏗️ Tech Stack

Backend: FastAPI

Server: Uvicorn

Storage: AWS S3 / S3-compatible

Containerization: Docker

Environment Config: dotenv

OS (Production): Alpine Linux


- **📁 Project Structure
bucket-app/
│
├── main.py
├── services/
│   └── storage.py
├── routers/
│   └── files.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md


- **Create a .env file in the root directory:

AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=us-east-1
BUCKET_NAME=your_bucket_name
S3_ENDPOINT_URL=https://your-storage-endpoint.com  # optional


- **🖥️ Local Development
- **1️⃣ Clone repository
git clone https://github.com/yourusername/bucket-app.git

cd bucket-app

- **2️⃣ Create virtual environment
- 
python -m venv venv

source venv/bin/activate   # Linux/Mac

venv\Scripts\activate      # Windows

- **3️⃣ Install dependencies
- 
pip install -r requirements.txt

- **4️⃣ Run application
- 
uvicorn main:app --reload

API available at:

http://127.0.0.1:8000

Swagger Docs:

- **http://127.0.0.1:8000/docs

- **🐳 Production Deployment (Docker - Alpine Server)
📁 Server Path
/opt/apps/backend-bucket-1
🔨 Build & Deploy
cd /opt/apps/backend-bucket-1

sudo docker compose down

sudo docker compose build --no-cache
sudo docker compose up -d


- **🔎 Verify Deployment

Check running containers:

docker ps

Check logs:

docker logs -f backend-bucket-1


- **Test locally on server:

curl http://localhost:8000

Production URL (LAN example):

http://192.168.0.97:8000


- **🔄 Updating the Application
- 
cd /opt/apps/backend-bucket-1
-
git pull

sudo docker compose down
-
sudo docker compose build --no-cache

sudo docker compose up -d

- **📡 API Endpoints
- 
Method	Endpoint	Description

POST	/upload	Upload file

GET	/files	List files

GET	/download/{id}	Download file

DELETE	/delete/{id}	Delete file


- **🛡️ CORS Configuration

CORS is enabled for frontend integration.

Modify in main.py:

origins = [
    "http://localhost:3000",
    "http://192.168.0.97:3000"
]
- **🧪 Example Upload (cURL)
- 
curl -X POST "http://127.0.0.1:8000/upload" \

-H "Content-Type: multipart/form-data" \

-F "file=@example.pdf"

- **📊 Monitoring & Maintenance

View container status:

docker ps
-
docker ps -a

Restart backend:

docker compose restart

Check listening ports:

ss -tulpn | grep 8000

- **⚙️ Auto Start on Server Reboot (Alpine)

Enable Docker at boot:

sudo rc-update add docker default

sudo rc-service docker start

- **📦 Deployment Targets

Docker

AWS EC2

Any VPS

S3-compatible storage

On-premise server

- **📝 License

MIT License
