def grossPay():
    hours = int(input('Enter hours: '))
    rate = int(input('Enter rate: '))
    print('Pay: ', rate*hours)
    return

def bottlesOfBeer():
    howManyBeers = int(input('How many beers on the wall?'))
    for x in range(howManyBeers):
        bottlesPlural = 'bottles'
        if(howManyBeers - (x) == 1):
            bottlesPlural = 'bottle'
        print(str(howManyBeers - x) + ' '+bottlesPlural+' of beer on the wall, ' + str(howManyBeers - x) + ' '+bottlesPlural+' of beer')
        if(howManyBeers - (x+1) == 0):
            print('Take one down and pass it around, no more bottles of beer on the wall')
            print('No more bottles of beer on the wall, no more bottles of beer ')
            print('Go to the store and buy some more, '+ str(howManyBeers) +' bottles of beer on the wall ')
        else:
            if(howManyBeers - (x+1) == 1):
                bottlesPlural = 'bottle'
            print('Take one down and pass it around, ' + str(howManyBeers - (x + 1)) + ' '+bottlesPlural+' of beer on the wall')
    return

def addNumbers():
    maxNumber = int(input('up to what number should we add numbers?'))
    totalNumber = 0
    for x in range (1, maxNumber + 1):
        totalNumber += x
    print('Total number is: ' + str(totalNumber))
    return

def factorial():
    upTo = int(input('Factorial of what number would you like to know?'))
    totalFactorial = 1
    for x in range (1, upTo + 1):
        totalFactorial *= x
    print('Factorial is: ' + str(totalFactorial))
    return

def initFunction():
    print('Which exercise would you like to try? \n 1. Compute pay \n 2. Bottles of beer \n 3. Adding numbers \n 4. Factorial calculator')
    exercNumber = int(input('Choose the number. Choose 0 if you\'d like to quit'))
    while(exercNumber != 0):
        if(exercNumber == 1):
            grossPay()
        elif(exercNumber == 2):
            bottlesOfBeer()
        elif(exercNumber == 3):
            addNumbers()
        elif(exercNumber == 4):
            factorial()
        else:
            print('Wrong number!')
        exercNumber = int(input('Choose a new number(1-4). Choose 0 if you\'d like to quit'))
    print('Bye!')
    return

initFunction()