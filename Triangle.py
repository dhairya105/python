def Pointdown(n, p):
	x  = int(input("Give me yournumber please:"))
	for y in range(x):
		for z in range(x-y):
			print(n, end=" ")
		print()

def Pointup(o, u):
	y = int(input("give me a number: "))
	for x in range(y+1):
		for z in range(x):
			print(o, end =" ")
		print("")
    		
def cordinator(f, a):
	if a == "up":
		bring = Pointup(f, a)
	elif a == "down":
		bring = Pointdown(f, a)
	else:
		print("not valid")	
	
g = input("Please enter the character that you want to make your triangle with: ")
b = input("Do you want to make your star pointing up or down: ")
run = cordinator(g, b)