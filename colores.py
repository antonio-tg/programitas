class colores:
    def morado(text):
        return f'\033[95m{text}\033[0m'
    def azul(text):
        return f'\033[94m{text}\033[0m'
    def cian(text):
        return f'\033[96m{text}\033[0m'
    def verde(text):
        return f'\033[92m{text}\033[0m'
    def amarillo(text):
        return f'\033[93m{text}\033[0m'
    def rojo(text):
        return f'\033[91m{text}\033[0m'
    def negritas(text):
        return f'\033[1m{text}\033[0m'
    def subrayado(text):
        return f'\033[4m{text}\033[0m'

#print(f'Este texto debería ser {colores.morado("morado")}!!')
#print(f'Este texto debería ser {colores.azul("azul")}!!')
#print(f'Este texto debería ser {colores.cian("cian")}!!')
#print(f'Este texto debería ser {colores.verde("verde")}!!')
#print(f'Este texto debería ser {colores.amarillo("amarillo")}!!')
#print(f'Este texto debería ser {colores.rojo("rojo")}!!')
#print(f'Este texto debería ser {colores.negritas("negritas")}!!')
#print(f'Este texto debería ser {colores.subrayado("subrayado")}!!')
#print(f'Este texto debería ser {colores.subrayado(colores.morado("morado"))}!!')
#print(f'Este texto debería ser {colores.negritas(colores.amarillo("amarillo"))}!!')
