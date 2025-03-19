# 🐬 Setting Up MySQL in a Docker Container with an Initialization Script 🚀

## 📌 Overview
This project demonstrates how to set up a MySQL database inside a Docker container with an **automatic initialization script**. When the container starts, the database and tables will be **automatically created**, and sample data will be inserted.

## 📋 Prerequisites
Before proceeding, ensure you have the following installed:

- ✅ [Docker](https://www.docker.com/get-started) installed and running.
- ✅ Basic knowledge of SQL and Docker.

## 📂 Project Directory Structure
Your project should be structured as follows:

```
mysql-docker-setup/
│── Dockerfile
│── database_students.sql
```

- **Dockerfile** → Defines the container setup.
- **database_students.sql** → SQL script to initialize the database.

---

## 📜 Step 1: Create the SQL Initialization Script
Create a file named `database_students.sql` in your project directory with the following content:

```sql
-- Create a new database
CREATE DATABASE student_db;

-- Use the database
USE student_db;

-- Create a table for storing student data
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);

-- Insert sample data into the table
INSERT INTO students (name, age) VALUES ('Alice', 22), ('Bob', 24);
```

This script ensures that the **student_db** database and the **students** table are created when the MySQL container starts.

---

## 🛠 Step 2: Create the Dockerfile
Next, create a **Dockerfile** inside the `mysql-docker-setup` directory:

```dockerfile
# 🏗 Use the official MySQL image
FROM mysql:latest

# 📂 Copy the initialization script into the MySQL container
COPY database_students.sql /docker-entrypoint-initdb.d/

# 🔥 Expose MySQL port
EXPOSE 3306
```

### 🔍 Explanation:
- ✅ **FROM mysql:latest** → Uses the official MySQL image.
- ✅ **COPY database_students.sql /docker-entrypoint-initdb.d/** → Ensures MySQL runs the script on startup.
- ✅ **EXPOSE 3306** → Opens MySQL's default port.

---

## 🏗 Step 3: Build the Docker Image
Navigate to the project directory and build the Docker image:

```bash
docker build -t mysql-custom .
```
<img width="862" alt="image" src="https://github.com/user-attachments/assets/7c07d7d2-03dc-4bab-841a-5618dce18f51" />


### 💡 Explanation:
- **`-t mysql-custom`** → Tags the image with the name `mysql-custom`.
- The `.` at the end refers to the **current directory** where the Dockerfile is located.

---

## 🚀 Step 4: Run the MySQL Container
Start a new MySQL container from the custom image:

```bash
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=root -d mysql-custom
```
<img width="978" alt="image" src="https://github.com/user-attachments/assets/e45777e3-2a53-490e-a3a3-0ab7bf4c89c7" />


### 🧐 Explanation:
- **`--name mysql-container`** → Names the container `mysql-container`.
- **`-e MYSQL_ROOT_PASSWORD=root`** → Sets the MySQL root password to `root`.
- **`-d`** → Runs the container in detached mode (in the background).
- **`mysql-custom`** → Uses the custom-built image.

---

## 🔍 Step 5: Access the Running MySQL Container
To enter the MySQL container’s shell, run:

```bash
docker exec -it mysql-container bash
```
<img width="976" alt="image" src="https://github.com/user-attachments/assets/69e14891-08b1-413e-847e-9caccc42020a" />


This opens an **interactive terminal session** inside the container.

---

## 💻 Step 6: Connect to MySQL Inside the Container
Once inside the container, log into MySQL:

```bash
mysql -u root -p
```
<img width="664" alt="image" src="https://github.com/user-attachments/assets/8fd038ac-c115-44ef-b4c5-fca6b7b3cfd3" />


🔑 **Enter the password:** `root`

---

## 🏗 Step 7: Verify Database and Tables
After logging into MySQL, check the available databases:

```sql
SHOW DATABASES;
```

🔄 **Switch to the `student_db` database:**

```sql
USE student_db;
```

📊 **Query the `students` table:**

```sql
SELECT * FROM students;
```

If everything is set up correctly, you should see the pre-inserted student records.

---
<img width="783" alt="image" src="https://github.com/user-attachments/assets/a10fb489-7000-42bb-bfc5-32093e865527" />


## 🎯 Stopping and Removing the Container
To **stop** the MySQL container:

```bash
docker stop mysql-container
```

To **remove** the container:

```bash
docker rm mysql-container
```

To **remove the custom Docker image**:

```bash
docker rmi mysql-custom
```

---

## 🎉 Conclusion
🚀 **Congratulations!** You have successfully:
✔ Set up MySQL in a Docker container.
✔ Initialized a database and table with a script.
✔ Connected to the MySQL instance and verified the setup.

### 🔥 Next Steps:
✅ Integrate this MySQL container with your application.
✅ Use **Docker Compose** to manage multiple services.
✅ Deploy this setup to **AWS, GCP, or Azure**.

Happy Coding! 🐳🎨

