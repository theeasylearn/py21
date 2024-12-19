# write a program that reverse a string
# python -> nohtyp

text = input("enter a string : ")

last_position = len(text)-1
# print(last_position)

for i in range(last_position,-1,-1):
    print(text[i],end="")


# print(text[last_position],end="")

# last_position -= 1

# print(text[last_position],end="")

# last_position -= 1

# print(text[last_position],end="")

# last_position -= 1

# print(text[last_position],end="")