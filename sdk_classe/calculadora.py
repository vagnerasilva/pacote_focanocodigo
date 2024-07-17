class Calculadora:

    def calcular(self, op, num1, num2):
        if op == '+':
            self.__adicionar(num1, num2)
        elif op == '-':
            self.__subtrair(num1, num2)
        else:
            print("Operacao Invalida")

    def __adicionar(self, num1, num2):
        return num1 + num2
    
    def __subtrair(self, num1, num2):
        return num1 + num2

calculadora = Calculadora()

resultado = calculadora.calcular("+", 3, 2)
print(resultado)