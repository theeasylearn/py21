''''
write a program to find out whether given year is leap year or not
for understanding refer 
https://www.wikihow.com/Calculate-Leap-Years
step 1
    accept year from user
    then findout reminder of by dividing year by 4 then store it in reminder1
    then findout reminder of by dividing year by 100 then store it in reminder2
    then findout reminder of by dividing year by 400 then store it in reminder3
    if reminder1 is zero and reminder 2 is not zero
        display message given year is leap year
    otherwise 
        if reminder2 is zero and reminder3 is zero 
            display message given year is leap year
        otherwise not leap year
'''
year = input("Enter year to check is it leap year or not")
year = int(year)
reminder1 = year%4
reminder2 = year%100
reminder3 = year%400
if reminder1==0 and reminder2!=0: # < > <= >= == !=
    print("given year is leap year")
else:
    if reminder2==0 and reminder3==0: # < > <= >= == !=
        print("given year is leap year")
    else: 
        print("given year is not leap year")

    
