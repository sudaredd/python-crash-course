print("Give me two numbers, I will divid them")
print("Enter q to quit")
while True:
    num1 = input("enter first number:")
    if(num1 == 'q'):
        break
    num2 = input ("enter second number:")
    if(num2 == 'q'):
        break
    try:
        answer = int(num1)/int(num2)
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print("result is "+str(answer))
