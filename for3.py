# write a program that seprate odd and even numbers between given range
# 1...100 
# -> [1,3,5...99] 
# -> [2,4,6,...100]

# if n/2 == int(n/2):
#     print("even")
n = int(input("enter number : "))

even = []
odd = []

for i in range(1,n+1):
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
    
print(f"even numbers : {even}")
print(f"\nodd numbers : {odd}")
