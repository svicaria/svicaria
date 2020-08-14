menu = """
Bienvenido al conversor de monedas 😁

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = input(menu)

if opcion == "1":
    pesos = input("¿Cuántos pesos colombianos tienes?: ")
    pesos = float(pesos)
    TRM = 3768
    USD = pesos / TRM
    USD = round(USD, 2)
    USD = str(USD)
    print("Tienes $" + USD + " dólares")
elif opcion == "2":
    pesos = input("¿Cuántos pesos argentinos tienes?: ")
    pesos = float(pesos)
    TRM = 73.16
    USD = pesos / TRM
    USD = round(USD, 2)
    USD = str(USD)
    print("Tienes $" + USD + " dólares")
elif opcion == "3":
    pesos = input("¿Cuántos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    TRM = 21.97
    USD = pesos / TRM
    USD = round(USD, 2)
    USD = str(USD)
    print("Tienes $" + USD + " dólares")
else:
    print("Ingresa una opción correcta porfavor.")
    


