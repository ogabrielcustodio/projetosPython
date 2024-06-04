import math
"""
Este programa cria um objeto esfera e calcula as seguintes medidas do objeto: diâmetro, circunferência, área da superfície e volume.
"""
class Esfera:
    def __init__(self, raio):
        """
        Cria uma variável única para cada objeto instanciado da classe Esfera. O argumento é o objeto instanciado e o atributo a ser
        inicializado na instanciação do objeto, no caso o atributo 'raio". É uma função sem retorno: None.
        """
        self.raio = raio

    def calculaDiametro(self):
        """
        Calcula o diâmetro da esfera. O argumento é o objeto instanciado contendo o atributo raio ja com o valor estabelecido. O retorno
        da função é o resultado de duas vezes o valor do atributo raio, sendo um retorno do tipo inteiro.
        """
        return 2*self.raio 
    
    def calculaCircunferencia(self):
        """
        Calcula a circunferência da esfera. O argumento é o objeto instanciado contendo o atributo raio já com o valor estabelecido.
        O retorno da função é o resultado de duas vezes o pi, e para acessar o valor de pi usamos a biblioteca math importada neste arquivo, vezes o raio, sendo um
        retorno do tipo float.
        """
        return 2 * math.pi * self.raio 
    
    def calculaSuperficie(self):
        """
        Calcula a área da superfície da esfera. O argumento é o objeto instanciado contendo o atributo raio já com o valor estabelecido. O retorno da função
        é o resultado de quatro vezes o pi, e novamente usamos a biblioteca math, vezes o raio elevado a 2, sendo um retorno do tipo float.
        """
        return 4 * math.pi * (self.raio**2)
    
    def calculaVolume(self):
        """
        Calcula o volume da esfere. O argumento é o objeto instanciado contendo o atributo raio já com o valor estabelecido. O retorno da função 
        é o resultado de quatro terço vezes o pi vezes o raio elevado a 3, sendo um retorno do tipo float.
        """
        return (4/3 ) * math.pi * (self.raio**3)