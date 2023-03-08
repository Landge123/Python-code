
def printValue(digit):

    if digit == '0':
        print("Zero ", end = " ")

    elif digit == '1':
        print("One ", end = " ")

    elif digit == '2':
        print("Two ", end = " ")

    elif digit=='3':
        print("Three",end=" ")

    elif digit == '4':
        print("Four ", end = " ")

    elif digit == '5':
        print("Five ", end = " ")

    elif digit == '6':
        print("Six ", end = " ")

    # For digit 7
    elif digit == '7':
        print("Seven", end = " ")

    # For digit 8
    elif digit == '8':
        print("Eight", end = " ")

    # For digit 9
    elif digit == '9':
        print("Nine ", end = " ")

def printWord(N):
    i = 0
    length = len(N)


    while i < length:


        printValue(N[i])
        i += 1

N = "1234"
printWord(N)
