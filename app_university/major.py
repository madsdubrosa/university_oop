
class Major:
    def __init__(self, identifier, name, required_courses=[]):
        self.name = name.strip()
        self.required_courses = required_courses
        self.id = identifier

    def add_required_course(self, course):
        self.required_courses.append(course)

    def display_info(self):
        print(f"Major Information:\n\tID: {self.id}\n\tName: {self.name}")
        for c in self.required_courses:
            print(f"\tCourse: {c.name}")
