# userdefine module
# 1) import filename
# -> it import all containt in module
# import module_maths
import module_maths as m  #give alias to module name

print(m.name)
m.add()

m.multiplication()


# 2) from module name import  variable,fun,class 
# -> it import spesific containt in module

# from module_maths import name
# from module_maths import add,name
from module_maths import *

add()
print(name)
multiplication()


import sys
for i in sys.path:
    print(i)
