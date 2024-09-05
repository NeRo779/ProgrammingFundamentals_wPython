def pair_of_rows(student: str, grade: float, student_dict: dict):
    if student not in student_dict:
        student_dict[student] = []
    student_dict[student].append(grade)

score = int(input())
grade_register = {}
avg_score = lambda item: sum(item) / len(item)

for _ in range(score):
    student_name = input()
    student_grade = float(input())
    pair_of_rows(student_name, student_grade, grade_register)

print(*[f"{key} -> {avg_score(value):.2f}" for key, value in grade_register.items()
    if avg_score(value) >= 4.5], sep="\n")

