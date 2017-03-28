
import math

def funcion1(radio):
	resultado = (4*(math.pi)*(radio*radio*radio))/3
	return (resultado)

num1=float(raw_input("Ingresa el Radio: "))

print 'El Volumen De La Esfera Es: '
print funcion1(num1)
