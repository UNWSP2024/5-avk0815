# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.

import random

def math_quiz():
    num1 = random.randint(0, 1000)
    num2 = random.randint(0, 1000)
   
    print(" ",num1)
    print("+", num2)
    print("------")
   
    answer = int(input("Enter your answer: "))
    if answer == num1 + num2:
        print("Congratulations! Your answer is correct.")
    else:
        print("Sorry, the correct answer is:", num1 + num2)
    
if __name__ == '__main__':
    math_quiz()