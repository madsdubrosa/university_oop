
class Course:
    """
    Course:
    --> id
    --> name: str
    --> syllabus: str
    --> students: map of student_id : str TO student : Student
    --> belonging_majors: map of major_id : str TO major : Major
    --> prof: Professor object
    """
    def __init__(self, identifier, name, syllabus, semester, major, prof):
        self.name = name.strip()
        self.syllabus = syllabus.strip()
        self.students = {}
        self.semester = semester
        self.id = identifier
        self.majors = {major.id: major}
        if prof:
            self.prof = prof
            self.prof.add_course(self, self.semester)
        else:
            self.prof = None

    def add_to_major(self, major):
        major.add_required_course(self)
        self.majors[major.id] = major

    def add_student(self, student):
        student.register_for_course(self)
        self.students[student.id] = student

    def add_prof(self, prof):
        self.prof = prof
        self.prof.add_course(self, self.semester)

    def display_info(self):
        print(f"Course Information:\n\tID: {self.id}\n\tName: {self.name}\n\tSyllabus: {self.syllabus}"
              f"\n\tNumber of Students: {len(self.students)}")
        for i, m in enumerate(self.majors.values()):
            print(f"\tMajor #{i+1}: {m.name}")
        if self.prof:
            self.prof.display_info()
