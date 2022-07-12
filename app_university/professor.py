
import random
from collections import defaultdict


class Professor:
    def __init__(self, identifier, name):
        self.name = name.strip()
        self.id = identifier
        self.semester_to_courses = defaultdict(dict)

    def add_course(self, course, semester):
        self.semester_to_courses[semester][course.id] = course

    def _get_students_for_course(self, course_id, semester):
        courses = self.semester_to_courses[semester]
        if len(courses) == 0:
            print(f"WARNING: prof not teaching during semester {semester}")
            return
        course = courses.get(course_id, None)
        if not course:
            print(f"ERROR: course does not exist with id {course_id}")
            return
        return list(course.students.values())

    def assign_grades(self, semester):
        """
        for every student in every course the professor teaches, we assign a grade based on some external metrics
        """
        courses = self.semester_to_courses[semester]
        if len(courses) == 0:
            print(f"WARNING: prof not teaching during semester {semester}")
            return
        for c_id in courses:
            students = self._get_students_for_course(c_id, semester)
            for student in students:
                student.receive_grade(semester, c_id, random.randint(65, 100))

    def display_info(self):
        print(f"Professor Information:\n\tID: {self.id}\n\tName: {self.name}")
