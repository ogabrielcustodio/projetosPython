from tabulate import tabulate
"""
Este programa cria um relatório de folha de pagamento contendo o nome do funcionário, as horas que ele trabalhou e o salário pago.
"""
dadosFuncionarios = []

class Funcionarios:
    def __init__(self, nome, salarioPorHora, horasTrabalhadas):
        self.nome = nome
        self.__salarioPorHora = salarioPorHora
        self.horasTrabalhadas = horasTrabalhadas
        self.salarioPago = 0
    
    @property
    def salarioPorHora(self):
        """ 
        Método da classe que identifica por meio do decorador property que o atributo salarioPorHora é uma propriedade da classe não podendo receber
        alterações futuras.
        """
        return self.__salarioPorHora
    
    @salarioPorHora.setter
    def salarioPorHora(self, salario):
        """
        Método setter que é utilizado para alterar um atributo do objeto, sendo que neste caso como o objeto não pode ser alterado, é levantado uma exceção
        de erro de valor e uma mensagem indicativa de que o atributo não pode ser alterado.
        """
        raise ValueError('Não é permitido alterar esse atributo')
    
    def calculaSalario(self):
        """
        Calcula o salário do funcionário. O argumento é o objeto instanciado da classe Funcionários. O retorno é o resultado do cálculo do salário pago que
        envolve o salario por hora e horas trabalhadas, ambos são atributos do objeto instanciado da classe Funcionários, sendo um retorno do tipo float.
        """
        self.salarioPago = self.__salarioPorHora * self.horasTrabalhadas
        return self.salarioPago

funcionario = Funcionarios('Gabriel', 30.33, 4)
salarioPago = funcionario.calculaSalario()

def adicionaFuncionario(): 
    """
    Adiciona um novo funcionário na lista de funcionários criada anteriormente. É uma função sem argumento e o retorno é a lista com o funcionário adicionado 
    pelo método append. O funcionário é convertido em dicionário ao ser adicionado na lista usando o atributo especial dict que está armazenando os 
    atributos do objeto instanciado em um dicionário, assim teremos uma lista de dicionário, onde cada dicionário é um funcionário, ou seja, um objeto da 
    classe Funcionarios.
    """
    dadosFuncionarios.append(funcionario.__dict__)
    return dadosFuncionarios

recebeAdicionaFuncionario = adicionaFuncionario()
tabela = tabulate(recebeAdicionaFuncionario, headers = "keys", tablefmt="grid")


