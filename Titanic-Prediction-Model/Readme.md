🚢 Titanic Survival Predictor: Containerized Streamlit App
📌 Overview
The Titanic Survival Prediction Model is a machine learning application that predicts whether a passenger would have survived the Titanic disaster based on various input features.
It is built using Python, scikit-learn, pandas, and Streamlit for a user-friendly web interface.
To ensure seamless deployment and portability, Docker is used to containerize the application.

📂 Project Structure
css
Copy
Edit
Titanic-Prediction-Model/
├── Dockerfile
├── requirements.txt
├── main.py
├── titanic_model.py
└── titanic_model.pkl
📜 Description of Files

File	Description
main.py	Streamlit-based web application for user interaction
titanic_model.py	Script to train and save the Titanic survival model
titanic_model.pkl	Serialized Random Forest model for predictions
requirements.txt	Required Python libraries
Dockerfile	Docker configuration for containerizing the application
🤖 Model Training (titanic_model.py)
The model is trained using a Random Forest Classifier from scikit-learn, based on Titanic dataset features.
After training, the model is saved as titanic_model.pkl using joblib for efficient storage and fast loading.

Steps in titanic_model.py:

Load the Titanic dataset

Preprocess missing values and encode categorical features

Train the Random Forest model

Save the trained model as titanic_model.pkl

<img width="625" alt="image" src="https://github.com/user-attachments/assets/5f90c1e1-6f7a-42ce-865a-1bd39c0464e2" />
<img width="833" alt="image" src="https://github.com/user-attachments/assets/d2c15410-db4d-43ad-acb6-0d1231f4b684" />



🎨 Streamlit Application (main.py)
The Streamlit app provides a clean and interactive interface for users to input passenger details and predict survival chances in real-time.

✨ Features
✔️ User-friendly UI with enhanced design

✔️ Real-time survival prediction updates

✔️ Interactive sliders and dropdowns for input selection

✔️ Dark mode compatible

<img width="583" alt="image" src="https://github.com/user-attachments/assets/c495686e-0e91-4c7c-946d-ad081086817e" />
<img width="653" alt="image" src="https://github.com/user-attachments/assets/a0fe6ef2-1d7d-4a2b-a87b-e37eb946efc5" />



🐳 Docker Setup
To containerize the application, a Dockerfile is provided.

📄 Dockerfile Overview:
Dockerfile
Copy
Edit
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

<img width="630" alt="image" src="https://github.com/user-attachments/assets/334b0717-9b68-49d1-9b63-8e86a306a5c5" />
<img width="804" alt="image" src="https://github.com/user-attachments/assets/739d669e-d632-4dbc-9bee-3c216e8b550c" />


# Run the Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
🚀 Running the Application with Docker
Follow these steps to build and run the Dockerized application:

1️⃣ Navigate to the Project Directory
bash
Copy
Edit
cd Titanic-Prediction-Model
2️⃣ Build the Docker Image
bash
Copy
Edit
docker build -t titanic-prediction .
3️⃣ Run the Docker Container
bash
Copy
Edit
docker run -p 8501:8501 titanic-prediction
4️⃣ Access the Application
Open your browser and navigate to:

<img width="1103" alt="image" src="https://github.com/user-attachments/assets/fb569603-7f01-475f-898c-b6fc05e3d315" />
<img width="1090" alt="image" src="https://github.com/user-attachments/assets/868fb6e6-ecf7-4cfe-b25c-aa8281fd8c9d" />



👉 http://localhost:8502
<img width="1381" alt="image" src="https://github.com/user-attachments/assets/a110fb8c-d11d-4537-9caa-727481ae023c" />


🎯 Conclusion
This project demonstrates the deployment of a Machine Learning model using Streamlit and Docker.
The model predicts Titanic survival outcomes based on user inputs, and the Dockerized environment ensures portability, consistency, and easy deployment across any platform.

🔥 Next Steps
🚀 Deploy the containerized app to AWS, GCP, or Vercel

🎨 Enhance the UI with advanced Streamlit widgets & custom visualizations

🧠 Improve model accuracy with more feature engineering

⚡ Add monitoring and logging for production deployments

⚡ Happy Coding & Containerizing! 🐳🚢
