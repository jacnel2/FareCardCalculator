#This little program calculates the minimum even amount you can load to a farecard.
def calculateLoadAmount(count, amount):
    while True :
        calcResult = count / amount
        if (calcResult.is_integer()):
            print ('\033[96m' + "Load $" + str(count) + " for " + str(calcResult) + " trips")
            break
        else:
            count += 1
    
while True:
    print('\033[0m' + "****FARECARD FUNDS CALCULATOR****")
    print("\tEnter the minimum amount that can be loaded to the card, followed by the fare cost per trip.")
    print("\tThis program will then calculate the minimum EVEN dollar amount you can load to the card as well as the number of trips that amount will pay for.")
    minAmount = input("Enter the minimum load value or q to exit:")
    if minAmount == 'q':
        break;
    fare = input("Enter the fare amount:")
    try:
        calculateLoadAmount(int(minAmount), float(fare))
    except ValueError:
        print('\033[41m' + "ERROR: Enter a whole number for the minimum load amount and a number for the fare amount" + '\033[0m')