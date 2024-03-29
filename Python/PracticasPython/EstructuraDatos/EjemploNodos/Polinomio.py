class Nodo(object):
    info, sig = None, None


class datoPolinomio(object):
    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino


class Polinomio(object):
    def __init__(self):
        self.termino_mayor = None
        self.grado = -1


def agregar_termino(polinomio : Polinomio, termino, valor):
    aux = Nodo()
    dato = datoPolinomio(valor, termino)
    aux.info = dato
    
    if (termino > polinomio.grado):
        aux.sig = polinomio.termino_mayor
        polinomio.termino_mayor = aux
        polinomio.grado = termino
    else:
        actual = polinomio.termino_mayor
        
        while (actual.sig is not None) and (termino < actual.sig.info.termino):
            actual = actual.sig
        
        aux.sig = actual.sig
        actual.sig = aux


def obtener_valor(polinomio, termino):
    aux = polinomio.termino_mayor
    
    while(aux is not None) and (aux.info.termino > termino):
        aux = aux.sig
    if (aux is not None) and (aux.info.termino == termino):
        return aux.info.valor
    else:
        return 0


def mostrar(polinomio):
    aux = polinomio.termino_mayor
    pol = ''
    
    if (aux is not None):
        while (aux is not None):
            signo = ' '
            
            if (aux.info.valor >= 0):
                signo += '+'
            
            pol += signo + str(aux.info.valor) + "x" + str(aux.info.termino)
            aux = aux.sig
    return pol


def sumar(polinomio1, polinomio2):
    paux = Polinomio()
    
    if (polinomio1.grado > polinomio2.grado):
        mayor = polinomio1
    else:
        polinomio2
    
    for i in range(0, mayor.grado + 1):
        total = obtener_valor(polinomio1, i) + obtener_valor(polinomio2, i)
        
        if (total != 0):
            agregar_termino(paux, i, total)
    return paux