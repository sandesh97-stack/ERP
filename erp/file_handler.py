# file_handler.py

from models import Student, Course

students = []
courses = []


def save_data():
    try:
        with open("students.txt", "w") as f:
            for s in students:
                course_ids = ",".join(str(c.course_id) for c in s.registered_courses)
                f.write(f"{s.user_id}|{s.name}|{s.department}|{s.semester}|{course_ids}\n")

        with open("courses.txt", "w") as f:
            for c in courses:
                f.write(f"{c.course_id}|{c.name}|{c.credits}|{c.dept}\n")

        print("✔ Data saved successfully!")

    except Exception as e:
        print("Error:", e)


def load_data():
    try:
        with open("courses.txt", "r") as f:
            for line in f:
                c_id, name, credits, dept = line.strip().split("|")
                courses.append(Course(int(c_id), name, int(credits), dept))
    except:
        load_default_courses()

    try:
        with open("students.txt", "r") as f:
            for line in f:
                parts = line.strip().split("|")
                s_id, name, dept, sem = parts[:4]
                student = Student(int(s_id), name, dept, int(sem))

                if len(parts) == 5 and parts[4]:
                    for cid in parts[4].split(","):
                        for c in courses:
                            if c.course_id == int(cid):
                                student.registered_courses.append(c)

                students.append(student)
    except:
        pass


def load_default_courses():
    courses.extend([
        Course(101, "C Programming", 3, "CSE"),
        Course(102, "Data Structures", 4, "CSE"),
        Course(103, "DBMS", 4, "CSE"),
        Course(104, "OS", 4, "CSE")
    ])