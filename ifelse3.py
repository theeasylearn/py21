maths = int(input("enter math marks : "))
english = int(input("enter english marks : "))
science = int(input("enter science marks : "))

if (maths>100 or maths<0) or (english>100 or english<0) or (science>100 or science<0):
    print("error : given marks are not valid")

else:
    percentage = (maths+english+science) /3
    print(f"percentage : {round(percentage,2)}%")
    
    if percentage>=40:
        print("status : pass")
        
        if percentage>=80 and percentage<=100:
            print("gard : A")
        
        if percentage>=60 and percentage<80:
            print("grad : B")
            
        if percentage>=40 and percentage<60:
            print("grad : c")
            
    else:
        print("status : fail")