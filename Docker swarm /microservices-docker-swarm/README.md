# Microservices Architecture with Docker Swarm ⚓

## Introduction
This repository contains a microservices-based architecture deployed on Docker Swarm. It includes an API Gateway and a Backend Service, along with configurations for deployment and networking.

## Prerequisites
Ensure you have the following installed:
- **Docker** ([Download Here](https://www.docker.com/get-started))
- **Docker Swarm** (Built into Docker)

## Setting Up Docker Swarm
### Step 1: Initialize Docker Swarm
```sh
docker swarm init
```
If you get an error stating the node is already part of a swarm, leave the existing swarm:
```sh
docker swarm leave --force
```
Then reinitialize:
```sh
docker swarm init
```
<img width="1013" alt="image" src="https://github.com/user-attachments/assets/9b464ba1-3556-48a4-a48c-418990af7d5d" />


## Project Structure
```
microservices-docker-swarm/
│── backend-service/
│   ├── backend.py
│   ├── Dockerfile
│
│── api-gateway/
│   ├── api_gateway.py
│   ├── Dockerfile
│
│── docker-compose.yml
│── README.md
```

## Creating Microservices
### **1. Backend Service**
Create `backend.py`:
```python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello from Backend Service"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
```
<img width="527" alt="image" src="https://github.com/user-attachments/assets/bd34a73e-4c75-4c7a-82bc-215ccf7369fa" />

Create `Dockerfile` for Backend:
```Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY backend.py /app
RUN pip install flask
CMD ["python", "backend.py"]
```
<img width="549" alt="image" src="https://github.com/user-attachments/assets/3c12f4b5-345a-4289-9d96-298bf0dcd089" />


### **2. API Gateway**
Create `api_gateway.py`:
```python
from flask import Flask
import requests
app = Flask(__name__)
@app.route('/')
def hello():
    backend_response = requests.get('http://backend-service:5000')
    return f"API Gateway: {backend_response.text}"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
```
<img width="634" alt="image" src="https://github.com/user-attachments/assets/fabf5647-c46b-4c99-838a-04f314579d66" />

Create `Dockerfile` for API Gateway:
```Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY api_gateway.py /app
RUN pip install flask requests
CMD ["python", "api_gateway.py"]
```
<img width="597" alt="image" src="https://github.com/user-attachments/assets/c1a9fb55-c9ba-4d37-adfb-e86379e22a6a" />


## Building Docker Images
Navigate to your project directory and build the images:
```sh
docker build -t backend-service ./backend-service
docker build -t api-gateway ./api-gateway
```
Verify the built images:
```sh
docker images
```
<img width="1147" alt="image" src="https://github.com/user-attachments/assets/e25ffcde-ed62-4574-bf12-521917e85336" />


## Deploying Microservices Using Docker Swarm
### **Step 1: Create `docker-compose.yml`**
Create a `docker-compose.yml` file:
```yaml
version: '3.7'
services:
  backend-service:
    image: backend-service
    deploy:
      replicas: 2
      restart_policy:
        condition: on-failure
    networks:
      - app-network
    ports:
      - "5000:5000"

  api-gateway:
    image: api-gateway
    deploy:
      replicas: 2
      restart_policy:
        condition: on-failure
    networks:
      - app-network
    ports:
      - "8080:8080"
    depends_on:
      - backend-service

networks:
  app-network:
    driver: overlay
```
<img width="711" alt="image" src="https://github.com/user-attachments/assets/5f8e12d7-e129-4d80-8d93-b03fd4e083a9" />


### **Step 2: Deploy Services**
Deploy your services to Docker Swarm:
```sh
docker stack deploy -c docker-compose.yml my_microservices
```
Verify running services:
```sh
docker stack services my_microservices
```
Check running containers:
```sh
docker ps
```
<img width="1145" alt="image" src="https://github.com/user-attachments/assets/8f374c59-3815-4daa-8f7a-62c77a26242a" />


## Accessing the Microservices
Open a browser and go to:
```
http://localhost:8080
```
Expected output:
```
API Gateway: Hello from Backend Service
```

## Scaling the Services
Increase the number of backend service replicas to 5:
```sh
docker service scale my_microservices_backend-service=5
```
Verify the scaled services:
```sh
docker stack services my_microservices
```
<img width="462" alt="image" src="https://github.com/user-attachments/assets/d2ab9f11-f7f5-4c7e-9993-f40e5c102cae" />


## Updating the Services
If you make changes to `backend.py`, rebuild the image:
```sh
docker build -t backend-service ./backend-service
```
Then update the service in Swarm:
```sh
docker service update --image backend-service:latest my_microservices_backend-service
```

## Removing the Stack & Leaving Swarm
To remove the deployed stack:
```sh
docker stack rm my_microservices
```
To leave Docker Swarm:
```sh
docker swarm leave --force
```
<img width="1150" alt="image" src="https://github.com/user-attachments/assets/798c75cd-fe2d-4f22-b53d-b07e99ff5a09" />


## Future Enhancements
- Add more microservices
- Implement CI/CD pipeline
- Improve security with RBAC and network policies

## License
This project is licensed under the MIT License.

