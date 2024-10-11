STS=int(input("Please enter in a students score "))
match STS:
    case STS if STS<0 or STS>100:
        print("Invalid Number")
    case STS if 90<=STS<=100:
        print("A")
    case STS if 80<= STS<=89:
        print("B")
    case STS if 70<= STS<=79:
        print("C")
    case STS if 60<= STS <=69:
        print("D")
    case STS if STS<60:
        print("F")
