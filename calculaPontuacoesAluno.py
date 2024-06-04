"""
Este programa cria um objeto da classe Estudante e para cada objeto estudante temos o nome e uma lista de pontuações. Ao final deve ser impresso o nome do estudante
as pontuações enumeradas. Também é feito o cálculo da pontuação média, a busca pela pontuação mais alta e a substituição de uma pontução.
"""

class Student:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = []

    def __str__(self):
        return self.nome
    
    def obterPontuacao(self):
        """
        Obtém a pontuação do estudante e armazena cada pontuação em uma lista de até 3 elementos. O argumento é o objeto instanciado e dele é utilizado o atributo
        lista para ir armazenando cada pontuação na lista. O retorno é a lista atualizada com as pontuações do estudante.
        """
        for p in range(0,3):
            pontos = int(input('Informe a pontuação do aluno: '))
            self.pontuacao.append(pontos)
            pontos = 0
        return self.pontuacao
    
    def obterPontuacaoMaisAlta(self):
        """
        Obtém a pontuação mais alta do estudante. O argumento é o objeto instanciado e dele utilizamos o atributo lista para que por meio da iteração possamos encontrar
        a maior pontuação que será o retorno do método, sendo um retorno do tipo float.
        """
        maior = 0
        for i in range(len(self.pontuacao)):
            if self.pontuacao[i] > maior:
                maior = self.pontuacao[i]
        return maior

    def obterPontuacaoMedia(self):
        """
        Obtém a pontuação média do estudante. O argumento é o objeto instanciado e dele utilizamos a lista para somar todas as pontuações e dividir pelo tamanho da lista
        obtendo desta forma a pontuação média que também é o retorno deste método, sendo um retorno do tipo float.
        """
        soma = 0
        for n in self.pontuacao:
            soma += n
        media = soma/len(self.pontuacao)
        return media

    def substituiPontuacao(self):
        """
        Substitui a pontuação do estudante depois do usuário indicar qual das pontuações deseja alterar. O argumento é o objeto instanciado e dele utilizamos a lista 
        de pontuações para encontrar a pontuação a ser substituída e posteriormente substituí-la. É um método sem retorno.
        """
        posicao = int(input('Informe a posição da pontuação que deseja alterar: '))
        for pt in range(0,len(self.pontuacao)):
            if self.pontuacao[pt] == self.pontuacao[posicao]:
                notaNova = int(input('Informe a pontuação nova: '))
                self.pontuacao[pt] = notaNova

def exibirPontuacao():
    """
    Exibi a pontuação do estudante enumerando as pontuações.  É um método sem argumento e sem retorno.
    """
    numeroPontuacao = 1
    print(f'Nome: {estudante.nome}')
    for ponto in estudante.pontuacao:
        print(f'Pontuação {numeroPontuacao}: {ponto}.')
        numeroPontuacao += 1


estudante = Student('Gabriel')



