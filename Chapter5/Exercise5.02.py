import  random
import  time

count = 0
correct_count = 0
NUMBER_OF_QUESTIONS = 10
start_time = time.time()

while count < NUMBER_OF_QUESTIONS:
    # Generate two random numbers
    number1 = random.randint(1, 15)
    number2 = random.randint(1, 15)

    # If number1 < number2, swap number1 with number2
    if number1 < number2:
        number1, number2 = number2, number1

    # Prompt the student to answer "What is number1 - number2?"
    answer = eval(input("What is " + str(number1) + ' - ' + str(number2) + '? '))

    # Grade the answer and display the result
    if number1 - number2 == answer:
        print("You are correct")
        correct_count += 1
    else:
        print("You are wrong. \n" +
              str(number1) + ' - ' + str(number2) + ' = ', number1 - number2)
    # Increase the count
    count += 1
end_time = time.time()
test_time = int(end_time - start_time)
print("Correct count is", correct_count, "out of", NUMBER_OF_QUESTIONS, "\nTest time is", test_time, "seconds")
