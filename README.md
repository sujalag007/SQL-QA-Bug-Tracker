# SQL-Based QA Bug & Task Tracking Database

A lightweight, efficient relational database application built with Python and SQLite. This tool is designed to manage the lifecycle of software bugs and test cases, demonstrating core DBMS concepts and automated reporting logic.

## 🎯 Project Overview
In a professional QA environment, tracking system-level bugs and test execution states is critical. This project implements a relational schema to store, update, and query bug logs using raw SQL integrated into a Python automation script.

## 🛠️ Technical Features
* **Relational Schema:** Designed with structured tables using Primary Keys and data types to ensure referential integrity.
* **SQL Implementation:** Utilizes standard SQL queries including `CREATE`, `INSERT`, and `SELECT` to manage the bug lifecycle.
* **Python Integration:** Uses the `sqlite3` library to bridge high-level automation logic with a persistent data layer.
* **QA Focus:** Built specifically to track bug priority, status (Open/Closed), and descriptions for system-level testing.

## 📊 Core Concepts Covered
* **DBMS Fundamentals:** ER Modeling, Relational Algebra, and ACID properties.
* **Data Persistence:** Moving beyond volatile memory to local disk-based storage.
* **Automation:** Programmatic interaction with databases, a core skill for QA Tools Engineering.

## 🚀 How to Run
1. Ensure you have Python installed.
2. Run the tracker:
   ```bash
   python3 bug_tracker.py
