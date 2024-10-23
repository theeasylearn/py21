#empty dictionary
movie = {}
print(movie)
movie['name'] = 'Singham'
movie['duration'] = 150
movie['generation'] = 'Action'

print(movie)
#adding list in dictionary
movie['starcast'] = ['Ajay Devgan','Karina kapoor','others']
movie['part'] = (1,2,3) #adding tuple in dictionary
print(movie)
#first star name
print(movie['starcast'][0])
