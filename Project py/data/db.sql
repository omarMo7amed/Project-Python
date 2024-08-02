
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


CREATE TABLE IF NOT EXISTS registrations (
    registration_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL,
    department_id INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (student_id),
    FOREIGN KEY (department_id) REFERENCES departments (department_id),
    UNIQUE (student_id, department_id)
);



INSERT INTO departments (department_name, description) VALUES (
    'Computer Science',
    'The main concern of the Department of Computer Science is to follow up, ' ||
    'assimilate and develop scientific concepts behind what computers accomplish ' ||
    'and how they accomplish with knowledge of computer construction and ' ||
    'how they operate The Department is interested in analysing, designing ' ||
    'and measuring the complexity of algorithms used to solve real problems, ' ||
    'The section focuses on AI applications in which computers simulate a human''s' ||
    ' intelligent behaviour in information processing Education and research on courses such as:' ||
    'Algorithms Analysis and Design - Mock Languages and Mechanics Theory - Systems Performance Assessment -' ||
    ' Computer Arabization - Artificial Intelligence - Expert systems - Neural networks - Distributed accounts -' ||
    ' Programming Fundamentals - Structural programming - Shea Programming - Operating systems ' ||
    '- Software Translators theory - Image processing - ' ||
    'Logical programming - Speech processing - Computer vision - cognition science'
);

INSERT INTO departments (department_name, description) VALUES (
    'Information Systems',
    'The main concern of the Information Systems Section is to examine all substantive and senior management ' ||
    'issues and planning policies associated with the use of computers in the establishment of information systems ' ||
    'for bodies and institutions. The Section addresses in a balanced manner the theoretical and scientific aspects of' ||
    ' the characterization, analysis, design, implementation and management of information systems while maximizing' ||
    ' the use of information technology infrastructure. The Information Systems Section''s ' ||
    'interest is to teach and conduct research on courses such as:' ||
    ' Systems Analysis and Design - Information Engineering - Information Security - Information Systems Applications -' ||
    ' Desktop Automation Systems - Library Mechanization - Management Information Systems - ' ||
    'Geographic Information Systems - Software Engineering - Data Structures - File Organization - ' ||
    'Database Management Systems - Business Management - Decision Support Systems - Marketing Information Systems - ' ||
    'E-Commerce Systems - TransProcessing - Crisis Management and Disaster Management Systems Systems - ' ||
    'Information Systems Systems - Information Systems Management Systems'
);

INSERT INTO departments (department_name, description) VALUES (
    'Artificial Intelligence',
    'The main concern of the Department of Artificial Intelligence is the study and simulation of the human mind' ||
    ' and understanding of its nature and its modus operandi such as its ability to think, ' ||
    'detect and benefit from previous experiments and is done through the development of computer software' ||
    ' capable of simulating intelligent human behaviour, As well as building and designing different smart ' ||
    'systems in various fields and designing robot where AI can be used everywhere around us from self-driving cars,' ||
    ' drones, translation or investment software, expert systems, natural language processing, voice discrimination, ' ||
    'image discrimination and medical diagnosis, Stock trading, automated control, video games, children''s toys,' ||
    ' online search engines, anthropogenic design science and many other applications spread in life.' ||
    ' The section includes the following scientific areas: artificial intelligence - smart systems - machine learning - expert systems -' ||
    ' neural networks - natural language processing - multiple agent systems - knowledge base systems - robots.'
);

INSERT INTO departments (department_name, description) VALUES (
    'Scientific Computing',
    'The Department of Scientific Accounts is concerned with the development and development of new treatments ' ||
    'for the educational process and scientific research by exploiting fast-developing and high-performance computational technology. ' ||
    'Scientific calculations are concerned with the systematic development of computers and computational solution methods in understanding, ' ||
    'modeling and simulating phenomena in the natural and engineering sciences. ' ||
    'The Department of Scientific Calculations Trilateral Scientific Calculations, ' ||
    'Theoretical Thought and Experiment is an effective means of investigation and foresight, ' ||
    'leading to a degree of understanding that in many cases only theoretical understanding or experience cannot be attained. ' ||
    'It is worth mentioning that there is a great need for this new quality of graduates in all centers and research laboratories of universities, ' ||
    'institutes, scientific research sectors, industry, petroleum, mineral wealth and environmental affairs.'
);

SELECT * FROM departments;
SELECT * FROM  students;
SELECT * FROM registrations;

INSERT INTO students (name, student_id, student_code, level, hours_passed, gpa)
VALUES ('Amr Ashraf Mohamed Mostafa', '30402051700999', '202233235', 3, 61, 3.51);

-- INSERT INTO students (student_name, student_id, student_code, department_id, level, hours_passed, gpa)
-- VALUES ('Mohamed Ahmed Mohammed Khaled', '30402051700999', '202233235', 4, 61, 3.21);
--
-- INSERT INTO students (student_name, student_id, student_code, department_id, level, hours_passed, gpa)
-- VALUES ('John Snow Ehab Wagdy', '30402051700111', '202233236', 3, 58, 3.78);
--
-- INSERT INTO students (student_name, student_id, student_code, department_id, level, hours_passed, gpa)
-- VALUES ('Karim Ehab Ahmed Yousif', '30402051755182', '202233237', 3, 61, 1.9);
--
-- INSERT INTO students (student_name, student_id, student_code, department_id, level, hours_passed, gpa)
-- VALUES ('Mostafa Mohammed Mahmoud Yousif', '30402051712257', '202233238', 3, 61, 2.3);
--
-- INSERT INTO students (student_name, student_id, student_code, department_id, level, hours_passed, gpa)
-- VALUES ('Omar Magdy Mohamed Yousif', '30402051755991', '202233239', 3, 61, 3.9);
--
-- INSERT INTO students (student_name, student_id, student_code, department_id, level, hours_passed, gpa)
-- VALUES ('Ahmed Waled John Mohamed', '30402051755120', '202233240', 3, 61, 2.1);
--
-- INSERT INTO students (student_name, student_id, student_code, department_id, level, hours_passed, gpa)
-- VALUES ('Ashraf Mohamed Abdel3ati Wagdy', '30402051745672', '202233241', 3, 61, 2.89);
--
-- INSERT INTO students (student_name, student_id, student_code, department_id, level, hours_passed, gpa)
-- VALUES ('Asmaa John Ahmed Khalel', '30402051745001', '202233242', 3, 58, 3.0);
--
-- INSERT INTO students (student_name, student_id, student_code, department_id, level, hours_passed, gpa)
-- VALUES ('Waled Ahmed Yousif Saad', '30402051777420', '202233243', 3, 61, 3.2);
--
-- INSERT INTO students (student_name, student_id, student_code, department_id, level, hours_passed, gpa)
-- VALUES ('Sara Ahmed Ali', '30402051799999', '202233244', 3, 60, 3.6);
--
-- INSERT INTO students (student_name, student_id, student_code, department_id, level, hours_passed, gpa)
-- VALUES ('Mohamed Ali Hassan', '30402051800000', '202233245', 3, 62, 3.3);
--
-- INSERT INTO students (student_name, student_id, student_code, department_id, level, hours_passed, gpa)
-- VALUES ('Heba Hossam Youssef', '30402051811111', '202233246', 3, 64, 3.8);
--
-- INSERT INTO students (student_name, student_id, student_code, department_id, level, hours_passed, gpa)
-- VALUES ('Khaled Tamer Mostafa', '30402051822222', '202233247', 3, 59, 2.7);
--
-- INSERT INTO students (student_name, student_id, student_code, department_id, level, hours_passed, gpa)
-- VALUES ('Noura Ibrahim Saleh', '30402051833333', '202233248', 3, 63, 3.5);




DELETE FROM departments
WHERE department_id = 5;

UPDATE students
SET level = 3
WHERE student_id = 2;


SELECT * FROM departments;
SELECT description  FROM departments WHERE department_name = 'Computer Science';
