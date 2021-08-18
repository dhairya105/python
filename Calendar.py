months = ["January","February","March","April","May","June","July","Aust","September","October","November","December"]
number_of_days_in_month  =[31,28,31,30,31,30,31,31,30,31,30,31]
year = int(input("Gimme your year:"))
month = input("Gimme your month:")
no_of_days_in_year=365
month_index= months.index(month)
no_of_days = number_of_days_in_month[month_index]
if year %4==0:
	no_of_days_in_year=366
	if month_index ==1:
		no_of_days =no_of_days+1
	print("The year",year, " has ",no_of_days_in_year, " days and the month of",month," has",no_of_days, "days")