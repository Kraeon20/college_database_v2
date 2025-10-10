# populate_college_db.py

from sshtunnel import SSHTunnelForwarder
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import random
from faker import Faker
import phonenumbers

# Setup Faker and load env vars
fake = Faker("en_US")
load_dotenv()

SSH_HOST = os.getenv("SSH_HOST")
SSH_USER = os.getenv("SSH_USER")
SSH_PASS = os.getenv("SSH_PASS")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASS = os.getenv("MYSQL_PASS")
MYSQL_DB   = os.getenv("MYSQL_DB")


# ------------------------------------------------------
# SSH + DB connection
# ------------------------------------------------------
def connect_via_ssh():
    tunnel = SSHTunnelForwarder(
        (SSH_HOST, 22),
        ssh_username=SSH_USER,
        ssh_password=SSH_PASS,
        remote_bind_address=(MYSQL_HOST, 3306)
    )
    tunnel.start()
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=tunnel.local_bind_port,
        user=MYSQL_USER,
        password=MYSQL_PASS,
        database=MYSQL_DB,
        autocommit=False
    )
    return tunnel, conn


# ------------------------------------------------------
# Generate a formatted U.S. phone number
# ------------------------------------------------------
def make_phone():
    """Always generate a 10-digit US-style phone number like 402-734-9281."""
    # Optionally fix Nebraska area codes if you want realism
    area_codes = [402, 308, 531]  # Nebraska area codes
    area = random.choice(area_codes)
    exchange = random.randint(200, 999)
    subscriber = random.randint(1000, 9999)
    return f"{area}-{exchange}-{subscriber}"

# ------------------------------------------------------
# Main population logic
# ------------------------------------------------------
def populate_college_db():
    tunnel, conn = connect_via_ssh()
    cursor = conn.cursor()
    print("🚀 Connected, inserting data...")

    cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
    conn.commit()

    # 1. Departments
    departments = [
        "Computer Science", "Mathematics", "English", "History", "Physics",
        "Chemistry", "Economics", "Psychology", "Sociology", "Art"
    ]
    cursor.executemany("INSERT INTO department (department_name) VALUES (%s)", [(d,) for d in departments])
    conn.commit()
    print("✅ Departments inserted.")

    # 2. Semesters
    semesters = [("Fall",), ("Spring",), ("Summer",)]
    cursor.executemany("INSERT INTO semester (semester_term) VALUES (%s)", semesters)
    conn.commit()
    print("✅ Semesters inserted.")

    # 3. Rooms
    buildings = ["Science Hall", "Engineering Building", "Main Building", "Library Annex", "Humanities Hall"]
    rooms = [(f"{chr(65+i)}{100+i*101}", b, random.choice([25, 30, 35, 40, 50])) for i, b in enumerate(buildings)]
    cursor.executemany("INSERT INTO room (room_number, building, capacity) VALUES (%s,%s,%s)", rooms)
    conn.commit()
    print("✅ Rooms inserted.")

    # 4. People (2,000)
    people_ids = []
    print("👥 Generating 2,000 people...")
    batch_size = 500
    total_people = 2000

    for batch_start in range(0, total_people, batch_size):
        batch_data = []
        current_batch = min(batch_size, total_people - batch_start)
        for _ in range(current_batch):
            first = fake.first_name()
            last = fake.last_name()
            email = f"{first.lower()}.{last.lower()}@example.com"
            dob = fake.date_of_birth(minimum_age=18, maximum_age=65)
            gender = random.choice(["M", "F"])
            address = f"{random.randint(100,999)} {fake.street_name()}"
            phone = make_phone()
            batch_data.append((first, last, email, dob, gender, address, phone))

        cursor.executemany("""
            INSERT INTO people (first_name, last_name, email, date_of_birth, gender, address, phone_number)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        """, batch_data)
        conn.commit()

        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()[0]
        start_id = last_id - current_batch + 1
        people_ids.extend(range(start_id, last_id + 1))
        print(f"   ✅ Inserted batch {batch_start + current_batch}/{total_people}")

    print("✅ Inserted 2,000 people successfully.")

    # 5. Faculty (~5%)
    faculty_count = total_people // 20
    faculty_ids = []
    for pid in random.sample(people_ids, faculty_count):
        dept_id = random.randint(1, len(departments))
        office = f"{departments[dept_id-1][:3].upper()}-{random.randint(100,399)}"
        cursor.execute("INSERT INTO faculty (people_id, department_id, office_location) VALUES (%s,%s,%s)", (pid, dept_id, office))
        faculty_ids.append(cursor.lastrowid)
    conn.commit()
    print(f"✅ Faculty inserted ({faculty_count}).")

    # 6. Students (~60%)
    student_count = int(total_people * 0.6)
    student_ids = []
    for pid in random.sample(people_ids, student_count):
        advisor = random.choice(faculty_ids)
        gpa = round(random.uniform(2.0, 4.0), 2)
        cursor.execute("INSERT INTO student (people_id, cumulative_gpa, advisor_id) VALUES (%s,%s,%s)", (pid, gpa, advisor))
        student_ids.append(cursor.lastrowid)
    conn.commit()
    print(f"✅ Students inserted ({student_count}).")

    # 7. Courses
    base_courses = [
        ("CS101", "Intro to Programming", 3, 1),
        ("CS201", "Data Structures", 4, 1),
        ("MATH101", "Calculus I", 4, 2),
        ("ENG101", "English Composition", 3, 3),
        ("HIST201", "World History", 3, 4),
        ("PHY101", "Physics I", 4, 5),
        ("CHEM101", "General Chemistry", 4, 6),
        ("ECO101", "Microeconomics", 3, 7),
        ("PSY101", "Intro to Psychology", 3, 8),
        ("ART101", "Art Appreciation", 3, 10)
    ]
    cursor.executemany("INSERT INTO course (course_code, course_title, credits, department_id) VALUES (%s,%s,%s,%s)", base_courses)
    conn.commit()
    print("✅ Courses inserted.")

    cursor.execute("SELECT course_id FROM course")
    course_ids = [row[0] for row in cursor.fetchall()]

    # 8. Course offerings
    offerings = []
    for cid in course_ids:
        for _ in range(random.randint(2, 5)):
            section = f"{random.randint(1,3):03}"
            sem = random.randint(1, 3)
            room = random.randint(1, len(rooms))
            faculty = random.choice(faculty_ids)
            offerings.append((section, cid, sem, room, faculty))
    cursor.executemany("INSERT INTO course_offering (section_number, course_id, semester_id1, room_id1, faculty_id) VALUES (%s,%s,%s,%s,%s)", offerings)
    conn.commit()
    print(f"✅ Course offerings inserted ({len(offerings)}).")

    # 9. Letter grades
    grades = [
        ("A", 4.0, "Excellent"),
        ("B", 3.0, "Good"),
        ("C", 2.0, "Average"),
        ("D", 1.0, "Below Average"),
        ("F", 0.0, "Fail"),
        ("I", None, "Incomplete"),
        ("W", None, "Withdrawn")
    ]
    cursor.executemany("INSERT INTO letter_grade (grade_symbol, grade_points, letter_grade_col) VALUES (%s,%s,%s)", grades)
    conn.commit()
    print("✅ Letter grades inserted.")

    # 10. Enrollment
    cursor.execute("SELECT course_offering_id FROM course_offering")
    offering_ids = [r[0] for r in cursor.fetchall()]
    enrollments = []
    for s_id in student_ids:
        for _ in range(random.randint(3, 6)):
            enrollments.append((random.randint(1, len(grades)), s_id, random.choice(offering_ids)))
    print(f"📝 Preparing {len(enrollments)} enrollments...")
    for i in range(0, len(enrollments), 5000):
        cursor.executemany("INSERT INTO enrollment (letter_grade_id, student_id, course_offering_id) VALUES (%s,%s,%s)", enrollments[i:i+5000])
        conn.commit()
    print(f"✅ Enrollments inserted ({len(enrollments)}).")

    # 11. Staff
    staff_roles = ["Department Secretary", "Administrative Assistant", "Registrar Clerk", "Lab Technician", "Library Assistant"]
    staff_count = max(1, total_people // 50)
    for pid in random.sample(people_ids, staff_count):
        dept = random.randint(1, len(departments))
        role = random.choice(staff_roles)
        cursor.execute("INSERT INTO staff (people_id, department_id, staffcol) VALUES (%s,%s,%s)", (pid, dept, role))
    conn.commit()
    print(f"✅ Staff inserted ({staff_count}).")

    cursor.execute("SET FOREIGN_KEY_CHECKS=1;")
    conn.commit()
    cursor.close()
    conn.close()
    tunnel.stop()
    print("🎉 Finished populating database successfully!")


if __name__ == "__main__":
    try:
        populate_college_db()
    except Error as e:
        print(f"❌ MySQL Error: {e}")