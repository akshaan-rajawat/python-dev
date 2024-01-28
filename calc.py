def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1//n2
operation = {
 "+":add,
 "-":sub,
 "*":multiply,
 "/":divide
 }
yesno=True
while yesno==True:
    num1=int(input("Enter the first number "))
    num2=int(input("Enter the second number "))
    print("Pick an operation")
    for symbol in operation:
        print(symbol)
    user_opp=input()   
    answer = operation[user_opp](num1,num2)
    print(f"{num1} {user_opp} {num2} = {answer}")
    answer=input(print("Do you want to continue y or n "))
    if answer.lower()=="n":
        yesno=False