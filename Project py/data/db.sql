
CREATE TABLE IF NOT EXISTS departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    department_name TEXT NOT NULL,
    description TEXT
);


CREATE TABLE IF NOT EXISTS students (
    student_id TEXT PRIMARY KEY NOT NULL ,
    name TEXT NOT NULL,
    student_code TEXT UNIQUE NOT NULL,
    department_id INTEGER DEFAULT NULL,
    level INTEGER NOT NULL,
    hours_passed INTEGER NOT NULL,
    gpa REAL NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments (department_id)
);


INSERT INTO departments (department_name) VALUES (
    'Computer Science'
);

INSERT INTO departments (department_name) VALUES (
    'Information Systems'
);

INSERT INTO departments (department_name) VALUES (
    'Artificial Intelligence'
);

INSERT INTO departments (department_name) VALUES (
    'Scientific Computing'
);

SELECT * FROM departments;
SELECT * FROM  students;

-- Original data
INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Amr Ashraf Mohamed', '30402051700999', '202233235', 3, 61, 3.51);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Sara Ahmed Ali', '30402051701000', '202233236', 3, 40, 3.75);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Mohamed Tarek Salim', '30402051701001', '202233237', 3, 64, 3.85);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Lina Hassan Omar', '30402051701002', '202233238', 3, 60, 3.60);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Youssef Adel Kamal', '30402051701003', '202233239', 3, 75, 3.45);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Nour Ibrahim Zaki', '30402051701004', '202233240', 3, 55, 2.1);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Layla Ahmed Nabil', '30402051701005', '202233241', 3, 59, 2.2);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Omar Khaled Salah', '30402051701006', '202233242', 3, 70, 2.3);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Fatma Hany Ali', '30402051701007', '202233243', 3, 55, 2.5);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Hussein Gamal Farid', '30402051701008', '202233244', 3, 65, 2.7);

-- Additional data (with unique student_id and student_code)
INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Ali Mohamed Ahmed', '30402051701009', '202233245', 3, 49, 2.76);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Mona Hussein Ali', '30402051701010', '202233246', 3, 52, 2.45);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Khaled Saad Ahmed', '30402051701011', '202233247', 3, 55, 1.1);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Jana Ibrahim Khaled', '30402051701012', '202233248', 3, 60, 1.34);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Rami Adel Saad', '30402051701013', '202233249', 3, 50, 1.5);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Sara Khaled Ahmed', '30402051701014', '202233250', 3, 62, 1.6);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Nabil Hasan Omar', '30402051701015', '202233251', 3, 47, 1.88);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Heba Tamer Ahmed', '30402051701016', '202233252', 3, 59, 1.9);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Omar Ahmed Saad', '30402051701017', '202233253', 3, 63, 0.4);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Fatima Osama Ahmed', '30402051701018', '202233254', 3, 48, 0.6);

-- Additional unique data
INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Ahmed Mohamed Salah', '30402051701019', '202233255', 3, 49, 0.7);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Hanan Ali Rami', '30402051701020', '202233256', 3, 56, 0.9);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Ibrahim Saad Khaled', '30402051701021', '202233257', 3, 53, 2.1);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Zainab Mohamed Samir', '30402051701022', '202233258', 3, 62, 2.0);

-- ----------------------------------------------------------------
INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Hossam Ahmed Fadi', '30402051701023', '202233259', 3, 48, 2.95);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Rana Ibrahim Hassan', '30402051701024', '202233260', 3, 60, 3.35);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Mona Saad Ali', '30402051701025', '202233261', 3, 51, 3.5);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Yasser Mohamed Khaled', '30402051701026', '202233262', 3, 59, 3.7);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Laila Ahmed Farid', '30402051701027', '202233263', 3, 46, 3.9);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Amina Tarek Ahmed', '30402051701028', '202233264', 3, 57, 4);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Jamal Saad Hossam', '30402051701029', '202233265', 3, 63, 3.3);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Dalia Ibrahim Khaled', '30402051701030', '202233266', 3, 49, 3.15);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Mariam Mohamed Rami', '30402051701031', '202233267', 3, 55, 3.05);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Nabil Ahmed Osama', '30402051701032', '202233268', 3, 62, 3.20);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Khadija Saad Fadi', '30402051701033', '202233269', 3, 47, 2.90);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Sami Mohamed Ibrahim', '30402051701034', '202233270', 3, 58, 3.05);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Hala Ahmed Rami', '30402051701035', '202233271', 3, 54, 3.25);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Kamal Mohamed Hossam', '30402051701036', '202233272', 3, 50, 2.85);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Rasha Ibrahim Ahmed', '30402051701037', '202233273', 3, 46, 3.00);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Nasser Saad Khaled', '30402051701038', '202233274', 3, 61, 3.10);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Yasmine Mohamed Ahmed', '30402051701039', '202233275', 3, 59, 3.05);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Ibrahim Ahmed Hossam', '30402051701040', '202233276', 3, 63, 3.20);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Hadiya Saad Ahmed', '30402051701041', '202233277', 3, 55, 3.25);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Samir Mohamed Fadi', '30402051701042', '202233278', 3, 48, 2.80);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Dina Ahmed Khaled', '30402051701043', '202233279', 3, 57, 3.00);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Moustafa Saad Ibrahim', '30402051701044', '202233280', 3, 52, 2.85);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Salma Ibrahim Rami', '30402051701045', '202233281', 3, 56, 3.10);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Faris Mohamed Ahmed', '30402051701046', '202233282', 3, 49, 3.05);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Layla Saad Hossam', '30402051701047', '202233283', 3, 58, 3.15);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Amira Mohamed Saad', '30402051701048', '202233284', 3, 54, 2.90);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Nadia Ibrahim Khaled', '30402051701049', '202233285', 3, 47, 3.00);

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Ayman Ahmed Fadi', '30402051701050', '202233286', 3, 55, 3.05);




DELETE FROM departments
WHERE department_id = 5;

UPDATE students
SET level = 3
WHERE student_id = 2;


SELECT * FROM departments;
SELECT * FROM students;
SELECT description  FROM departments WHERE department_name = 'Computer Science';
