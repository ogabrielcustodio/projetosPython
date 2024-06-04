salarioPorHora = float(input('Informe o seu salário por hora: '))
totalHorasRegulares = int(input('Informe o total de horas regulares: '))
totalHorasExtras = int(input('Informe o total de horas extras: '))


def calculaHorasExtras(totalHorasExtras, salarioPorHora):
    """A função calcula o pagamento de horas extras, 
    recebendo como argumentos o total de horas extras (int) e o salario por hora (float).
    Ao final a função retorna o resultado do pagamento de horas extras."""

    pagamentoHorasExtras = (totalHorasExtras * 1.5) * salarioPorHora

    return pagamentoHorasExtras

recebePagamentoHorasExtras = calculaHorasExtras(totalHorasExtras, salarioPorHora)


def calculaPagamentoSemanal(salarioPorHora, totalHorasRegulares, recebePagamentoHorasExtras):
    """A função calcula o pagamento semanal total  de um funcionário,
    recebendo como argumentos o salarioPorHora(float), total de horas regulares(int) e
    o pagamento das horas extras(float). Ao final a função retorna o resultado  do pagamento total semanal"""

    pagamentoSemanal = (salarioPorHora * totalHorasRegulares) + recebePagamentoHorasExtras

    return pagamentoSemanal

recebePagamentoSemanal = calculaPagamentoSemanal(salarioPorHora,totalHorasRegulares,recebePagamentoHorasExtras)

print(f'O salário por hora do funcionário é: R$ {salarioPorHora:.2f}.\n'
      f'As horas extras do funcionário é: {totalHorasExtras}.\n'
      f'As horas regulares do funcionário é: {totalHorasRegulares}.\n'
      f'O pagamento das horas extras é: R$ {recebePagamentoHorasExtras:.2f}.\n'
      f'O pagamento total semanal é: R$ {recebePagamentoSemanal:.2f}.')

