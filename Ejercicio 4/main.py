from Polinomio1 import Polinomio1
from Polinomio2 import Polinomio as Polinomio2


class Main:
    @staticmethod
    def demostrar_operaciones():
        polinomio1 = Polinomio2()
        polinomio1.agregar_termino(1, 3)  # x^3
        polinomio1.agregar_termino(-2, 1)  # -2x
        polinomio1.agregar_termino(4, 0)  # +4
        print("Polinomio1 (x^3 - 2x + 4) evaluado en x=2:", polinomio1.evaluar(2))

        polinomio2 = Polinomio2()
        polinomio2.agregar_termino(3, 2)  # 3x^2
        polinomio2.agregar_termino(1, 1)  # x
        polinomio2.agregar_termino(-2, 0)  # -2
        print("Polinomio2 (3x^2 + x - 2) evaluado en x=2:", polinomio2.evaluar(2))

        # A continuación, asumimos que las operaciones retornan nuevas instancias de Polinomio2
        suma = polinomio1.sumar(polinomio2)
        print("Suma de polinomio1 y polinomio2 evaluada en x=2:", suma.evaluar(2))

        resta = polinomio1.restar(polinomio2)
        print("Resta de polinomio1 y polinomio2 evaluada en x=2:", resta.evaluar(2))

        multiplicacion = polinomio1.multiplicar(polinomio2)
        print("Multiplicación de polinomio1 y polinomio2 evaluada en x=2:", multiplicacion.evaluar(2))
        
        # La división de polinomios puede ser compleja y no siempre dará un polinomio resultante simple.
        # La implementación y el uso adecuado dependerán de cómo desees manejar esta operación.

if __name__ == "__main__":
    Main.demostrar_operaciones()