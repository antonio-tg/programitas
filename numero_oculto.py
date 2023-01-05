# Esta programa se trata de que el usuario adivine un numero entre el 1 y 50
from random import randint

numero_oculto = randint(1,50)
#print(numero_oculto) #solo para hacer pruebas
print('Vamos a jugar a adivinar el número oculto, el rango es [1,50]')
n = 0
numeu = ''
while numero_oculto != numeu:
    n += 1
    try:
        numeu = int(input('Ingrese su pronostico: '))
    except:
        print('Su elección no es valida, intente de nuevo')
    if numeu not in range(1,51):
        print('El número ingresado no pertenece al rango [1,50]')
print(f'Ah adivinado el número en {n} intentos')
