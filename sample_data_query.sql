USE af25willa1_college_db;

-- =====================================================
-- 1. Departments
-- =====================================================
INSERT INTO department (department_name) VALUES
('Computer Science'),
('Mathematics'),
('English'),
('History'),
('Physics'),
('Chemistry'),
('Economics'),
('Psychology'),
('Sociology'),
('Art');

-- =====================================================
-- 2. Semesters
-- =====================================================
INSERT INTO semester (semester_term) VALUES
('Fall'),
('Spring'),
('Summer');

-- =====================================================
-- 3. Rooms
-- =====================================================
INSERT INTO room (room_number, building, capacity) VALUES
('A101', 'Science Hall', 40),
('B202', 'Engineering Building', 50),
('C303', 'Main Building', 35),
('D404', 'Library Annex', 25),
('E505', 'Humanities Hall', 30);

-- =====================================================
-- 4. People
-- =====================================================
-- (Example for 20 people; scale up to 500+ as needed)
INSERT INTO people (first_name, last_name, email, date_of_birth, gender, address, phone_number) VALUES
('John', 'Smith', 'john.smith@example.com', '1995-06-15', 'M', '123 Elm St', '555-1234'),
('Jane', 'Doe', 'jane.doe@example.com', '1998-09-12', 'F', '456 Oak Ave', '555-2345'),
('Robert', 'Williams', 'robert.williams@example.com', '1980-02-25', 'M', '789 Pine Rd', '555-3456'),
('Emily', 'Johnson', 'emily.johnson@example.com', '1999-11-05', 'F', '234 Maple Blvd', '555-4567'),
('David', 'Brown', 'david.brown@example.com', '1985-04-09', 'M', '567 Birch Ln', '555-5678'),
('Sarah', 'Miller', 'sarah.miller@example.com', '2000-01-15', 'F', '890 Cedar St', '555-6789'),
('Michael', 'Davis', 'michael.davis@example.com', '1978-03-10', 'M', '321 Walnut Dr', '555-7890'),
('Jessica', 'Garcia', 'jessica.garcia@example.com', '1997-07-21', 'F', '654 Chestnut Rd', '555-8901'),
('Daniel', 'Martinez', 'daniel.martinez@example.com', '1996-10-01', 'M', '987 Spruce Ct', '555-9012'),
('Laura', 'Hernandez', 'laura.hernandez@example.com', '1989-12-30', 'F', '111 Poplar St', '555-0123'),
('Steven', 'Lopez', 'steven.lopez@example.com', '1975-08-20', 'M', '222 Fir Ln', '555-2346'),
('Patricia', 'Gonzalez', 'patricia.gonzalez@example.com', '1994-03-14', 'F', '333 Cypress Rd', '555-3457'),
('Thomas', 'Wilson', 'thomas.wilson@example.com', '1992-09-17', 'M', '444 Palm Ave', '555-4568'),
('Linda', 'Anderson', 'linda.anderson@example.com', '1988-05-19', 'F', '555 Redwood St', '555-5679'),
('Matthew', 'Thomas', 'matthew.thomas@example.com', '1990-07-23', 'M', '666 Sequoia Blvd', '555-6780'),
('Barbara', 'Taylor', 'barbara.taylor@example.com', '1979-11-11', 'F', '777 Magnolia Ct', '555-7891'),
('Christopher', 'Moore', 'christopher.moore@example.com', '1983-04-04', 'M', '888 Aspen Way', '555-8902'),
('Elizabeth', 'Jackson', 'elizabeth.jackson@example.com', '2001-02-22', 'F', '999 Willow St', '555-9013'),
('Joshua', 'White', 'joshua.white@example.com', '1993-10-09', 'M', '1010 Pinecrest Rd', '555-0124'),
('Karen', 'Harris', 'karen.harris@example.com', '1986-06-03', 'F', '1111 Oakridge Ave', '555-1235');

-- =====================================================
-- 5. Faculty
-- =====================================================
INSERT INTO faculty (people_id, department_id, office_location) VALUES
(3, 1, 'ENG-201'),
(5, 2, 'MATH-105'),
(7, 3, 'ENG-302'),
(11, 4, 'HIST-210'),
(13, 5, 'PHY-115');

-- =====================================================
-- 6. Students
-- =====================================================
INSERT INTO student (people_id, cumulative_gpa, advisor_id) VALUES
(1, 3.5, 1),
(2, 3.8, 1),
(4, 3.6, 2),
(6, 3.2, 3),
(8, 3.7, 1),
(9, 3.1, 2),
(10, 2.9, 4),
(12, 3.9, 5),
(14, 3.0, 3),
(15, 2.8, 4);

-- =====================================================
-- 7. Courses
-- =====================================================
INSERT INTO course (course_code, course_title, credits, department_id) VALUES
('CS101', 'Intro to Programming', 3, 1),
('CS201', 'Data Structures', 4, 1),
('MATH101', 'Calculus I', 4, 2),
('ENG101', 'English Composition', 3, 3),
('HIST201', 'World History', 3, 4),
('PHY101', 'Physics I', 4, 5),
('CHEM101', 'General Chemistry', 4, 6),
('ECO101', 'Microeconomics', 3, 7),
('PSY101', 'Intro to Psychology', 3, 8),
('ART101', 'Art Appreciation', 3, 10);

-- =====================================================
-- 8. Course Offerings
-- =====================================================
INSERT INTO course_offering (section_number, course_id, semester_id1, room_id1, faculty_id) VALUES
('001', 1, 1, 1, 1),
('001', 2, 2, 2, 1),
('001', 3, 1, 3, 2),
('001', 4, 3, 4, 3),
('001', 5, 1, 5, 4),
('001', 6, 2, 1, 5);

-- =====================================================
-- 9. Letter Grades
-- =====================================================
INSERT INTO letter_grade (grade_symbol, grade_points, letter_grade_col) VALUES
('A', 4.0, 'Excellent'),
('B', 3.0, 'Good'),
('C', 2.0, 'Average'),
('D', 1.0, 'Below Average'),
('F', 0.0, 'Fail'),
('I', NULL, 'Incomplete'),
('W', NULL, 'Withdrawn');

-- =====================================================
-- 10. Enrollment
-- =====================================================
INSERT INTO enrollment (letter_grade_id, student_id, course_offering_id) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 2, 1),
(1, 2, 3),
(2, 3, 4),
(3, 4, 5),
(4, 5, 1),
(5, 6, 2),
(1, 7, 3),
(2, 8, 4),
(3, 9, 5),
(4, 10, 6);

-- =====================================================
-- 11. Staff
-- =====================================================
INSERT INTO staff (people_id, department_id, staffcol) VALUES
(16, 1, 'Department Secretary'),
(17, 2, 'Administrative Assistant'),
(18, 3, 'Registrar Clerk'),
(19, 4, 'Lab Technician'),
(20, 5, 'Library Assistant');

