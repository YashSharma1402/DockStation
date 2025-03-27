# Titanic Survival Predictor

## Overview
The **Titanic Survival Prediction Model** is a machine learning web application that predicts whether a passenger would have survived the Titanic disaster based on various input features. The project is built using:

- **Python** (for data processing & model training)
- **Scikit-learn** (for machine learning)
- **Pandas & NumPy** (for data handling)
- **Streamlit** (for web-based UI)
- **Docker** (for containerization)

The app is hosted on **Streamlit Cloud**, allowing users to interact with the model in real time.

## 🚀 Live Demo
Access the deployed app at: [Titanic Survival Predictor](https://docknest-jm7n5epjlpfny7jveon7xs.streamlit.app/)

## Project Structure
```
Titanic-Prediction-Model/
│── Dockerfile
│── requirements.txt
│── main.py
│── titanic_model.py
│── titanic_model.pkl
│── README.md
```

### **Description of Files**
- **`main.py`** → Streamlit-based web application for user interaction.
- **`titanic_model.py`** → Script to train and save the Titanic survival prediction model.
- **`titanic_model.pkl`** → Pre-trained Random Forest model.
- **`requirements.txt`** → List of dependencies required to run the application.
- **`Dockerfile`** → Configuration file to containerize the application.

## Model Training (`titanic_model.py`)
The model is trained using **Random Forest Classifier** from scikit-learn on the Titanic dataset.

### **Steps:**
1. Load the Titanic dataset.
2. Preprocess missing values and encode categorical data.
3. Train the Random Forest Model.
4. Save the trained model as `titanic_model.pkl`.

## Streamlit Application (`main.py`)
The Streamlit app provides a clean interface for users to input passenger details and predict survival chances.

### **Features:**
✔ User-friendly UI with enhanced CSS  
✔ Live predictions using the trained model  
✔ Interactive sliders & dropdowns for input selection  

## 🐳 Docker Setup
To containerize the application, a `Dockerfile` is created.

### **Dockerfile**
```dockerfile
# Use Python 3.12 slim as base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy necessary files
COPY requirements.txt requirements.txt
COPY main.py main.py
COPY titanic_model.pkl titanic_model.pkl

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### **Running the Application with Docker**
```bash
# Navigate to the Project Directory
cd Titanic-Prediction-Model

# Build the Docker Image
docker build -t titanic-prediction .

# Run the Docker Container
docker run -p 8501:8501 titanic-prediction
```

Then, open your browser and navigate to:
**[http://localhost:8501](http://localhost:8501)**

## 🌍 Deploying to Streamlit Cloud
### **Steps to Deploy:**
1. **Push your project to GitHub** (Make sure `requirements.txt` is correct!)
2. **Go to [Streamlit Cloud](https://share.streamlit.io)** and log in.
3. **Click "Deploy an App"** and enter your repository URL.
4. **Set up the app:**
   - **Repository:** `https://github.com/YOUR_USERNAME/YOUR_REPO_NAME`
   - **Branch:** `main`
   - **Main file path:** `main.py`
5. Click **"Deploy"** and wait for the setup to complete.

🔹 If you see an **error installing requirements**, check the logs in **"Manage App"**.

## 🔥 Next Steps
✅ Deploy the containerized app on **AWS / GCP / Vercel**  
✅ Enhance UI with **Streamlit widgets & visualizations**  
✅ Improve model accuracy with **feature engineering**  

---
📝 **Author:** Yash  
🔗 **GitHub:** [YOUR_GITHUB_LINK]  
🚀 **Deployed at:** [Titanic Survival Predictor](https://docknest-jm7n5epjlpfny7jveon7xs.streamlit.app/)
