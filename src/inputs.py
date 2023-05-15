import sys

class Entrada:
    values: list
    nome_binario: str
    nome_trabalho: str
    nome_algoritmo: str
    printar: bool

    def __init__(self) -> None:
        self.values = sys.argv
        self.nome_trabalho = self.values.pop(0) # Recebendo o nome do trabalho
        self.tamanho_vetor = self.values.pop(0) # Recebendo o nome do trabalho        
        self.nome_algoritmo = self.values.pop(0) # Recebendo o nome do algoritmo
        self.printar = False

        try:
            int(self.values[-1]) # Verificando se o último valor da lista é a palavra print
        except:
            self.values.pop(-1)
            self.printar = True

        self.values = [int(i) for i in self.values]

    def __str__(self) -> str:
        buffer = "Nome do trabalho: " + self.nome_trabalho + "\nNome do algoritmo: " + self.nome_algoritmo + "\nTamanho do Vetor: " + self.tamanho_vetor + "\nValores: ["

        i = 0
        for valor in self.values:
            buffer += f"{valor}"
            i += 1

            if i < len(self.values):
                buffer += ", "

        return buffer + "]"