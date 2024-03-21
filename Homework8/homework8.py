import sqlite3

# ბაზის მონაცემები შექმნილია ჩათით, მაგრამ კოდი დავწერე ჩატის გარეშე. მადლობა.

connection = sqlite3.connect('data.db')
c = connection.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Students (
                student_id INTEGER PRIMARY KEY,
                name TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS Advisors (
                advisor_id INTEGER PRIMARY KEY,
                name TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS Student_Advisor (
                    student_id INTEGER,
                    advisor_id INTEGER,
                    FOREIGN KEY(student_id) REFERENCES Students(student_id),
                    FOREIGN KEY(advisor_id) REFERENCES Advisors(advisor_id),
                    PRIMARY KEY (student_id, advisor_id))''')

students_data = [
    (1, 'John Doe'),
    (2, 'Alice Smith'),
    (3, 'Michael Johnson'),
    (4, 'Emily Brown'),
    (5, 'David Wilson'),
    (6, 'Sarah Taylor'),
    (7, 'Daniel Martinez'),
    (8, 'Emma Anderson'),
    (9, 'James Garcia'),
    (10, 'Olivia Lee')
]
c.executemany("INSERT INTO Students (student_id, name) VALUES (?, ?)", students_data)

advisors_data = [
    (101, 'Dr. Smith'),
    (102, 'Prof. Johnson'),
    (103, 'Dr. Williams'),
    (104, 'Prof. Brown'),
    (105, 'Dr. Wilson'),
    (106, 'Prof. Taylor'),
    (107, 'Dr. Martinez'),
    (108, 'Prof. Anderson'),
    (109, 'Dr. Garcia'),
    (110, 'Prof. Lee')
]
c.executemany("INSERT INTO Advisors (advisor_id, name) VALUES (?, ?)", advisors_data)

student_advisor_data = [
    (1, 101),  # John Doe advised by Dr. Smith
    (2, 102),  # Alice Smith advised by Prof. Johnson
    (3, 103),  # Michael Johnson advised by Dr. Williams
    (4, 104),  # Emily Brown advised by Prof. Brown
    (5, 105),  # David Wilson advised by Dr. Wilson
    (6, 106),  # Sarah Taylor advised by Prof. Taylor
    (7, 107),  # Daniel Martinez advised by Dr. Martinez
    (8, 108),  # Emma Anderson advised by Prof. Anderson
    (9, 109),  # James Garcia advised by Dr. Garcia
    (10, 110),  # Olivia Lee advised by Prof. Lee
]

c.executemany("INSERT INTO Student_Advisor (student_id, advisor_id) VALUES (?, ?)", student_advisor_data)

c.execute('''
    SELECT Advisors.advisor_id, Advisors.name, COUNT(Student_Advisor.student_id) AS num_students
    FROM Advisors
    LEFT JOIN Student_Advisor ON Advisors.advisor_id = Student_Advisor.advisor_id
    GROUP BY Advisors.advisor_id, Advisors.name
''')

rows = c.fetchall()
for row in rows:
    advisor_id, advisor_name, num_students = row
    print(f"id of advisor: {advisor_id}, name of advisor: {advisor_name}, number of students: {num_students}")

connection.close()
