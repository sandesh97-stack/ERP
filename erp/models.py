# models.py
#This module was developed by N.PRANAY as part of an academic software project.

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


class Student(User):  # Inheritance
    def __init__(self, user_id, name, dept, sem):
        super().__init__(user_id, name)
        self.department = dept
        self.semester = sem
        self.registered_courses = []


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)


class Course:
    def __init__(self, course_id, name, credits, dept):
        self.course_id = course_id
        self.name = name
        self.credits = credits
        self.dept = dept
