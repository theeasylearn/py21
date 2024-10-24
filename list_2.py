'''
append()  
	Add an element to the end of the list    
extend(list)  
	Add  set of values(list) at the end of list. 
insert(position,item)  
	Insert an item at the defined position    
remove(item)  
	Removes given item from the list    
pop(position)  
	Removes and returns an element at the given position
clear()  
	Removes all items from the list    
index()  
	Returns the index of the first matched item    
count(item)  
	Returns the count of the number of items passed as an argument    
sort()  
	Sort items in a list in ascending order if all items are of same type    
reverse()  
	Reverse the order of items in the list    
copy()  
	Returns a shallow copy of the list
'''
fruits = ['mango','pinapple','apple','cherry','kiwi','apple']
print(fruits)
#add new item at the end of list 
fruits.append('banana')
#add new item at the begining of list 
fruits.insert(0,'orange')
print('after add items into fruits')
print(fruits)
#remove item cherry from list
fruits.remove('cherry')

#remove 0th(1st item for us) item
fruits.pop(0)
print('after removing items from fruits')
print(fruits)

#count no of apples
no_of_apples = fruits.count('apple')
print("no of apples = " + str(no_of_apples))
first_apple = fruits.index('apple')
print("1st apple position = " + str(first_apple))
fruits.sort()
print("sorted list ")
print(fruits)
fruits.reverse()
print("reversed list ")
print(fruits)
# fruits2 = fruits #store reference of fruit into fruits2 (both are same) if you change one other will change (wrong way)
fruits2 = fruits.copy()
print('before clear')
print(fruits)
print(fruits2)
fruits2.clear()
print('after clear')
print(fruits)
print(fruits2)
vegis = ['potato','onion','tomato']
fruits.extend(vegis)
print('after merging fruits with vegis')
print(fruits)
size = len(fruits)
print("size of the fruits  " + str(size))