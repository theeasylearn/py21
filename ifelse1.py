'''
    write a program to accept  production price and sales price of product from user. display profit or loss with message.
    step 
    accept product price
    accept sales price
    create variable to store difference between product price and sales price.
    if difference is positive then display difference as profit
    else display difference as loss
'''
production_price = input("Enter production price")
production_price = int(production_price)

sales_price = input("Enter sales price")
sales_price = int(sales_price)

difference = sales_price - production_price

if difference>0: # == != < > <= >=
    print(f"profit is {difference}")
else:
    print(f"loss is {difference}")

print("good bye")