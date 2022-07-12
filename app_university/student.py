
from collections import defaultdict


class Student:
    def __init__(self, identifier, name, age, major=None, year_of_study=1):
        self.name = name.strip()
        self.age = age
        self.major = major
        self.year_of_study = year_of_study
        self.current_courses = {}
        self.transcript = defaultdict(dict)
        self.id = identifier

    def __str__(self):  # ASCII
        return f"{self.id}"

    def receive_grade(self, semester, course_id, grade):
        course = self.current_courses.get(course_id, None)
        if not course:
            return
        self.transcript[semester][course_id] = (course, grade)

    def register_for_course(self, course):
        self.current_courses[course.id] = course

    def display_info(self):
        print(f"Student Information:\n\tID: {self.id}\n\tName: {self.name}\n\tAge: {self.age}\n\tYear: "
              f"{self.year_of_study}")
        if self.major:
            self.major.display_info()
