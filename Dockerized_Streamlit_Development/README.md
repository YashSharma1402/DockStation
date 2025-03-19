🚀 Dockerized Streamlit Development Environment
This guide helps you set up a Streamlit application inside a Docker container for an efficient and portable development experience. 🐳

✅ Prerequisites
Ensure you have the following installed on your machine:

🔹 Docker 🐳 (Ensure the Docker daemon is running)
🔹 Python 3.9+ 🐍 (Check installation with python --version)
🔹 pip 📦 (Ensure it's up to date with pip --version)
🔹 Basic knowledge of Streamlit 📊
📂 Project Structure
bash
Copy code
Dockerized_Streamlit_Development/
│── .streamlit/
│   └── config.toml          # Streamlit configuration file
│── src/
│   └── main.py              # Streamlit app entry point
│── .gitignore               # Ignore unnecessary files in Git
│── Dockerfile               # Docker setup
│── README.md                # Project documentation
│── requirements.txt         # Python dependencies
📜 File Explanations
1️⃣ .streamlit/config.toml
Configures Streamlit settings for local development:

ini
Copy code
[server]
headless = true
runOnSave = true
fileWatcherType = "poll"
2️⃣ src/main.py
This file contains the core logic of the Streamlit application, including:
🏠 Home Page → Introduction to the app.
📊 Data Explorer → Upload and inspect CSV files.
📈 Visualization Page → Generates interactive charts.

Example Code:

python
Copy code
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🚀 Streamlit Dockerized App")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    fig = px.histogram(df, x=df.columns[0])
    st.plotly_chart(fig)
3️⃣ Dockerfile
Defines the containerized environment for Streamlit.

dockerfile
Copy code
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
4️⃣ requirements.txt
Contains necessary dependencies:

txt
Copy code
streamlit
pandas
numpy
matplotlib
plotly
⚡ How to Run the Project
1️⃣ Navigate to the Project Directory
bash
Copy code
cd path/to/Dockerized_Streamlit_Development
2️⃣ Build the Docker Image
bash
Copy code
docker build -t streamlit-app .
3️⃣ Run the Container
bash
Copy code
docker run -p 8501:8501 streamlit-app
4️⃣ Open in Browser
🌐 Go to: http://localhost:8501

🎯 Conclusion
You now have a fully functional Streamlit environment running inside Docker! 🚀
<img width="1045" alt="image" src="https://github.com/user-attachments/assets/eeb84179-9c5c-4698-aa24-0bd80ea6123a" />
<img width="986" alt="image" src="https://github.com/user-attachments/assets/f04c217d-bc77-4893-b918-de275b692595" />



💡 Next Steps
🔹 Add more features to your Streamlit app.
🔹 Deploy the containerized app on AWS, GCP, or Azure.
🔹 Experiment with Docker Compose for multi-container applications.

🚀 Happy Coding! 🐳💙

