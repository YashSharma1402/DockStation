Docker Bridge Networking Isolation Experiment

📌 Overview

This experiment demonstrates how Docker Bridge Networking works by creating custom bridge networks, running containers within them, and testing network connectivity and isolation. This setup is crucial for securing microservices and containerized applications.

🚀 Objectives

Understand Docker Bridge Networking

Create and manage custom bridge networks

Test container communication within a network

Demonstrate network isolation

Expose a container to the host network

🌐 Understanding Docker Bridge Networking

Docker uses different networking modes, and bridge networks are the most common.

🔹 Key Features of Bridge Networking

Containers communicate using container names instead of IPs.

Network isolation is maintained between different bridge networks.

Custom bridge networks offer more control over inter-container communication.

External access can be enabled via port forwarding.

🔧 Setup & Execution

Follow these steps to set up and test Docker bridge networking on your machine.

📌 Step 1: Verify Docker Installation

Ensure Docker is installed and running:

docker --version

If not installed, download Docker from Docker Official Website.

📌 Step 2: Create a Custom Bridge Network

Run the following command to create a custom bridge network:

docker network create --driver bridge my_custom_bridge

Verify that the network was created:

docker network ls

You should see my_custom_bridge in the list.
<img width="751" alt="image" src="https://github.com/user-attachments/assets/e904180e-3b32-41bd-ba06-de4cd32e1554" />


📌 Step 3: Run Containers Inside the Custom Bridge Network

Start two containers in the my_custom_bridge network:

docker run -d --name container1 --network my_custom_bridge nginx
docker run -d --name container2 --network my_custom_bridge alpine sleep 3600

nginx: Runs a web server.

alpine sleep 3600: Runs a lightweight container to keep it active.
<img width="850" alt="image" src="https://github.com/user-attachments/assets/109b4016-203c-4be2-803c-fe3705ff64b9" />


📌 Step 4: Verify Network Connectivity

Inspect the network and check container IPs:

docker network inspect my_custom_bridge

Test connectivity between containers:

docker exec -it container2 ping -c 4 container1

If ping is missing inside container2, install it:

docker exec -it container2 sh
apk add iputils
ping -c 4 container1
exit
<img width="959" alt="image" src="https://github.com/user-attachments/assets/c9b07fb1-c150-44ae-9abf-dcb6530a60d7" />
<img width="894" alt="image" src="https://github.com/user-attachments/assets/0f021499-0c5a-4460-8941-8b8a863c836b" />



📌 Step 5: Demonstrate Network Isolation

Create two separate bridge networks:

docker network create --driver bridge bridge_network_A
docker network create --driver bridge bridge_network_B

Run containers in different networks:

docker run -d --name container_A --network bridge_network_A alpine sleep 3600
docker run -d --name container_B --network bridge_network_B alpine sleep 3600

Test isolation by trying to ping container_B from container_A:

docker exec -it container_A ping -c 4 container_B

🚨 Expected Result: The ping should fail, proving network isolation.
<img width="952" alt="image" src="https://github.com/user-attachments/assets/0c2b2bc3-68a6-4697-b6c6-c3372743c667" />
<img width="860" alt="image" src="https://github.com/user-attachments/assets/191e562b-2330-4291-8056-92f0e34bb925" />



📌 Step 6: Restrict Container Communication

Run a container without network access:

docker run -d --name isolated_container --network none nginx

Verify that it has no IP assigned:

docker inspect isolated_container
<img width="1154" alt="image" src="https://github.com/user-attachments/assets/026442e9-c6d6-4d8e-99f3-3ae08c548c6b" />


📌 Step 7: Connect a Container to Multiple Networks

A container can be part of multiple networks for controlled communication:

docker network connect bridge_network_A container1

Now container1 can communicate with containers in both my_custom_bridge and bridge_network_A.
<img width="745" alt="image" src="https://github.com/user-attachments/assets/4f3b502f-57d9-4071-8270-73986abcd8a9" />


📌 Step 8: Expose a Container to the Host Network

Run an Nginx web server and expose it to the host machine:

docker run -d -p 8080:80 --name webserver nginx

Access it from your browser at:
👉 http://localhost:8080

🛠 Managing and Cleaning Up Networks

📌 List available networks:

docker network ls

📌 Inspect a network:

docker network inspect my_custom_bridge

📌 Remove a specific network:

docker network rm my_custom_bridge

📌 Clean up unused networks and stopped containers:

docker system prune -f

🏆 Conclusion

✔ Created a custom bridge network✔ Connected containers within the same network✔ Demonstrated network isolation✔ Restricted a container’s network access✔ Connected a container to multiple networks✔ Exposed a container to the host machine

Now you have a solid understanding of Docker Bridge Networking! 🚀 Let me know if you have any questions. 🎯
