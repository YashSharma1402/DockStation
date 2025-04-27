# 🚢 Evidently AI Sets Sail in Docker: A Voyage into Data Monitoring 🐳📊

## 📌 Introduction

This project is a Dockerized Streamlit application that integrates with **Evidently AI** to monitor machine learning models. It allows you to interactively explore reports, compare performance over time, and visualize key insights — all in a containerized environment.

> **Note:** This guide is for manual setup — no cloning required. You’ll create files and folders step-by-step.

---

## 🗂️ Project Structure
📁 evidently-ai-streamlit
 ├── 📂 projects                # Contains different ML monitoring projects
 │    ├── 📂 project_1
 │    │    ├── 📂 reports       # Stores monitoring reports
 │    │    ├── ...
 │    ├── 📂 project_2
 │    │    ├── 📂 reports
 │    │    ├── ...
 │    ├── ...
 │
 ├── 📂 src                     # Contains Python scripts for UI and utilities
 │    ├── ui.py                 # UI components
 │    ├── utils.py              # Utility functions
 │    ├── ...
 │
 ├── 📂 static                  # Stores static assets (CSS, images, etc.)
 │    ├── style.css             # Custom styling
 │    ├── ...
 │
 ├── 📄 app.py                   # Main Streamlit application
 ├── 📄 Dockerfile               # Defines the Docker image for Streamlit
 ├── 📄 requirements.txt          # Python dependencies
 ├── 📄 README.md                 # Project documentation
2️⃣ Create Dockerfile
Dockerfile
Copy
Edit
# Dockerfile
FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir --break-system-packages -r requirements.txt

COPY . /app/

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

<img width="897" alt="image" src="https://github.com/user-attachments/assets/fb354ba1-ada3-484a-b71d-7b6b5a9f68c2" />

3️⃣ Create requirements.txt
text
Copy
Edit
category_encoders==2.6.0
evidently==0.2.6
jupyter==1.0.0
jupyter_contrib_nbextensions==0.7.0
matplotlib==3.7.0
numpy==1.24.2
pandas==1.5.3
pyarrow==11.0.0
python-box==5.4.1
requests==2.28.2
streamlit==1.19.0
pyyaml==5.1
scikit-learn==1.2.1
scipy==1.10.1
seaborn==0.12.2
altair==4.0

<img width="790" alt="image" src="https://github.com/user-attachments/assets/19ed3342-be6c-445f-b5e2-6ac2a50a7ed6" />

4️⃣ Create app.py
python
Copy
Edit
# app.py
import streamlit as st
import os
from src.ui import display_sidebar_header, select_project, select_period, select_report, display_report

st.set_page_config(layout="wide")
display_sidebar_header()

project = select_project()
if project:
    period = select_period(project)
    if period:
        report = select_report(project, period)
        if report:
            display_report(project, period, report)

            <img width="1097" alt="image" src="https://github.com/user-attachments/assets/64222e90-bb76-468a-9168-b08828f676ab" />

5️⃣ Create Folder Structure and Files
bash
Copy
Edit
mkdir -p src static projects/project_1/reports/2023-12
touch src/ui.py projects/project_1/reports/2023-12/report.html
Add dummy HTML report:
bash
Copy
Edit
echo "<h1>Evidently Report: Sample</h1>" > projects/project_1/reports/2023-12/report.html
6️⃣ Create src/ui.py
python
Copy
Edit
# src/ui.py
import streamlit as st
import os

def display_sidebar_header():
    st.sidebar.title("Evidently Dashboard")
    st.sidebar.markdown("🚢 Monitor ML models with Evidently")

def select_project():
    projects = os.listdir("projects")
    return st.sidebar.selectbox("Select Project", projects) if projects else None

def select_period(project):
    periods = os.listdir(f"projects/{project}/reports")
    return st.sidebar.selectbox("Select Period", periods) if periods else None

def select_report(project, period):
    reports = os.listdir(f"projects/{project}/reports/{period}")
    return st.sidebar.selectbox("Select Report", reports) if reports else None

def display_report(project, period, report):
    file_path = f"projects/{project}/reports/{period}/{report}"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            st.components.v1.html(f.read(), height=800, scrolling=True)
    else:
        st.error("Report not found.")

        <img width="733" alt="image" src="https://github.com/user-attachments/assets/452a5716-7783-4676-a338-25960cbf3569" />

🐳 Run with Docker
🏗️ Build the Docker Image
bash
Copy
Edit
docker build -t evidently-streamlit .

<img width="998" alt="image" src="https://github.com/user-attachments/assets/a9c8c342-eeb3-4a6a-9b09-2892a8d49ae2" />

🚀 Run the Container
bash
Copy
Edit
docker run -p 8501:8501 evidently-streamlit

<img width="997" alt="image" src="https://github.com/user-attachments/assets/ed1dcf3d-dd6f-4798-931d-1ad4e3c5986b" />

🌐 Access the App
Open your browser and visit:

arduino
Copy
Edit
http://localhost:8501
You’ll see a Streamlit dashboard where you can choose projects, periods, and reports to display interactive Evidently AI outputs.

<img width="997" alt="image" src="https://github.com/user-attachments/assets/fd76b80c-7b8c-4ed0-ac5d-0253b9f431de" />


🎯 Next Steps
🔒 Add user authentication

📊 Compare reports across time periods

☁️ Deploy on AWS, GCP, or Azure

🌀 Integrate CI/CD pipelines
