course = {'name':'Python','duration':90,'fees':7500.99,'isCertified':True}
print(course)

#get only values 
print(course.values())

#get only keys
print(course.keys())

details = ['name','surname','age','gender']
print(details)

#create dictionary using list 
harsh = dict.fromkeys(details,'')
print(harsh)

jay = dict.fromkeys(details,'')
print(jay)

#update value using keys
harsh['name'] = "Harshrajsinh"
harsh['surname'] = "zala"
harsh['age'] = 21
harsh['gender'] = True
harsh['country'] = 'bharat'

print(harsh)

jay.update({'name':'jay'})
jay.update({'surname':'langaliya'})
jay.update({'age':42})
jay.update({'gender':True})
jay.update({'country':'india'}) #add new key 

print(jay)