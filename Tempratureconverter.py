def ftoc(x):
    return (x - 32) * 5/9
def ctof(x):
    return (x * 9/5) + 32

def inp(to,t):
    if to == "f":
        return ctof(t)
    elif to == "c":
        return ftoc(t)
    else:
        print("not valid")    

z = input("what do you want to get i.e c or f: ")
v = int(input("give me you temperature:"))
value = inp(z,v)
print(value)
    