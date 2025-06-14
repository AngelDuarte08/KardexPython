# 🎓 University Kardex System

This is a personal academic project developed in Python for managing student academic records using a Kardex system. The application features a graphical interface built with PyQt6 and is backed by a relational database (SQL dump included). It’s designed for use in a university context but can be adapted for other educational environments.

## 📦 Technologies Used

- Python 3.10.17
- PyQt6 (GUI development)  
- MySQL(relational database)   
- VSCode (IDE)

## 🗂 Project Structure

```bash
├── Views/               # GUI interfaces using PyQt6
├── Models/              # Core logic classes (Student, Course, Kardex, etc.)
├── database/            # Database handler and SQL model interaction
│   ├── model.py         # Executes procedures and SQL queries
├── assets/              # Images or icons used in the GUI
├── kardex.sql           # SQL file for database schema and sample data
├── requirements.txt     # Python dependencies
└── main.py              # Entry point to run the application

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Import the database:
Use your favorite database tool to import the kardex.sql file into your MySQL/MariaDB server.

## Run the aplicaition

```bash
python main.py
```
