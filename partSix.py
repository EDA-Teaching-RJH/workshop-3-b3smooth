UAge= int(input("Please input in your age "))
UStu= input("are you a student yes/no ")
if (UAge<12 or UAge>65):
    print("£5")
elif (UAge>12 or UAge<65)and UStu=="yes":
    print("£8")
else:
    print("£10")
