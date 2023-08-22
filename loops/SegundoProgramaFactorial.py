while True:
    value = int(input("Enter a positive integer value:"))
    print("value:", value)
    a = issinstance(value, int)
    if a == True and value > 0:
        fact == 1
        for i in range (1, value + 1):
            fact = fact*i
            print (f"The factorial of {value} is: ", fact)
    else:
        print ("Please, enter a positive integer number")
