# 🎓 College Database Project (Version 2.1)
![MySQL](https://img.shields.io/badge/Database-MySQL-blue)
![Status](https://img.shields.io/badge/Version-2.1-success)
![Workbench](https://img.shields.io/badge/Workbench-Compatible-orange)

---

## 🧭 Table of Contents
- [📘 Overview](#-overview)
- [🗂️ Key Features (v21)](#️-key-features-v21)
- [🧱 Entities and Relationships](#-entities-and-relationships)
- [🧮 Sample Data (v21)](#-sample-data-v21)
- [👀 Views (v21)](#-views-v21)
- [🧩 Files Included](#-files-included)
- [🚀 Getting Started](#-getting-started)
- [👨‍💻 Contributors](#-contributors)
- [🏁 License](#-license)

---

## 📘 Overview

**Version 2.1** is a build-up on [Version 1](https://github.com/yourusername/college_database_v1) of the College Database Project.  
This enhanced version improves upon the original design with:

- ✔️ Expanded **sample data** for testing and demonstration  
- ✔️ Introduced **views** for simplified reporting and analysis  
- ✔️ Improved **relational design** for more advanced queries and better normalization  

This project defines a **relational database schema** for managing a college’s academic and administrative system using **MySQL**.  
It is fully compatible with **MySQL Workbench** and includes all **DDL (schema)** and **DML (data)** scripts for easy setup, learning, and experimentation.

---

## 🗂️ Key Features (v2.1)

| Feature | Description |
|----------|-------------|
| ✅ Expanded sample data | 20+ example records for students, faculty, and staff |
| ✅ Academic structure | Departments, semesters, rooms, and courses fully populated |
| ✅ Relationships | Faculty advising students, students enrolled in courses |
| ✅ Views added | Simplified reporting for students, faculty, and courses |
| ✅ Workbench support | All schemas viewable via `.mwb` file in MySQL Workbench |

---

## 🧱 Entities and Relationships

### 📌 Main Tables

| Table | Description |
|--------|-------------|
| **people** | All individuals (students, faculty, staff) and their personal information |
| **department** | Academic departments (e.g., CS, Math, History) |
| **semester** | Academic terms (Fall, Spring, Summer) |
| **room** | Building and room data including capacity |
| **faculty** | Faculty details, office locations, and department links |
| **student** | Student-specific info including GPA and advisors |
| **course** | Master list of courses offered |
| **course_offering** | Course sections per semester |
| **enrollment** | Enrollment and grades for each student in a course section |
| **letter_grade** | Standard grading scale (A–F, I, W) |
| **staff** | Non-teaching personnel and their assigned roles |

---

## 🧮 Sample Data (v2.1)

Version 2 includes a **sample dataset** (`sample_data_query.sql`) with realistic entries for testing and practice.

Included sample records:

- 🏫 10 departments  
- 📅 3 semesters  
- 🏢 5 rooms  
- 👥 20 people  
- 👨‍🏫 5 faculty members  
- 🎓 10 students  
- 📚 10 courses  
- 🧾 6 course offerings  
- 🅰️ 11 letter grades  
- 📝 10 enrollments  
- 🧑‍💼 5 staff members  

---

## 👀 Views (v2.1)

To support analysis and simplify frequent queries, the following 7 **views** were added:

| # | View Name | Description |
|---|------------|-------------|
| 1️⃣ | **people_summary** | Displays general information for all individuals |
| 2️⃣ | **faculty_summary** | Lists faculty names, departments, and office locations |
| 3️⃣ | **student_summary** | Shows students, GPA, and their assigned advisors |
| 4️⃣ | **staff_summary** | Displays staff roles with their departments |
| 5️⃣ | **course_summary** | Shows all courses with department names |
| 6️⃣ | **course_offering_summary** | Lists course sections with instructor, room, and semester |
| 7️⃣ | **enrollment_summary** | Combines students, courses, grades, and instructors |


### 🧩 Example: `student_summary`

```sql
CREATE OR REPLACE VIEW student_summary AS
SELECT 
    s.student_id,
    p.first_name AS student_first_name,
    p.last_name AS student_last_name,
    s.cumulative_gpa,
    f.faculty_id AS advisor_id,
    pf.first_name AS advisor_first_name,
    pf.last_name AS advisor_last_name
FROM student s
JOIN people p ON s.people_id = p.people_id
LEFT JOIN faculty f ON s.advisor_id = f.faculty_id
LEFT JOIN people pf ON f.people_id = pf.people_id;
```


## 🧩 Files Included

| File Name | Purpose |
|------------|----------|
| `schema.sql` | Creates the complete database schema |
| `sample_data_query.sql` | Inserts all sample data |
| `views.sql` | Contains all view creation statements |
| `college_database_v2.1.mwb` | MySQL Workbench EER diagram |
| `README.md` | Project documentation (this file) |


## 🚀 Getting Started

1. Open MySQL Workbench

Launch MySQL Workbench on your local machine.

2. Create the database

```sql
CREATE DATABASE af25willa1_college_db;
USE af25willa1_college_db;
```

3. Run the scripts in order:
	a.	schema.sql – Defines tables and relationships
	b.	sample_data_query.sql – Adds sample data
	c.	views.sql – Creates the necessary views

4. (Optional)

Open college_database_v2.1.mwb in MySQL Workbench to visually explore the schema.


## 👨‍💻 Contributors

[Williams Asante](https://github.com/kraeon20)  
[Sara Kone](https://github.com/sadekone01)

---

## 🖇️ Links

**Branches:**  
[`version2.1_williams`](https://github.com/kraeon20/college_database_v2/tree/version2.1_williams)  
[`version2.1_sara`](https://github.com/kraeon20/college_database_v2/tree/version2.1_sara)

---

**Base Project:**  
[College Database Project – Version 1](https://github.com/Typher7/College_Database_v1)

## 📄 License

This project is licensed under the MIT License.
You are free to modify, use, and extend it for educational or testing purposes.