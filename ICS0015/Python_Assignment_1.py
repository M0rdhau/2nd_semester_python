
def sortints():
    print('Type five integers \n')
    arr = []
    for x in range (5):
        arr.append(int(input(str(x + 1) + ":")))
    print("Sorted ascending:")
    print(sorted(arr))
    print("Sorted descending:")
    print(sorted(arr, reverse=True))

def statistfloats():
    print('Type floating point values, zero and up. Enter a negative value to stop')
    arr = []
    flt = 0
    while(flt >= 0):
        flt = float(input("Float: "))
        if(flt >= 0): arr.append(flt)
    # sum = sum(arr)
    # avg = sum / len(arr)
    # min = min(sum)
    # max = max(sum)
    print("Sum is: " + str(sum(arr)))
    print("Average is: " + str(sum(arr) / len(arr)))
    print("Maximum is: " + str(max(arr)))
    print("Minimum is: " + str(min(arr)))

def initFunction():
    print('Which exercise would you like to try? \n 1. integer sorter \n 2. statistics generator\n')
    exercNumber = int(input('Type the number. Type 0 if you\'d like to quit\n'))
    while(exercNumber != 0):
        if(exercNumber == 1):
            sortints()
        elif(exercNumber == 2):
            statistfloats()
        else:
            print('Wrong number!')
        exercNumber = int(input('Type a new number(1-2). Type 0 if you\'d like to quit\n'))
    print('Bye!')
    return

initFunction()