# 🚀 Minikube with Docker on macOS

## 📌 Overview
This guide helps you set up **Minikube** with **Docker** on macOS, enabling a local Kubernetes cluster for development and testing.

---

## 🛠 Prerequisites
Ensure you have the following installed:

1. **Docker Desktop** 🐳  
   - [Download & Install Docker](https://www.docker.com/products/docker-desktop)
   - Ensure Docker is **running** before proceeding.

2. **Minikube** 📦  
   Install using Homebrew:
   ```sh
   brew install minikube
   ```
   <img width="1230" alt="image" src="https://github.com/user-attachments/assets/fbb0a540-e1af-4d56-8331-d70874ccf820" />


3. **kubectl (Kubernetes CLI)** 🖥  
   Install using Homebrew:
   ```sh
   brew install kubectl
   ```
   Verify installation:
   ```sh
   kubectl version --client
   ```

---
<img width="841" alt="image" src="https://github.com/user-attachments/assets/a1a4c54f-e7b6-4b74-bc6a-be14c3b30978" />


## ✅ Step 1: Start Minikube with Docker Driver

Start Minikube using **Docker** as the driver:
```sh
minikube start --driver=docker
```

Check the Minikube status:
```sh
minikube status
```

---
<img width="814" alt="image" src="https://github.com/user-attachments/assets/f22de742-fa2d-411a-aa03-604121f55b35" />


## ✅ Step 2: Deploy an Application (Nginx)

### 1️⃣ Create an Nginx Deployment
```sh
kubectl create deployment nginx --image=nginx
```

### 2️⃣ Expose the Deployment (Make It Accessible)
```sh
kubectl expose deployment nginx --type=NodePort --port=80
```

### 3️⃣ Get the Service URL
```sh
minikube service nginx --url
```
Open the provided URL in your **browser** to view the running **Nginx** server.

---
<img width="682" alt="image" src="https://github.com/user-attachments/assets/3f6f4f1b-824a-43e4-8033-bbc580350e79" />

<img width="1470" alt="image" src="https://github.com/user-attachments/assets/25764e1f-6f93-4f8b-ab04-ee2d5a09767d" />


## ✅ Step 3: Managing Kubernetes Cluster

### 1️⃣ Check Running Pods
```sh
kubectl get pods
```

### 2️⃣ Scale the Deployment (Increase Replicas)
```sh
kubectl scale deployment nginx --replicas=3
```
Verify the pods:
```sh
kubectl get pods
```

### 3️⃣ Delete the Deployment & Service
```sh
kubectl delete service nginx
kubectl delete deployment nginx
```

---
<img width="676" alt="image" src="https://github.com/user-attachments/assets/a4db14cf-7fae-4d8e-aef0-42e26fba8a0f" />


## ✅ Step 4: Stop & Delete Minikube

### 1️⃣ Stop Minikube
```sh
minikube stop
```

### 2️⃣ Delete the Cluster
```sh
minikube delete
```

This removes all Kubernetes resources and stops Minikube.

---
<img width="737" alt="image" src="https://github.com/user-attachments/assets/612f1a75-e948-4e24-9711-1cc862727456" />


## 🎯 Conclusion
✅ Successfully set up **Minikube with Docker** on macOS!  
✅ Deploy, manage, and scale containerized applications locally.  
✅ A simple way to experiment with Kubernetes in a local development environment.

🚀 Now you’re ready to explore Kubernetes on your Mac! 🎉

