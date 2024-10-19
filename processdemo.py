#example of how to process data
#write a program to make addition subtraction, multiplication and division of given 2 numbers and show them
'''
   input of two number
   addition subtraction, multiplication and division of these two number
   output of addition subtraction, multiplication and division 
'''
#input
num1 = input("Enter 1st number")
num2 = input("Enter 2nd number")
#we can not do any mathematical operation on string so we have to convert variable into integer(number)


#process
num1 = int(num1)
num2 = int(num2)

#samikaran (expression)
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

#output
print("addition = " + str(add))
print("subtraction =" + str(sub))
print("multiplication =" + str(mul))
print("division =" + str(div))
