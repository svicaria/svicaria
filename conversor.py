pesos = input("¿Cuántos pesos colombianos tienes?: ")
pesos = float(pesos)
TRM = 3768
USD = pesos / TRM
USD = round(USD, 2)
USD = str(USD)
print("Tienes $" + USD + " dólares")