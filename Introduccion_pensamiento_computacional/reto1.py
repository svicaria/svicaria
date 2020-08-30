def main():
    nombre= str(input('Escribe tu nombre: '))
    print(f'Hola {nombre} , bienvenido a este programa')
    lenght = len(nombre)
    print(f'Tu nombre tiene {lenght} letras')
    print('Fin del programa')

if __name__ == "__main__":
    main()