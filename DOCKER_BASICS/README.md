# 🐳 DOCKER BASICS: Hello World

Welcome to **Docker Basics**! 🚀 This project provides a simple introduction to Docker by creating and running a basic **Python Hello World application** inside a container.

## 📌 Project Overview
This project demonstrates:
- How to create a simple Python application
- Writing a **Dockerfile** to containerize the application
- Building and running a Docker container
- Pushing the project to a **GitHub repository**

---

## 📂 Project Structure
```
DockerStation/
│-- DOCKER_BASICS/
│   │-- app.py          # Python script to print "Hello, World!"
│   │-- Dockerfile      # Docker configuration file
│   │-- .gitignore      # Ignore unnecessary files
│-- README.md          # Project documentation
```

---

## 📖 Prerequisites
Before running this project, ensure you have the following installed:

🔹 **Docker** → [Download Docker](https://www.docker.com/get-started)  
🔹 **Python (Optional)** → [Download Python](https://www.python.org/downloads/)  
🔹 **Git (Optional)** → [Download Git](https://git-scm.com/downloads)  

You can check if Docker is installed by running:
```sh
docker --version
```
If installed, it will return something like:
```
Docker version 24.0.5, build 123abc
```

---

## 🚀 Setting Up the Project

### 1️⃣ **Clone the Repository**
Run the following command to clone the repository:
```sh
git clone https://github.com/YashSharma1402/DockStation.git
cd DockStation/DOCKER_BASICS
```

### 2️⃣ **Create the Python Application**
Inside the `DOCKER_BASICS/` directory, create a file `app.py`:
```python
print("Hello, World!")
```

### 3️⃣ **Create a Dockerfile**
Create a file named `Dockerfile` (without any extension) in the same directory:
```Dockerfile
# Use the official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the local directory to the container
COPY . .

# Define the default command to run the Python script
CMD ["python", "app.py"]
```

---

## 🛠 Running the Dockerized Application

### 1️⃣ **Build the Docker Image**
Run the following command to build a Docker image:
```sh
docker build -t myapp .
```
<img width="751" alt="image" src="https://github.com/user-attachments/assets/90ba0297-6a6c-4ef9-9404-01aa02096602" />


### 2️⃣ **Verify the Image**
To check if the image was created successfully, run:
```sh
docker images
```
<img width="703" alt="image" src="https://github.com/user-attachments/assets/279b127b-184c-461b-a367-7969b312e32d" />

You should see an image named `myapp` in the list.

### 3️⃣ **Run the Docker Container**
Execute the container to print "Hello, World!":
```sh
docker run myapp
```
<img width="577" alt="image" src="https://github.com/user-attachments/assets/8af93457-d3ba-419d-ba85-9c10b10c960c" />

You should see the output:
```
Hello, World!
```

---

## 📤 Pushing the Project to GitHub
If you have modified the project, follow these steps to push your changes:

### 1️⃣ **Initialize Git and Add Remote Repository**
```sh
git init
git remote add origin https://github.com/YashSharma1402/DockStation.git
```
<img width="756" alt="image" src="https://github.com/user-attachments/assets/ce8c06b6-f2f8-436a-8054-d9bd2b61d6c4" />


### 2️⃣ **Commit and Push Changes**
```sh
git add .
git commit -m "Initial commit - Dockerized Hello World app"
git push -u origin main
```
<img width="614" alt="image" src="https://github.com/user-attachments/assets/56a62bc1-af9b-4db7-b783-c4424ca2e4d6" />
<img width="721" alt="image" src="https://github.com/user-attachments/assets/94b0be59-6e1b-4d85-a997-0cd718130a6d" />


---

## 🎯 Next Steps
Now that you’ve run a basic Docker container, here are some next steps:
✅ Learn about **Docker volumes** and **networking**  
✅ Use **Docker Compose** for multi-container applications  
✅ Deploy the application to **Docker Hub** or **Kubernetes**  

---

## 📚 Resources
🔹 **Official Docker Documentation** → [Docker Docs](https://docs.docker.com/)  
🔹 **Dockerfile Best Practices** → [Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)  
🔹 **GitHub Repo** → [DockStation](https://github.com/YashSharma1402/DockStation)  

---

🚀 **Happy Docking!** ⚓🐳

