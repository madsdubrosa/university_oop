
from test_applications.oop.app_university.university import University


def main():
    uni = University(name="Monsters University", motto="Be Scary!!! RiseNGrind", first_semester="F2013")

    # MAJOR CREATION pt 1
    uni.add_major("sg160", "Scaring")  # id: sg160
    # print(f"one possible major is {uni.majors['sg160']}")
    # uni.display_major_info("sg160")

    # STUDENT CREATION
    # stud_1 = Student(name="Mike Lazowsky", major=scaring)
    # print(f"one of the students is {stud_1.name} and he is studying {stud_1.major.name}")
    uni.add_student("my134", "Mike Lazowsky", 18, "sg160")  # id: my134
    # uni.display_student_info("my134")

    # PROFESSOR CREATION
    uni.add_prof("ge184", "George")  # id: ge184
    # uni.display_prof_info("ge184")

    # COURSE CREATION
    uni.add_course("s1167", "Scaring 101", "Learn how to scare", "sg160", "ge184")
    # uni.display_course_info("s1167")  # id: s1167

    # MAJOR CREATION pt 2
    uni.add_major("lg185", "Laughing")  # id: lg185
    uni.add_course_to_major("s1167", "lg185")
    # uni.display_major_info("lg185")
    # uni.display_course_info("s1167")

    # STUDENT CREATION pt 2
    uni.add_student("jn144", "John", 19, "lg185")  # id: jn144

    # COURSE CREATION pt 2
    uni.add_course("l1118", "Laughing 101", "Learn how to laugh", "lg185", "1738")  # l1118

    # PROFESSOR CREATION pt 2
    uni.add_prof("kn148", "Kevin")  # id: kn148

    # ADD PROFESSOR TO COURSE AFTER COURSE CREATION
    uni.add_prof_to_course("kn148", "l1118")
    # uni.display_course_info("l1118")

    # REGISTER STUDENT FOR COURSE
    uni.register_students(["my134", "jn144"], "s1167")
    # uni.display_course_info("s1167")
    # print(f"what is the student registered for Scaring 101? {uni.courses['s1167'].students['my134'].name}")
    # print(f"what course is Mike Lazowsky registered for? {uni.students['my134'].current_courses['s1167'].name}")

    # List comprehension -- IGNORE
    # students = uni.profs["ge184"].get_students_for_course("s1167")  # [Student1, Student2]
    # student_names = [s.name for s in students]
    # print(", ".join(student_names))

    # GRADE ASSIGNMENT
    uni.new_semester("S2014")
    print(uni.students["my134"].transcript)
    print(uni.students["jn144"].transcript)
    # uni.students["my134"].transcript["F2013"]["s1167"][0].display_info()
    uni.students["my134"].transcript["F2013"]["s1167"][0].students["jn144"].display_info()
    # uni --> students --> mike --> transcript --> course --> students --> john


main()
