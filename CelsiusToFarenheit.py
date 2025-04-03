while True:
    try:
        TempInC = float(input("Input a temperature in degrees celsius: "))
        break
    except:
        print("You must input a number")
        print("please try again\n")

TempInF = TempInC * 9/5 + 32

print(f"{TempInC:.1f} degrees celsius is {TempInF:.1f} degrees Farenheit")