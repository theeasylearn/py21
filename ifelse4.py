# bmi calculator

weight = float(input("enter weight in kg : "))
height = float(input("enter height in cm : "))

height = height/100

bmi = weight / (height**2)
print(round(bmi,2))

if bmi<=18.5:
    print("under weight")
    
else:
    # 18.5 - 24.9``
    if bmi>=18.5 and bmi<=24.9:
        print("normal weight")
        
    else:
        # 25–29.9
        if bmi>=25 and bmi<=29.9:
            print("overweight")
            
        else:
            print("obesity")
