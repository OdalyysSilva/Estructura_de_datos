print("Calculadora Simple")

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
operador = input("Ingrese un operador (+, -, *, /): ")

if operador == '+':
    resultado = num1 + num2
    print("Resultado: ", resultado)
elif operador == '-':
    resultado = num1 - num2
    print("Resultado: ", resultado)
elif operador == '*':
    resultado = num1 * num2
    print("Resultado: ", resultado)
elif operador == '/':
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado: ", resultado)
    else:
        print("Error: No se puede dividir por cero.")
else:
    print("Operador no valido")
