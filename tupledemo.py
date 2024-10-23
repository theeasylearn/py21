#example of tuple
gods = ('Bramha','Vishnu','Mahesh(shiv)')
print(gods)
print(gods[0])
print(gods[1:])
# gods[0] = 'Lord Bramha' # wont work because we can not change tuple as it is read only (immutable)
temp = gods.count('Bramha')
print("count of brama " + str(temp))

position = gods.index('Vishnu')
print("position of Vishnu " + str(position))


