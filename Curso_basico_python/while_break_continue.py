#Este ejercicio es realizado por Santiago Vicaría, el ojbetivo es usar los comandos break y continue dentro de un while

def run():
    limite = int(input('Ingresa un valor: '))
    while limite < 100:
        print(limite)
        limite = limite + 1
        if limite > 90:
            break
        if limite % 2 != 0:
            continue
    print('Se esta finalizando el codigo')

    


if __name__ == '__main__':
    run()
