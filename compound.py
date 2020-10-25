# Python program to find compound interest for given values. 

def compound_interest(principle, rate, time): 

	Amount = principle * (pow((1 + rate / 100), time)) 
	CI = Amount - principle 
	print("Compound interest is", CI) 

 
compound_interest(50000, 6.25, 5)  
