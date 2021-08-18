while True:
    g = input("Welcome to the tool of everything please enter what you want: P.S. you can ask what is available: ")
    if g == "what is available":
        print('''Thank you for asking. Here is the list:
Type a if you want Age of our family
Type c if you want Calculator
Type ca if you want Calendar
Even or odd number behind your number
            Fruites and Veggies
            Numberworks
            Temperature converter
            Triangle
            ''')
    elif g == "Age of our family":
        import AgeofourFamily
    elif g == "Calculator":
        import Calculator
    elif g == "Calendar":
        import Calendar
    elif g == "Even or odd number behind your number":
        import Evenoroddnumberbehindyournumber
    elif g == "Fruits and veggies":
        import FruitesandVeggies
    elif g == "Numberworks":
        import Numberworks
    elif g == "Temprature converter":
        import Tempratureconverter
    elif g == "Triangle":
        import Triangle
    else:
        print("Invalid")

    v = input("do you want to ask something else: ")
    if v == "yes":
        pass
    else:
        break   