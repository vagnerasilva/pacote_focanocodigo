

class MinhaClasse:
    estatico = "lhama"

    def __init__(self, estado) -> None:
        self.__estado = estado


obj1 = MinhaClasse(True)

#print(obj)

print(obj1.estatico)

print(MinhaClasse.estatico)








