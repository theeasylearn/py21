# cards game 
from random import *

# Suits and ranks
suits = ["♥", "♦", "♣", "♠"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# cards = {1: '2 ♥', 2: '3 ♥', 3: '4 ♥', 4: '5 ♥', 5: '6 ♥', 6: '7 ♥', 7: '8 ♥', 8: '9 ♥', 9: '10 ♥', 10: 'J ♥', 11: 'Q ♥', 12: 'K ♥', 13: 'A ♥', 14: '2 ♦', 15: '3 ♦', 16: '4 ♦', 17: '5 ♦', 18: '6 ♦', 19: '7 ♦', 20: '8 ♦', 21: '9 ♦', 22: '10 ♦', 23: 'J ♦', 24: 'Q ♦', 25: 'K ♦', 26: 'A ♦', 27: '2 ♣', 28: '3 ♣', 29: '4 ♣', 30: '5 ♣', 31: '6 ♣', 32: '7 ♣', 33: '8 ♣', 34: '9 ♣', 35: '10 ♣', 36: 'J ♣', 37: 'Q ♣', 38: 'K ♣', 39: 'A ♣', 40: '2 ♠', 41: '3 ♠', 42: '4 ♠', 43: '5 ♠', 44: '6 ♠', 45: '7 ♠', 46: '8 ♠', 47: '9 ♠', 48: '10 ♠', 49: 'J ♠', 50: 'Q ♠', 51: 'K ♠', 52: 'A ♠'}

# Generate the deck dictionary
cards = {}
numbers = []
priority = 1
for i in suits:
    for j in ranks:
        cards[priority] = f"{j} {i}"
        priority += 1

# print(cards)
user1 = sample(list(cards.values()),3)
user2 = sample(list(cards.values()),3)
print(f"user1 : {user1}      user2 : {user2}")
user1 = "".join(user1)
l1=[]
l1.append(user1[0])
l1.append(user1[3])
l1.append(user1[6])
# print(l1)

l1.sort()
print(l1)

result1 = 0
result2 = 0
if  (l1[0] == (l1[1] or l1[2])) or (l1[1] == (l1[0] or l1[2])) or (l1[2] == (l1[1] or l1[0])):
    result1 = "pair"
    

else:
    result1="high card"
    
print(result1)