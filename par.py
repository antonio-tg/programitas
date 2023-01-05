# Este programa pide un número al usuario y le indica si es par o impar y si quiere meter otro número

class par_impar():
    # Atributos
    numero=None
    # Metodos
    def isnum(self):
        while self.numero.isdigit() == False:
            self.numero = input('Ese no es un número, intente de nuevo por favor: ')

    def par_o_impar(self):
        if float(self.numero)//2 == float(self.numero)/2:
            print('¡Es un número par!')
        else:
            print('¡Es un número impar!')

final = 'si'
while final == 'si':
    num = par_impar()
    num.numero = input('\nIngrese un número: ')
    num.isnum()
    num.par_o_impar()
    f = ''
    while f not in {'si','no'}:
        f = input('Si desea ingresar otro número teclee "si", en caso contrario teclee "no": ').lower()
    final = f
