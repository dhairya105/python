def rangeofno(x):
	x = int(input('Give me your number please:'))
	for y in range(x):
		print(y+1)

def Addofallnobehindyourno(x):
	x = int(input("give me a number: "))
	x = x * (x + 1) / 2
	print(x)

def comparerange25(x):
	x= int(input("Gimme your number please:"))
	if x<5:
		print("I am smaller than 5")
	elif x<10:
		print("I am smaller than 10")
	elif x<15:
		print("I am smaller than 15")
	elif x<20:
		print("I am smaller than 20")
	elif x<25:
		print("I am smaller than 25")
	else:
		print("I am greater than 25")

def compare(x,y):
	x = int(input("Give me your first number: "))
	y = int(input("Give me your second number: "))
	if x>y:
		 print(x, "is greater than", y)
	elif x<y:
		 print(x, "is less than", y)
	else:
		print("They are equal")	 	 

hf = input("what do you want: ")
g = 0
if hf =="range":
	c=rangeofno(hf)
	print(rangeofno)
elif hf == "addition":
	c=Addofallnobehindyourno(hf)
	print(c)	
elif hf == "compare with range of 25":
	c=comparerange25(hf, d)
	print(c)
elif hf == "compare":
	c=compare(hf, g)
	print(c)	
else:
	print("not valid")	