# logical operator
# and or not

# a=1
# b=1
# c=2

a,b,c = 1,1,2

# or - when any one condtion become trure it returns true else it returns false
print(a==10 or b==0)
print(a==10 or b==2 or c==20)

# and - when all conditions are true it returns ture else it returns false

print(a>b and a>c)
print(a==b and a!=c and b<c)
print(a==b and a!=c and b>c)
print(a!=b and a==c and c>b)

# not - reverse the output
print(not(a==b))
print(not(a!=b))
print(not(a>c or b==a or c<=b))
print(not(a==c and b==a and c>a))


a=10
b=20
c=10

answer = not((a>10 or b<20) and (c>=10 or a==c))
            # false      and         true
            
print(answer)

# "10"==10 false
# a=10 a="10"
print(((str(a)==str(b)) or (str(a)!=c and a>c)) and not((float(a) == b/2 and c==c**1)))
            # False       or         False                    True          True
                        # False               and                      false