def even(a):
	a = int(input('Gimme your first number please:'))
	for y in range(a):
		if (y+1) % 2==0:	
			print(y+1)

def odd(g):
	g = int(input('Gimme your first number please:'))
	for y in range(g):
		if (y+1) % 2==1:	
			print(y+1)

def cordinate(h):
	if h == "odd":
		call = odd(h)
	elif h == "even":
		call = even(h)
	else:
		print("not valid")

s = input("please give your operator: even or odd: ")
cordinate(s)