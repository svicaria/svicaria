USD = input('¿Ingrese los USD que desea convertir? ')
USD = float(USD)
TRM = 3768
COP = USD*TRM
COP = round(COP, 1)
COP = str(COP)
print('Tendrías $ '+ COP + ' Pesos colombianos')