lights = ["red","green","yellow"]

print("1 for red\n2 for green\n3 for yellow")
choise = int(input("enter traffic light color : "))

if choise == 1:
    print(f"{lights[0]} : stop you can't go")
    
elif choise == 2 :
    print(f"{lights[1]} : you can go now")
    
elif choise == 3 :
    print(f"{lights[2]} : wait for some seconds")
    
else:
    print("wrong light colour")