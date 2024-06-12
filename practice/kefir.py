def kefir():
    crystal = float(input("Enter crystal weight: "))
    sugar = (4*crystal)/5
    water = 20*crystal
    print (f'{sugar}g sugar\n{water}ml water')

    while True:
        divide = str(input("Divide by 2?"))
        if divide == "Yes"or divide == "yes":
            print ((f'{sugar/2}g sugar\n{water/2}ml water'))
            break
        elif divide == "No" or divide == "no":
            print ("Okay then.")
            break
        print ("It's a 'yes' or 'no' question")

kefir()
