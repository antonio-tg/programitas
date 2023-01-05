# Este programa le pide una palabra al usuario y le dice si es palindromo
from colores import colores

palabras = input('Escriba cinco palabras separadas por una coma: ').replace(' ','').split(',')
while len(palabras) != 5:
    palabras = input('La lista de palabras no tiene la longitud solicitada, intente de nuevo: ').replace(' ','').split(',')
for palabra in palabras:
    p1 = palabra.lower()
    p2 = p1[::-1]
    if p1 == p2:
        print(f'La palabra {colores.negritas(colores.verde(palabra))} es un palindromo')
    else:
        print(f'La palabra {colores.negritas(colores.rojo(palabra))} no es un palindromo')

        #print(f'Este texto debería ser {colores.negritas(colores.amarillo("amarillo"))}!!')
