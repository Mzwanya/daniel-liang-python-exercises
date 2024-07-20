'''
*5.11 (Find the two highest scores) Write a program that prompts the user to enter the
number of students and each student’s score, and displays the highest and second-highest scores.
'''

number_of_students = int(input("Enter the number of students: "))
count = 0
score = 0
student = ''
highest_student = ''
largest_score = 1
second_highest_student = ''
second_largest_score = 0

while count < number_of_students:
    student = input("Student: ")
    score = eval(input("Score: "))
    if score > largest_score:
        highest_student = student
        largest_score = score
    elif score > second_largest_score:
        second_highest_student = student
        second_largest_score = score
    count += 1
print("The student with highest score is " + str(highest_student) + " with a score of " + str(largest_score) + '.' + '\n' +\
      "While the student with second highest score is " + str(second_highest_student) + " with a score of " + str(second_largest_score))