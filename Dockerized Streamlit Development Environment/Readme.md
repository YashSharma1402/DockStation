Dockerized Streamlit Development Environment
This guide helps you set up a Streamlit application inside a Docker container for an efficient and portable development experience. 🚀

Prerequisites
Before setting up the environment, ensure you have the following installed on your machine:

🔹 Docker (Ensure the Docker daemon is running)
🔹 Python 3.9+ (Check installation with python --version)
🔹 pip (Ensure it's up to date with pip --version)
🔹 Basic knowledge of Streamlit

Directory Structure
project_root/
│── .streamlit/
│   └── config.toml
│── src/
│   └── main.py
│── Dockerfile
│── requirements.txt
│── README.md
<img width="278" alt="image" src="https://github.com/user-attachments/assets/eac6fb8d-8460-45c5-b058-f53e57bf80ed" />


File Explanations
1️ .streamlit/config.toml
This file configures Streamlit settings for local development.

[server]
headless = true
runOnSave = true
fileWatcherType = "poll"
2️ src/main.py
This file contains the core logic of the Streamlit application, including:

🏠 Home Page → Introduction to the app.
📊 Data Explorer → Allows users to upload and inspect CSV files.
📈 Visualization Page → Generates interactive charts and graphs.

3️ Dockerfile
Defines the containerized environment for Streamlit.

# Use a lightweight Python image
FROM python:3.9-slim  

# Set working directory
WORKDIR /app  

# Copy dependencies and install them
COPY requirements.txt /app/  
RUN pip install --no-cache-dir -r requirements.txt  

# Copy all project files
COPY . /app/  

# Expose Streamlit’s default port
EXPOSE 8501  

# Run the Streamlit app
CMD ["streamlit", "run", "src/main.py", "--server.port=8501", "--server.address=0.0.0.0"]

<img width="683" alt="image" src="https://github.com/user-attachments/assets/f70b426a-68f7-4342-80d9-b4ec26c81603" />

4️ requirements.txt
Contains necessary dependencies:

streamlit
pandas
numpy
matplotlib
plotly

<img width="845" alt="image" src="https://github.com/user-attachments/assets/22e0e96a-a862-4eee-9420-a7a4d848963b" />

⚡ Steps to Run the Project
1️ Navigate to the project directory
cd path/to/project_root
2️ Build the Docker image
docker build -t streamlit-app .

<img width="1120" alt="image" src="https://github.com/user-attachments/assets/d9d6a058-0cfa-4181-bf78-7387db1afbb5" />

3️ Run the container
docker run -p 8501:8501 streamlit-app
<img width="921" alt="image" src="https://github.com/user-attachments/assets/b64b4083-1c35-46b0-90e8-bedaffe28191" />


4️ Open in Browser
🌐 Go to → http://localhost:8501

<img width="1213" alt="image" src="https://github.com/user-attachments/assets/ca3f231e-6fc3-4654-80e7-5dd0e7c29192" />
<img width="1470" alt="image" src="https://github.com/user-attachments/assets/0c7158c8-21f4-4bcc-98e5-fad8f78deb01" />
<img width="1470" alt="image" src="https://github.com/user-attachments/assets/431673ea-4085-4180-b167-be2de20714ca" />
<img width="1470" alt="image" src="https://github.com/user-attachments/assets/a0eda01c-208e-4b50-9c63-b190e9105236" />


Conclusion
You now have a fully functional Streamlit environment running inside Docker! 🚀

Screenshot 2025-03-19 144538 Screenshot 2025-03-19 144550 Screenshot 2025-03-19 144602

💡 Next Steps:
🔹 Add more features to your Streamlit app.
🔹 Deploy the containerized app on AWS, GCP, or Azure.
🔹 Experiment with Docker Compose for multi-container applications.

🚀 Happy Coding! 🐳💙
