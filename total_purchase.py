print("Welcome to Supermarket.")
item_1 = float(input("Enter the price of first item : "))
item_2 = float(input("Enter the price of second item : "))
item_3 = float(input("Enter the price of third item : "))
item_4 = float(input("Enter the price of fourth item : "))
item_5 = float(input("Enter the price of fifth item : "))

sub_total = item_1 + item_2 + item_3 + item_4 + item_5

sales_tax = 0.07 * sub_total

total = sub_total + sales_tax

print( "Sub total :Rs" + format( sub_total , ",.2f") , "Sales tax :Rs" + format( sales_tax , ",.2f") , "Total :Rs" + format( total , ",.2f") , sep ="\n")
