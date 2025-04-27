
# 🚀 Streamlit Spiral Visualization App with Docker


Welcome to the **Streamlit Spiral Visualization App!** This project is a simple and interactive Python application built with **Streamlit** to visualize a **dynamic spiral.** You can customize the spiral’s characteristics using sliders and see real-time changes.

The app is **Dockerized** for easy deployment and environment consistency.

---
![Uploading image.png…]()


## 🌟 Features

✅ **Interactive Controls** – Adjust the number of points and turns in the spiral.  
✅ **Real-time Visualization** – Watch the spiral dynamically change.  
✅ **Dockerized Application** – Run seamlessly across different environments.  
✅ **Lightweight & Easy to Use** – No extra dependencies, just Python & Streamlit.  

---

## 🚀 Technologies Used

- **Python 3** – Core programming language
- **Streamlit** – Web framework for interactive UI
- **Altair** – Data visualization library for the spiral graph
- **Pandas** – Data manipulation and handling
- **Docker** – Containerization for easy deployment

---

## ⚙ Prerequisites

Before running the application, make sure you have:

- **Docker** installed ([Install Docker](https://docs.docker.com/get-docker/))
- **Git** installed ([Install Git](https://git-scm.com/downloads))

---

## 🛠 Getting Started

### **Step 1: Clone the Repository**


### **Step 2: Install Dependencies (Optional for Local Execution)**
If you’re running locally without Docker, install the required packages:
```bash
pip install -r requirements.txt
```

### **Step 3: Build the Docker Image**
```bash
docker build -t streamlit-app .
```
After building, verify the image with:
```bash
docker images
```
<img width="1148" alt="image" src="https://github.com/user-attachments/assets/9f9fc2cd-f951-4129-aa49-7be7cddb4fc3" />


### **Step 4: Run the Docker Container**
```bash
docker run -p 8501:8501 streamlit-app
```

<img width="779" alt="image" src="https://github.com/user-attachments/assets/9570d4e0-ac92-47b8-93f4-4b7c9c934c79" />


### **Step 5: Access the Application**
Once the container is running, open your browser and visit:
**[http://localhost:8501](http://localhost:8501)**

---

## 🌀 How the App Works

- **Sliders for Customization:**
  - **Number of Points in Spiral** – Controls the number of points that form the spiral.
  - **Number of Turns in Spiral** – Adjusts how many full turns the spiral makes.
- **Real-Time Visualization:**
  - The spiral updates instantly when you move the sliders.
- **Under the Hood:**
  - The app generates spiral points using **polar coordinates**.
  - The x and y positions are calculated using **cosine and sine functions**.
  - **Altair charts** visualize the spiral in Streamlit.

---

## 📜 Code Overview

### **Python Code (`app.py`)**

<img width="972" alt="image" src="https://github.com/user-attachments/assets/d151adcf-6a24-475a-b9c5-af0177f53935" />


## 🐳 Dockerfile


<img width="965" alt="image" src="https://github.com/user-attachments/assets/fcc94e7b-9691-440c-a557-0fa10beb7497" />



## 🛠 Troubleshooting

🛑 **Issue: "Streamlit command not found" inside Docker?**  
✔ Fix: Make sure dependencies are installed inside the container by rebuilding it:  
```bash
docker build --no-cache -t streamlit-app .
```

🛑 **Issue: Port 8501 is already in use?**  
✔ Fix: Run on a different port:  
```bash
docker run -p 8502:8501 streamlit-app
```
Then, visit **http://localhost:8502**

---

## 🤝 Contributing

🚀 Want to contribute? Here’s how:
1. **Fork** the repository
2. **Create a branch** (`git checkout -b feature-branch`)
3. **Commit your changes** (`git commit -m "Added feature XYZ"`)
4. **Push to the branch** (`git push origin feature-branch`)
5. **Submit a Pull Request**

---

## 📜 License
This project is open-source.**.

💡 **Happy Coding! 🚀🎉**






