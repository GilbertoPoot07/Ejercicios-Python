
def funcion1(num):
	for num in range(13, 32):
		if num % 2 != 0:
			print (num)	
	return num


num1=int(raw_input("Escribe un numero: "))

print funcion1(num1)
