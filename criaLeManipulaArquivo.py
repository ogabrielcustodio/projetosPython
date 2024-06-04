import os
"""
Este programa faz escrita e leitura de arquivo. O propósito desse programa é que o usuário ao terminar de escrever no arquivo
possa ler uma linha específica de acordo com o número de linhas. A resolução dessa atividade pode ser feita com a 
criação de um objeto enumerate.
"""
# escrita do arquivo
with open('file.txt','w') as file:
    file.write('Primeira linha\n')
    file.write('Segunda linha\n')
    file.write('Terceira linha\n')

numeroLinha = int(input('Informe o número da linha  que deseja fazer a leitura: '))

def numeroDeLinhas():
    """
    Conta o número de linhas do arquivo após o arquivo se aberto em modo de leitura. 
    Essa função não possui argumento.
    O retorno da função deve ser o número de linhas
    totais do arquivo.
    """
    nlinha = 0
    # leitura do arquivo
    with open('file.txt', 'r') as file:
        linhas = file.readlines()
        for l in linhas:
            nlinha += 1
    return nlinha

quantidadeLinha = numeroDeLinhas()

def lerLinha(numeroLinha):
    """
    Ler a linha indicada pelo usuário. 
    O argumento da função é a linha a ser lida pelo usuário, esse argumento deve ser do tipo inteiro. 
    O retorno da função é a linha correspondente a linha indicada pelo usuário, 
    nessa linha de retorno deve estar o texto correspondente ao número da linha no arquivo.
    """
    with open('file.txt', 'r') as file:
        lines = file.readlines()
        if numeroLinha == 0:
            return None
        elif 1 <= numeroLinha and numeroLinha <= quantidadeLinha:
            return lines[numeroLinha - 1]
        else:
            return None
    
leitura = lerLinha(numeroLinha)
print(f'O texto da linha {numeroLinha} é: {leitura}')

def removeFile(filename):
    """
    Remove o arquivo usando o método nativo do sistema operacional "remove()" . 
    O argumento da função deverá ser o nome do arquivo a ser removido, sendo do tipo string.
    É uma função sem retorno e com tratamento de exceções de arquivo, caso o arquivo não seja encontrado.
    """
    try:
        os.remove(filename)
        print('Arquivo deletado com sucesso!')
    except FileNotFoundError:
        print('Arquivo não encontrado!')

removeFile()