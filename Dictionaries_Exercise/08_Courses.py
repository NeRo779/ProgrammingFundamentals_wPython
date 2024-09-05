def add_student(name: str, current_course: str, courses: dict):
    if current_course not in courses:
        courses[current_course] = []
    courses[current_course].append(name)

total_courses = {}
while 1:
    course_info = input().split(" : ")
    if course_info[0] == "end":
        break
    course_name, student_name = course_info
    add_student(student_name, course_name, total_courses)

for course, total_students in total_courses.items():
    print(f"{course}: {len(total_students)}")
    print(*[f" -- {student}" for student in total_students], sep="\n")


