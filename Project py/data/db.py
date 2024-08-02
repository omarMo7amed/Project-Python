import sqlite3

conn = sqlite3.connect("college_registration.db")
cursor = conn.cursor()


def create_departments() -> None:
    # Departments
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS departments (
        department_id INTEGER PRIMARY KEY AUTOINCREMENT,
        department_name TEXT NOT NULL,
        description TEXT
    );
    """
    )


def create_students() -> None:
    # Students
    cursor.execute(
        """
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
    """
    )


def create_registrations() -> None:

    # Registrations
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS registrations (
    registration_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL,
    department_id INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (student_id),
    FOREIGN KEY (department_id) REFERENCES departments (department_id),
    UNIQUE (student_id, department_id)
);
    """
    )


def insert_into_CS_DEP():
    cursor.execute(
        """
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
)
"""
    )


def insert_into_IS_DEP():
    cursor.execute(
        """
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
)
"""
    )


def insert_into_AI_DEP():
    cursor.execute(
        """
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
)
"""
    )


def insert_into_SC_DEP():
    cursor.execute(
        """
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
)
"""
    )


def main():
    create_departments()
    create_students()
    create_registrations()

    conn.commit()
    conn.close()

    print("Database and tables created successfully, and sample data inserted.")


main()

# cursor = cursor.execute("SELECT * FROM students")
# data = cursor.fetchall()

# for name in data:
#     print(name)
