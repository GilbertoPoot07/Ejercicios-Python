import math
def fun1(a,b):
	c=math.sqrt((a*a+b*b))
	return (str(c))

num1=float(input("Ingrese un numero "))
num2=float(input("Ingrese un numero "))

print "El resultado es:"
print fun1(num1,num2)