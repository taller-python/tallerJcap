'''Ejercicio semana 3 taller Python'''


class Compuerta():
    '''Clase compuerta'''
    __param1 = 0
    __param2 = 0
    def __init__(self, param1, param2):
        self.__param1 = param1
        self.__param2 = param2

    def set_param1(self, param1):
        '''set_param1'''
        self.__param1 = param1

    def set_param2(self, param2):
        '''set_param2'''
        self.__param2 = param2

    def get_param1(self):
        '''get_param1'''
        return self.__param1

    def get_param2(self):
        '''get_param2'''
        return self.__param2

class CompuertaOr(Compuerta):
    '''Clase CompuertaOr'''
    def operacion(self):
        '''operacion'''
        if self.get_param1() == 0 and self.get_param2() == 0:
            return 'FALSO'
        return 'VERDADERO'

class CompuertaAnd(Compuerta):
    '''Clase CompuertaAnd'''
    def operacion(self):
        '''operacion'''
        if self.get_param1() == 1 and self.get_param2() == 1:
            return 'VERDADERO'
        return 'FALSO'


COMPUERTA_OR = CompuertaOr(1, 0)
print('Compuerta OR 1,0')
print(COMPUERTA_OR.operacion())

COMPUERTA_OR = CompuertaOr(1, 1)
print('Compuerta OR 1,1')
print(COMPUERTA_OR.operacion())

COMPUERTA_OR = CompuertaOr(0, 1)
print('Compuerta OR 0,1')
print(COMPUERTA_OR.operacion())

COMPUERTA_OR = CompuertaOr(0, 0)
print('Compuerta OR 0,0')
print(COMPUERTA_OR.operacion())

print('***********************************')

COMPUERTA_AND = CompuertaAnd(1, 1)
print('Compuerta AND 1,1')
print(COMPUERTA_AND.operacion())

COMPUERTA_AND = CompuertaAnd(1, 0)
print('Compuerta AND 1,0')
print(COMPUERTA_AND.operacion())

COMPUERTA_AND = CompuertaAnd(0, 0)
print('Compuerta AND 0,0')
print(COMPUERTA_AND.operacion())

COMPUERTA_AND = CompuertaAnd(0, 1)
print('Compuerta AND 0,1')
print(COMPUERTA_AND.operacion())
