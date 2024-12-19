# write program that generate table between range
start = int(input("enter starting number : "))
end = int(input("enter ending number : "))

# 1 x 1 = 1

for j in range(start,end+1):
    print(f"-------------table of {j}--------------")
    for i in range(1,11):
        print(f"{j} x {i} = {j*i}")
    

# for i in range(1,11):
#     print(f"{start} x {i} = {start*i}")
    
# start+=1

# for i in range(1,11):
#     print(f"{start} x {i} = {start*i}")
    
# start+=1

# for i in range(1,11):
#     print(f"{start} x {i} = {start*i}")
    
