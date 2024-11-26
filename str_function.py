l1 = ["a","b","c","d"]

# join
print("-".join(l1))

symbol = input("enter symbol : ")
symbol = f" {symbol} "
print(symbol .join(l1))

# replace
text = "hello world world world world"
rt = text.replace("world","user")
print(rt)

rt = text.replace("h","H")
print(rt)

rt = text.replace("world","user",2)
print(rt)

# split
text = "hello world"
st = text.split()  # output in list
print(st)

text = "1+2+3+4+5+6+7+8+9+0"
st =text.split("+")
print(st)

st= text.split("+",3)
print(st)

st=text.split("4",4)
print(st)

text = "<<>><<>><<>>"
st = text.split("<")
print(st)