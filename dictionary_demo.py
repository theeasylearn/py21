#example of dictionary 
course = {'name':'Python','duration':90,'fees':7500.99,'isCertified':True}
print(course)
#add new key 
course['trainer'] = "Ankit Patel"

#update value
course['duration'] = 75
print(course)

#delete key value pair 
del course['duration']

size = len(course)
print(course)
print("size of the course = " + str(size))
#delete dictionary 
del course 

print(course)