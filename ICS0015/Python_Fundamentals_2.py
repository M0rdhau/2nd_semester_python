import math
import time
import webbrowser

def subtractor():
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    difference = 0
    if a > b:
        difference = a - b
    else:
        difference = b - a

    print('Difference is: ' + str(difference))

def grader():
    grade = int(input('Enter your grade: '))
    gradedGrade = ''
    if(grade < 50):
        gradedGrade = 'Fail'
    elif(grade < 59):
        gradedGrade = 'D'
    elif (grade < 69):
        gradedGrade = 'C'
    elif (grade < 79):
        gradedGrade = 'B'
    elif (grade < 89):
        gradedGrade = 'A'
    else:
        gradedGrade = 'A+'
    print('Your grade is: ' + gradedGrade)

def divisors():
    numberToDivide = int(input('Enter the number: '))
    # number won't have a divisor bigger than its half
    floored = math.floor(numberToDivide/2)
    for i in range(1, floored + 1):
        if numberToDivide % i == 0:
            print(str(i) + ' Is a divisor of ' + str(numberToDivide))

def findOdd():
    numberRange = int(input('Enter the number: '))
    for i in range(1, numberRange + 1):
        if i % 2 == 1:
            print(str(i))

def favSite():
    site = input('Enter your favorite website: ')
    timeStart = time.time()
    totalTicks = 0
    while(totalTicks < 5):
        if ((timeStart - time.time()) % 5) == 0:
            webbrowser.open(site)
            totalTicks += 1

def fibonacci():
    maxNumber = int(input('Input number up to which we should go'))
    fibOne = 1
    fibTwo = 1
    print(str(fibOne))
    while(fibTwo < maxNumber):
        print(str(fibTwo))
        temp = fibTwo
        fibTwo = fibTwo + fibOne
        fibOne = temp

def initFunction():
    print('Which exercise would you like to try? \n 1. Compute difference \n 2. print grade' +
          ' \n 3. find all divisors of a number \n 4. Find all odd numbers in range \n' +
          '5.print your favorite site 5 times \n 6. print fibonacci sequence \n')
    exercNumber = int(input('Type the number. Type 0 if you\'d like to quit'))
    while(exercNumber != 0):
        if(exercNumber == 1):
            subtractor()
        elif(exercNumber == 2):
            grader()
        elif(exercNumber == 3):
            divisors()
        elif(exercNumber == 4):
            findOdd()
        elif(exercNumber == 5):
            favSite()
        elif(exercNumber == 6):
            fibonacci()
        else:
            print('Wrong number!')
        exercNumber = int(input('Type a new number(1-6). Type 0 if you\'d like to quit'))
    print('Bye!')
    return

initFunction()