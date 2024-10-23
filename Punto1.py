#Escribir un programa que dado el ingreso de un numero retorne si el mismo es primo o no.

numero = int(input("Ingrese un numero "))
es_primo= True

if numero <= 1:
    es_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
        
if es_primo:
    print ( str(numero) + " es un numero primo ")
else:
    print(str(numero) + " no es un numero primo ")
    




