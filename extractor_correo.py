# Recopile una dirección de correo electrónico del usuario y luego averigüe si el usuario tiene un nombre de dominio personalizado o un nombre de dominio popular. Por ejemplo
# Recopilamos una dirección de correo electrónico del usuario y luego vamos a averiguar si ese email tiene nombre de dominio personalizado o un nombre de un dominio popular. Por ejemplo:

correo = ''
while len(correo) != 2:
    correo = input('Ingrese por favor su correo: ').split('@')

dominio = correo[1]
dominio = dominio.replace('.com','').replace('.mx','').replace('.gob','')
if dominio in ['yahoo','gmail','hotmail','outlook']:
    print(f'Hola {correo[0].title()}, estoy viendo que tu email está registrado con {dominio.title()}. ¡Eso es genial!')
else:
    print(f'Hola {correo[0].title()}, estoy observando que estás utilizando un dominio personalizado de {dominio.title()}. ¡Impresionante!.')
