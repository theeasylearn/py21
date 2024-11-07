l1 = [10,20,30,40,50,50,20]
print(l1)

#unordered
#unique
color = {"red","green","green","blue","black","red"}
print(color)

number = set(l1) #converting list to set
print(number)

# add element to set
number.add(80)
print(number)
print(type(number))

# remove element from set
number.remove(20)
print(number)

color = list(color)
print(color)
print(type(color))

print("-"*100)
#set operations 

#unioun - unique
s1 = {100,200,300,400}
s2 = {500,400,600,800,200}
print(s1.union(s2))
unique = s2.union(s1)
print(unique)

print("\n")

#intersection - comman value
print(s1.intersection(s2))
print(s2.intersection(s1))

#difference - set1 - set2
print(s1.difference(s2))
print(s2.difference(s1))
