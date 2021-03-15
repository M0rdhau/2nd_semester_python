import numpy as np
import matplotlib.pyplot as plt

def problemone():
    x = [1, 2, 3]
    y = [5, 9, 2]

    plt.plot(x, y, 'bo-')
    plt.title('My Graph')
    plt.ylabel('y-Axis')
    plt.xlabel('x-Axis')
    plt.show()

def problemtwo():
    x1 = [2, 5, 6]
    y1 = [1, 6, 8]

    x2 = [4, 7, 9]
    y2 = [9, 3, 4]

    plt.plot(x1, y1, 'bo-',
             x2, y2, 'r*:')
    plt.title('My Graph')
    plt.ylabel('y-Axis')
    plt.xlabel('x-Axis')
    plt.legend(['line1', 'line2'])
    plt.show()

def problemthree():
    people = ['Adam', 'Eve', 'Paul', 'Rassel', 'Kate', 'Peter']
    ages = [45, 25, 67, 70, 21, 34]
    plt.bar(range(len(people)), ages, tick_label=people)
    plt.show()

def initFunction():
    print('Which exercise would you like to try? \n 1. plot one graph \n 2. Plot two graphs \n 3. Plot people\'s ages \n')
    exercNumber = int(input('Choose the number. Choose 0 if you\'d like to quit'))
    while(exercNumber != 0):
        if(exercNumber == 1):
            problemone()
        elif(exercNumber == 2):
            problemtwo()
        elif(exercNumber == 3):
            problemthree()
        else:
            print('Wrong number!')
        exercNumber = int(input('Choose a new number(1-3). Choose 0 if you\'d like to quit'))
    print('Bye!')
    return

initFunction()