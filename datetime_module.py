from datetime import *

today = date.today()
print(today)

while True:
    now = datetime.now()
    print("\033[H\033[J", end="")
    print(f" {now.hour} : {now.minute} : {now.second}")