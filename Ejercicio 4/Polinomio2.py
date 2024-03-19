class Polinomio:
    def __init__(self):
        self.coeficientes = {}  # Usamos un diccionario para facilitar la manipulación de términos.

    def agregar_termino(self, coeficiente, exponente):
        if exponente in self.coeficientes:
            self.coeficientes[exponente] += coeficiente
        else:
            self.coeficientes[exponente] = coeficiente

    def evaluar(self, x):
        resultado = sum(coef * (x ** exp) for exp, coef in self.coeficientes.items())
        return resultado

    def sumar(self, otro):
        resultado = Polinomio()
        for exp, coef in self.coeficientes.items():
            resultado.agregar_termino(coef, exp)
        for exp, coef in otro.coeficientes.items():
            resultado.agregar_termino(coef, exp)
        return resultado

    def restar(self, otro):
        resultado = Polinomio()
        for exp, coef in self.coeficientes.items():
            resultado.agregar_termino(coef, exp)
        for exp, coef in otro.coeficientes.items():
            resultado.agregar_termino(-coef, exp)
        return resultado

    def multiplicar(self, otro):
        resultado = Polinomio()
        for exp1, coef1 in self.coeficientes.items():
            for exp2, coef2 in otro.coeficientes.items():
                nuevo_exp = exp1 + exp2
                nuevo_coef = coef1 * coef2
                resultado.agregar_termino(nuevo_coef, nuevo_exp)
        return resultado

    def __str__(self):
        # Simplificada. Considera expandirla para manejar mejor la representación de términos.
        terminos = [f"{coef}x^{exp}" if exp != 0 else f"{coef}" for exp, coef in sorted(self.coeficientes.items(), reverse=True)]
        return " + ".join(terminos).replace("x^1 ", "x ").replace(" 1x", " x")

# Demostración
if __name__ == "__main__":
    polinomio1 = Polinomio()
    polinomio1.agregar_termino(1, 3)  # x^3
    polinomio1.agregar_termino(-2, 1)  # -2x
    polinomio1.agregar_termino(4, 0)  # +4

    polinomio2 = Polinomio()
    polinomio2.agregar_termino(3, 2)  # 3x^2
    polinomio2.agregar_termino(1, 1)  # x
    polinomio2.agregar_termino(-2, 0)  # -2

    suma = polinomio1.sumar(polinomio2)
    resta = polinomio1.restar(polinomio2)
    multiplicacion = polinomio1.multiplicar(polinomio2)

    print(f"Polinomio1: {polinomio1}")
    print(f"Polinomio2: {polinomio2}")
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
