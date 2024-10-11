TF= False
while TF==False:
    U1=float(input("Please enter in your first number "))
    U2= float(input("Please enter in your second number "))
    UOperator=input("Please enter in an operator ")
    match UOperator:
        case "+":
            Result = U1 + U2
            print(f"{U1} + {U2} = {Result}")
        case "-":
            Result = U1-U2
            print(f"{U1} - {U2} = {Result}")
        case "*":
            Result = U1*U2
            print(f"{U1} * {U2} = {Result}")
        case "/":
            if(U1!=0 and U2!=0):
                Result = U1/U2
                print(f"{U1} * {U2} = {Result}")
            else:
                print("this is a divide by 0 error")
        case "^":
            Result = U1**U2
            print(f"{U1} ^ {U2} = {Result}")
        case "%":
            Result = U1%U2
            print(f"{U1} % {U2} = {Result}")
        case "quit":
            print("The application is ending")
            TF=True
            break



