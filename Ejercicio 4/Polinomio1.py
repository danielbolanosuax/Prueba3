from Nodo import Nodo

class Polinomio1:
    def __init__(self):
        self.cabeza = None

    def agregar_termino(self, coeficiente, exponente):
        nuevo_nodo = Nodo(coeficiente, exponente)
        if not self.cabeza or self.cabeza.exponente < exponente:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.exponente >= exponente:
                actual = actual.siguiente
            if actual.exponente == exponente:
                actual.coeficiente += coeficiente
            else:
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo

    def evaluar(self, x):
        resultado = 0
        actual = self.cabeza
        while actual:
            resultado += actual.coeficiente * (x ** actual.exponente)
            actual = actual.siguiente
        return resultado