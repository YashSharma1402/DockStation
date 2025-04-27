Python Logging Application with Docker
This project demonstrates how to create a Python application that logs data continuously to a file while running inside a Docker container. The logs are stored persistently in a Docker volume to ensure they remain available even if the container is stopped or removed.

Project Structure
.
├── app.py            # Python application that generates logs
├── Dockerfile        # Dockerfile to build the image
└── README.md         # Project documentation
📥 Prerequisites
Before starting, make sure you have Docker installed on your system.

Download Docker
Steps to Build and Run the Application
Step 1: Write the Python Application
Create a file named app.py with the following content:

<img width="670" alt="image" src="https://github.com/user-attachments/assets/f4c1d7c1-2b23-4e07-87a9-2fd07be6dcda" />
<img width="756" alt="image" src="https://github.com/user-attachments/assets/d5616521-481d-4168-8898-0b17f63e6732" />



Step 2: Create a Dockerfile
Create a file named Dockerfile with the following content:
CMD ["python", "app.py"]

<img width="691" alt="image" src="https://github.com/user-attachments/assets/f5998ee9-5502-4b05-8e13-39e0c353a3d9" />
<img width="520" alt="image" src="https://github.com/user-attachments/assets/03e78ef4-e309-4619-84ec-a4cd10266cfc" />


Step 3: Build the Docker Image
Run the following command to build the Docker image:

docker build -t python-logger .

<img width="1147" alt="image" src="https://github.com/user-attachments/assets/53953eb4-4281-4a63-a2d0-16295d18d92a" />


Step 4: Run the Docker Container with a Volume
To ensure logs are persisted, mount a Docker volume and run the container:

docker volume create my-app-data
docker run -d --name logger -v log-data:/data python-logger
Explanation:

-d: Runs the container in detached mode.
-v my-app-data:/data: Mounts the volume my-app-data to the /data directory inside the container.

<img width="959" alt="image" src="https://github.com/user-attachments/assets/2c85f8eb-7b70-4852-948f-74a041fd88ff" />

Step 5: Verify Logs
Check if the container is running:

docker ps
image

View logs from the container:
<img width="1131" alt="image" src="https://github.com/user-attachments/assets/05cd632c-0906-4d3d-8af8-895338bc097f" />


docker logs <container_id/name>
<img width="1051" alt="image" src="https://github.com/user-attachments/assets/97bf4b2f-4e38-47d5-915a-c7ab2af503ec" />


Access the log file inside the container:



Inspect the volume on the host system:

docker volume inspect my-app-data
<img width="801" alt="image" src="https://github.com/user-attachments/assets/0a4e134a-dfa4-4988-ae32-f14ad6fa921a" />


Stopping and Cleaning Up
Stop the container:

docker stop python-log-container


Remove the container:

docker rm python-log-container


Remove the image (if needed):

docker rmi python-log-app
Remove the volume (if needed):

docker volume rm my-app-data

<img width="936" alt="image" src="https://github.com/user-attachments/assets/9c3c4f91-64ae-46c9-a20d-26dedfa6f2ea" />


Notes
The logs are stored persistently in the Docker volume my-app-data.
You can use docker volume inspect my-app-data to locate and analyze the logs on the host system. Happy Logging with Docker!
