name=input("Enter your name: ")
name=name.upper()
print(f"Hello {name}! Welcome to our simple calculator.")
print("\n")
while True:
	print("What you want to do (+, -, *,/,%, // or **) : ")
	sign=input()
	num1=int(input("Enter first number: "))
	num2=int(input("Enter second number: "))
	if sign=="+":
		print(f"{num1} + {num2} =",num1+num2)
	elif sign=="-":
		print(f"{num1} - {num2} =",num1-num2)
	elif sign=="*":
		print(f"{num1} * {num2} =",num1*num2)
	elif sign=="/":
		print(f"{num1} / {num2} =",num1/num2)
	elif sign=="%":
		print(f"{num1} % {num2} =",num1 % num2)
	elif sign=="//":
		print(f"{num1} // {num2} =",num1//num2)
	elif sign=="**":
		print(f"{num1} ** {num2} =",num1 ** num2)
	else:
		print("Invalied input")
	print("\n")
	print("Do you want to countinue?")
	n1=input("Enter y/n: ")
	print("\n")
	if n1=="n":
		break
	else:
		continue
	