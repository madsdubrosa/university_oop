"""
Docstring on University class
"""


from test_applications.oop.app_university.course import Course
from test_applications.oop.app_university.major import Major
from test_applications.oop.app_university.professor import Professor
from test_applications.oop.app_university.student import Student


class University:
    def __init__(self, name, motto, first_semester):
        self.name = name
        self.motto = motto
        self.current_semester = first_semester
        self.students = {}
        self.profs = {}
        self.courses = {}
        self.majors = {}

    """ MAJORS """

    def add_major(self, identifier, name, required_courses=[]):
        major = Major(identifier, name, required_courses)
        self.majors[major.id] = major

    def display_major_info(self, major_id):
        if major_id in self.majors:
            self.majors[major_id].display_info()

    """ STUDENTS """

    def add_student(self, identifier, name, age, major_id, year_of_study=1):
        student = Student(identifier=identifier,
                          name=name,
                          age=age,
                          major=self.majors.get(major_id, None),
                          year_of_study=year_of_study)
        self.students[student.id] = student

    def register_student(self, stud_id, course_id):
        student = self.students.get(stud_id, None)
        course = self.courses.get(course_id, None)
        if not student:
            print(f"ERROR: student with id {stud_id} not found")
            return
        if not course:
            print(f"ERROR: course with id {course_id} not found")
            return
        course.add_student(student)

    def register_students(self, stud_ids, course_id):
        for stud_id in stud_ids:
            self.register_student(stud_id, course_id)

    def display_student_info(self, stud_id):
        if stud_id in self.students:
            self.students[stud_id].display_info()

    """ COURSES """

    def add_course(self, identifier, name, syllabus, major_id, prof_id):
        major = self.majors.get(major_id, None)
        if not major:
            print(f"WARNING: major with id {major_id} not found")
            major = None
        prof = self.profs.get(prof_id, None)
        if not prof:
            print(f"WARNING: prof with id {prof_id} not found")
            prof = None
        course = Course(identifier=identifier,
                        name=name,
                        syllabus=syllabus,
                        semester=self.current_semester,
                        major=major,
                        prof=prof)
        self.courses[course.id] = course

    def add_course_to_major(self, course_id, major_id):
        course = self.courses.get(course_id, None)
        if not course:
            print(f"ERROR: course with id {course_id} not found")
            return
        major = self.majors.get(major_id, None)
        if not major:
            print(f"ERROR: major with id {major_id} not found")
            return
        # if course is None or major is None:
        #     print("invalid course and/or major")
        #     return
        course.add_to_major(major)
        self.courses[course.id] = course
        self.majors[major.id] = major

    def display_course_info(self, course_id):
        if course_id in self.courses:
            self.courses[course_id].display_info()

    """ PROFESSORS """

    def add_prof(self, identifier, name):
        prof = Professor(identifier=identifier, name=name)
        self.profs[prof.id] = prof

    def add_prof_to_course(self, prof_id, course_id):
        prof = self.profs.get(prof_id, None)
        if not prof:
            print(f"ERROR: prof with id {prof_id} not found")
            return
        course = self.courses.get(course_id, None)
        if not course:
            print(f"ERROR: course with id {course_id} not found")
            return
        course.add_prof(prof)

    def display_prof_info(self, prof_id):
        if prof_id in self.profs:
            self.profs[prof_id].display_info()

    """ OTHER """

    def request_grade_submission(self):
        # for prof_id in self.profs:
        #     prof = self.profs[prof_id]
        for prof_id, prof in self.profs.items():
            prof.assign_grades(self.current_semester)

    def new_semester(self, new_term):
        self.request_grade_submission()
        self.current_semester = new_term
