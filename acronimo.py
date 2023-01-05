import re
text = input('Ingrese el nombre de la organización de la que quiere obtener el acronimo: ')
acro = ''
for palabra in text.split(' '):
    if not re.search('[a-z]', palabra[0]):
        acro += palabra[0]
print(f'El acronimo de la organización "{text}" es: {acro}')
