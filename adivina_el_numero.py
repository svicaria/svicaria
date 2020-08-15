import random


def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input('Voy a elegir un número al azar del 1 al 100, escribe un número del 1 al 100 para saber si adivinaste: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('El número es más grande')
        else:
            print('El número es mas pequeño')
        numero_elegido = int(input('Elige otro número: '))
    print('¡Ganaste!')

if __name__ == '__main__':
    run()
