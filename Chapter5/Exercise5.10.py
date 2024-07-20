number_of_students = int(input("Enter the number of students: "))
count = 0
score = 0
student = ''
largest_student = ''
largest_score = 0
while count < number_of_students:
    student = input("Student: ")
    score = eval(input("Score: "))
    if score > largest_score:
        largest_student = student
        largest_score = score
    count += 1
print("The student with highest score is",largest_student, "and the score is", largest_score)