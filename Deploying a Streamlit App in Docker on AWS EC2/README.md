Deploying a Streamlit App in Docker on AWS EC2
📌 Overview
This guide provides a step-by-step approach to deploying a Streamlit app inside a Docker container on an AWS EC2 instance with a custom network setup. It covers:

✅ Setting up a VPC, Subnet, Route Table, and Internet Gateway
✅ Launching and configuring an EC2 instance
✅ Installing and configuring Docker
✅ Transferring project files to EC2
✅ Running the Streamlit app inside a Docker container
✅ Managing the Docker container

📖 Table of Contents-
1️⃣ Setting Up a VPC, Subnet, Route Table, and Internet Gateway
2️⃣ Launching and Configuring an EC2 Instance
3️⃣ Connecting to EC2
4️⃣ Setting Permissions for the PEM Key
5️⃣ Installing and Configuring Docker
6️⃣ Copying Project Files to EC2
7️⃣ Building and Running the Docker Container
8️⃣ Accessing the Streamlit App
9️⃣ Managing the Docker Container

1️⃣ Setting Up a VPC, Subnet, Route Table, and Internet Gateway
🔹 Create a New VPC
Go to AWS Console → VPC Dashboard → Create VPC

Name: MyCustomVPC
IPv4 CIDR block: 10.0.0.0/16
<img width="1007" alt="image" src="https://github.com/user-attachments/assets/e82a3659-4d18-4114-ba92-d366d9aa3108" />



🔹 Create a Subnet
Go to VPC Dashboard → Subnets → Create Subnet

Select: MyCustomVPC
Subnet name: MyPublicSubnet
CIDR block: 10.0.1.0/24
Enable Auto-assign Public IPv4
<img width="1006" alt="image" src="https://github.com/user-attachments/assets/f775b36a-751a-4c8b-9408-e69f8df7e0ce" />


🔹 Create an Internet Gateway and Attach to VPC
Name: MyIGW
Attach it to: MyCustomVPC

<img width="1010" alt="image" src="https://github.com/user-attachments/assets/a6fe0bdf-d945-4792-9da2-4ae2a733eb07" />


🔹 Create and Associate a Route Table
Name: MyPublicRouteTable
Destination: 0.0.0.0/0
Target: MyIGW
Associate with: MyPublicSubnet
<img width="1005" alt="image" src="https://github.com/user-attachments/assets/77573ab7-93ed-4bc3-adfc-9821e4cbbdf3" />


2️⃣ Launching and Configuring an EC2 Instance
🔹 Launch an EC2 Instance
Name: Streamlit-EC2
AMI: Amazon Linux 2023
Instance Type: t2.micro (Free Tier)
Key Pair: Select/Create a key pair
Network: MyCustomVPC
Subnet: MyPublicSubnet
Enable Auto-assign Public IP
Security Group: Allow SSH (22), HTTP (80), Streamlit (8501)
<img width="998" alt="image" src="https://github.com/user-attachments/assets/72da1812-8198-4386-94a5-1f7eeb3713a4" />


3️⃣ Connecting to EC2
🔹 Via EC2 Instance Connect
Go to EC2 Dashboard → Select Instance → Click Connect

Choose: EC2 Instance Connect
Click: Connect
<img width="969" alt="image" src="https://github.com/user-attachments/assets/ea694177-44f3-4e4a-8d0b-53f6e8ff9c72" />


4️⃣ Setting Permissions for the PEM Key
mv /path/to/your-key.pem ~/your-work-directory/
chmod 600 your-key.pem
5️⃣ Installing and Configuring Docker
sudo yum update -y
sudo yum install -y docker
sudo systemctl enable docker
sudo systemctl start docker
<img width="821" alt="image" src="https://github.com/user-attachments/assets/c17fa937-8243-472e-ba4b-30bd33ddeb39" />


6️⃣ Copying Project Files to EC2
scp -i your-key.pem app.py Dockerfile requirements.txt mushrooms.csv ec2-user@your-ec2-public-ip:/home/ec2-user/
<img width="889" alt="image" src="https://github.com/user-attachments/assets/4fdbab40-7611-4c9d-8175-ed00ecad25c6" />


7️⃣ Building and Running the Docker Container
🔹 Connect to EC2 and navigate to project directory
cd /home/ec2-user
🔹 Build the Docker image
sudo docker build -t streamlit-app .
<img width="733" alt="image" src="https://github.com/user-attachments/assets/42aca7a6-e9a5-489e-b744-a8639ff6cd0c" />


🔹 Run the container
sudo docker run -d -p 8501:8501 --name streamlit_container streamlit-app
<img width="969" alt="image" src="https://github.com/user-attachments/assets/11f02468-b168-4136-83c9-1f6a0aedfe85" />


8️⃣ Accessing the Streamlit App
🌐 Open your browser and visit:

http://your-ec2-public-ip:8501
<img width="896" alt="image" src="https://github.com/user-attachments/assets/8f4d7fa9-e695-4222-8775-1be4e5d68ba2" />


9️⃣ Managing the Docker Container

🔹 Check running containers

sudo docker ps
🔹 Stop the container

sudo docker stop streamlit_container
🔹 Remove the container

sudo docker rm streamlit_container
🔹 Restart the container

sudo docker start streamlit_container
🎯 Conclusion
This guide helps you deploy a Streamlit app inside a Docker container on AWS EC2 with a custom VPC setup. The deployment ensures scalability, security, and high availability for your application. 🚀🎉

✅ Happy Deploying! 🖥️🐳☁️ steps to do this
