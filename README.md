# Vishal DevOps Server 🚀

Hello from Vishal DevOps Server!  

This project demonstrates a fully automated CI/CD pipeline using Docker Compose, Nginx, Flask, Redis,
and Jenkins deployed on AWS EC2.

---

## 📌 Project Overview

This is a **multi-container DevOps project** where:

- Nginx serves as the frontend and reverse proxy  
- Flask acts as the backend API  
- Redis stores and increments visit counts  
- Docker Compose manages all services  
- Jenkins automates deployment using GitHub Webhooks  

---

## 🏗️ Architecture

```
GitHub --> Webhook --> Jenkins --> Docker Compose --> Nginx --> Flask --> Redis
```

---

## 🛠️ Tech Stack

- **Cloud:** AWS EC2 (Amazon Linux 2023)  
- **Containerization:** Docker & Docker Compose  
- **Web Server:** Nginx  
- **Backend:** Flask + Gunicorn  
- **Database/Cache:** Redis  
- **CI/CD:** Jenkins + GitHub Webhooks  
- **Version Control:** Git & GitHub  

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone git@github.com:Vishal-AWS-Devops/devops-project.git
cd devops-project
```

### 2. Create Environment File
```bash
cp .env.example .env
nano .env
```

> ⚠️ Do NOT commit real secrets to GitHub

Example `.env`:
```
FLASK_ENV=production
REDIS_HOST=redis
REDIS_PORT=6379
```

---

### 3. Start Application
```bash
docker compose up -d
```

---

### 4. Check Running Containers
```bash
docker compose ps
```

---

### 5. View Logs
```bash
docker compose logs -f
```

---

## 🚀 Usage

### Frontend
```
http://<EC2_PUBLIC_IP>:8081/
```

### API Test
```bash
curl http://<EC2_PUBLIC_IP>:8081/api/
```

Example Response:
```
Hello from Vishal Devops Server 🚀
Visits: 7
```

---

## 🔄 CI/CD Automation

- GitHub push triggers webhook  
- Webhook triggers Jenkins pipeline  
- Jenkins runs Docker Compose deployment  
- Application updates automatically  

---

## 📸 Features

- Auto Deployment using Jenkins  
- Multi-container setup (Nginx + Flask + Redis)  
- Live Visit Counter (Redis integration)  
- Reverse Proxy using Nginx  
- Fully working CI/CD pipeline  

---

## ⚠️ Important Notes

- Always attach Elastic IP for consistent access  
- Do not push `.env` file with secrets  
- Restart containers after EC2 reboot:
```bash
docker compose up -d
```

---

## 💻 Author

**Vishal Manore**  
Aspiring Cloud DevOps Engineer 🚀
