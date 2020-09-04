
rerun = 'yes'
while rerun == 'yes':

	principal_amount = float(input("Enter total cost: "))
	token_amount = int(input("Enter number of assets: "))
	desired_average = float(input("Enter desired average cost: "))
	monetary_force = float(input("how much to put down to reach that cost: "))

	p = principal_amount
	t = token_amount
	d = desired_average
	m = monetary_force
	
	PriceAvg = (m/(((p+m)-(t*d))/d))*0.99 #*0.99 is the comission charged by the exchange, (%1), here you may enter the commission charged by your exchange
	print()
	print("{:.2f} EUR".format(PriceAvg))
	
	print("If the cost is too low, try inputting a higher amount to put down or vice a versa")

	rerun = input("\n would you like to run another calculation?[yes/no] ")
