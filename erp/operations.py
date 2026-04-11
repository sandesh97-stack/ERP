# operations.py
#This module was developed by ABHINAV REDDY as part of an academic software project.

from file_handler import students, courses
from models import Student


def register_student():
    try:
        sid = int(input("Enter ID: "))
        name = input("Enter Name: ")
        dept = input("Enter Dept: ")
        sem = int(input("Enter Semester: "))

        students.append(Student(sid, name, dept, sem))
        print("✔ Student Registered")

    except:
        print(" Invalid Input")


def find_student(sid):
    for s in students:
        if s.user_id == sid:
            return s
    return None


def view_courses():
    for c in courses:
        print(f"{c.course_id} - {c.name} ({c.credits})")


def register_course():
    try:
        sid = int(input("Enter Student ID: "))
        student = find_student(sid)

        if not student:
            print("Student not found")
            return

        view_courses()
        cid = int(input("Enter Course ID: "))

        for c in courses:
            if c.course_id == cid:
                student.registered_courses.append(c)
                print("✔ Course Registered")
                return

        print("Course not found")

    except:
        print(" Invalid Input")


def view_registered_courses():
    try:
        sid = int(input("Enter Student ID: "))
        student = find_student(sid)

        if not student:
            print("Student not found")
            return

        for c in student.registered_courses:
            print(f"{c.name}")

    except:
        print("Error")
