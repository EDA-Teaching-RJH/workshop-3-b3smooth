import random
truefalse = False
secret_number = random.randint(1,10)
print(secret_number)
while truefalse==False:
    UInput = int(input("Please input a new number"))
    if(UInput==secret_number):
        print("just right")
        truefalse=True
    elif(UInput>secret_number):
        print("Too high")
    else:
        print("Too low")




