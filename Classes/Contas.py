from .ContaLuz import ContaLuz

class Contas:
    def __init__(self):
        self.__contasLuz = []

    def addContaLuz(self,conta:ContaLuz):
        self.__contasLuz.append(conta)

    def mediaConsumidor(self):
        media = 0
        for conta in self.__contasLuz:
            media+=conta.getValorPagar()
        return f"A media das Contas R$ {media/len(self.__contasLuz):.2f}"