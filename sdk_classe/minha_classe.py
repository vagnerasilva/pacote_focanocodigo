class MinhaClasse:

    def __init__(self, att) -> None:
        self.meu_atributo = 'Ola Mundo'
        self.meu_atributo2 = att

    def meu_metodo(self):
        print("Estou no metodo! ")
        print(self.meu_atributo)
        print(self.meu_atributo2)


    def meu_metodo2(self, num, mult):
        return num * mult
    

objeto = MinhaClasse(23)

objeto.meu_metodo()