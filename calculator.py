print("this is calculator")
while True:
    print("enter 1 to do additon")
    print("enter 2 to do subtraction")
    print("enter 3 to do multiplication")
    print("enter 4 to do division")
    print("enter 0 to exit")
    num = eval(input("enter a number to do what ever you want = "))
    if num == 1:
        a , b = eval(input("enter two number seperated with comma = "))
        print (a+b)
        input("press enter to continue")
    elif num == 2:
        a , b = eval(input("enter two number seperated with comma = "))
        print (a-b)
        input("press enter to continue")
    elif num == 3:
        a , b = eval(input("enter two number seperated with comma = "))
        print (a*b)
        input("press enter to continue")
    elif num == 4:
        a , b = eval(input("enter two number seperated with comma = "))
        print (a/b)
        input("press enter to continue")
    elif num == 0:
        break
