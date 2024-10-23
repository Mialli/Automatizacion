#Ejercicio 2
#Escribir una función que dado el ingreso de 3 variables (a, b, c) retorne las raíces resultantes de una ecuación cuadrática.

import math

def calcular_raices(a, b, c):
    discriminante = b**2 - 4*a*c    
    print(discriminante)

    if discriminante < 0:
        return "No hay raíces reales."
    elif discriminante == 0:
        raiz = -b / (2 * a)
        return f"La raíz es: {raiz}"
    else:
        raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return f"Las raíces son: {raiz1} y {raiz2}"

a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

resultado = calcular_raices(a, b, c)
print(f"{resultado}")