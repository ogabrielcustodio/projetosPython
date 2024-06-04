"""
Este é um arquivo modular e deverá ser importado para ser utilizado. O argumento *args pode ser substituido por uma lista em que 
os valores são adicionados por meio de entrada de valores e o método append().
"""
def Mediana(*args):
    """
    Calcula a mediana de uma lista de valores númericos. 
    O argumento da função é uma lista de valores númericos inteiros em quantidade indeterminada marcada pelo uso 
    da palavra chave *args. O retorno da função é o valor central inteiro da lista de valores númericos, ou seja, a mediana.
    """
    OrdenaLista = sorted(args)
    listaIndice = len(args)//2

    if len(args) % 2 == 0:
        mediana = (OrdenaLista[listaIndice-1] + OrdenaLista[listaIndice])/2
    else:
        mediana = OrdenaLista[listaIndice]

    return mediana

def Moda(*args):
    """
    Procura o valor númerico mais frequente em uma lista de valores numéricos inteiros. 
    O argumento da função é uma lista de valores númericos inteiros em quantidade
    indeterminada marcada pelo uso da palavra reservada *args. 
    O retorno da função é o valor númerico inteiro mais frequente na lista de valores númericos.
    """
    quantMaxima = 0
    valorFrequente = 0

    for n in args: 
        quantidade  = 0
        for m in args:
            if n == m:
                quantidade += 1

        if quantidade >  quantMaxima:
            quantMaxima = quantidade
            valorFrequente = n

    return valorFrequente

def Media(*args):
    """
    Calcula a média de uma lista de valores numéricos inteiros. 
    O argumento da função é uma lista de valores numéricos inteiros em quantidade indeterminada marcada pelo uso
    da palavra chave *args. O retorno da função é a média de uma lista de valores numéricos inteiros. 
    A média pode ser do tipo ponto flutuante ou ser do tipo inteiro.
    """
    soma = media = 0
    
    for n in args:
        soma = soma + n
        media = soma/len(args)
    return media