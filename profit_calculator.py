#write a program to findout profit from given sales price and production price
'''
    take sales price and production price from user 
    calculate profit by sales price - production price 
    display profit
'''
sales_price = input("Enter sales price ")
production_price = input("Enter product price")

sales_price = float(sales_price)
production_price = float(production_price)
profit = sales_price - production_price
print("profit = " + str(profit))