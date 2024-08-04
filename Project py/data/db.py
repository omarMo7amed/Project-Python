import sqlite3

conn = sqlite3.connect("college_registration.db")
cursor = conn.cursor()


def create_departments() -> None:
    # Departments
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS departments (
        department_id INTEGER PRIMARY KEY AUTOINCREMENT,
        department_name TEXT NOT NULL
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


def main():
    create_departments()
    create_students()
    conn.commit()
    conn.close()

    print("Database and tables created successfully, and sample data inserted.")


# main()

cursor = cursor.execute("SELECT * FROM students WHERE GPA >= 3.1")
data = cursor.fetchall()

for name in data:
    print(name)
