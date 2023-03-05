# Problem Statement
# Given an integer n representing the student's total marks, the task is to find the student's grade. The grades are defined as
# n >= 90 - > A
# n >= 80 - > B
# n >= 70 - > C
# n >= 60 - > D
# otherwise F



marks = int(input())
def grade (marks):
    if marks>=90:
        return "A";
    elif marks>=80:
        return "B";
    elif marks>=70:
        return "C";
    elif marks>=60:
        return "D";
    else:
        return "F"
print(grade(marks))