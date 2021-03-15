def problemone():
    def bmicalculator(bmi):
        if bmi < 18.5:
            bmi_string = 'Underweight'
        elif bmi < 24.9:
            bmi_string = 'Normal'
        elif bmi < 29.9:
            bmi_string = 'Overweight'
        else:
            bmi_string = 'Obese'
        return bmi_string

    bmi_input = int(input('Enter your bmi: '))
    print('Your category is: ' + bmicalculator(bmi_input))

def problemtwo():
    def pelCalculator(n):
        if n <= 1:
            return n
        else:
            return pelCalculator(n-2) + pelCalculator(n-1)*2

    pelNum = int(input('Enter the index of a pell number: '))
    if pelNum <=0:
        print('please enter a positive integer')
    else:
        print('Pell Numbers')
        for i in range (pelNum+1):
            print(pelCalculator(i))

def initFunction():
    print('Which exercise would you like to try? \n 1. BMI calculator \n 2. Pell number calculator\n')
    exercNumber = int(input('Type the number. Type 0 if you\'d like to quit'))
    while(exercNumber != 0):
        if(exercNumber == 1):
            problemone()
        elif(exercNumber == 2):
            problemtwo()
        else:
            print('Wrong number!')
        exercNumber = int(input('Type a new number(1-2). Type 0 if you\'d like to quit'))
    print('Bye!')
    return

initFunction()