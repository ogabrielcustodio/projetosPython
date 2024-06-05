from tabulate import tabulate

valorCompra = float(input('Digite o valor da compra: '))

pagamentoInicialLoja = 0.10
percentualValorCompra = 0.05
taxaJurosDevidos = 0.12


def calculaPagamentoInicial(valorCompra):
    return valorCompra * pagamentoInicialLoja

def calculaPagamentoMensal(valorCompra, percentualValorCompra, pagamentoInicial):
    return abs((percentualValorCompra * valorCompra) - pagamentoInicial)

def calculaSaldoInicial(valorCompra, pagamentoInicial):
    return valorCompra - pagamentoInicial

def calculaJurosDevidos(saldoInicial, taxaJurosDevidos):
    return saldoInicial * taxaJurosDevidos /12

def calculaValorPrincipal(pagamentoMensal, recebeJurosDevidos):
    return abs(pagamentoMensal - recebeJurosDevidos)

def calculaSaldoRestante(saldoInicial, valorPrincipal):
    return saldoInicial - valorPrincipal


pagamentoInicial = calculaPagamentoInicial(valorCompra)
pagamentoMensal = calculaPagamentoMensal(valorCompra, percentualValorCompra,pagamentoInicial)
saldoInicial= calculaSaldoInicial(valorCompra, pagamentoInicial)


cronograma = []

for mes in range(1,13):
    jurosDevidos = calculaJurosDevidos(saldoInicial,  taxaJurosDevidos)
    valorPrincipal = calculaValorPrincipal(pagamentoMensal, jurosDevidos)
    saldoRestante = calculaSaldoRestante(saldoInicial, valorPrincipal)

    pagamentos = {
        "mês": mes,
        "saldo inicial": saldoInicial,
        "juros devidos": jurosDevidos,
        "valor principal": valorPrincipal,
        "pagamento mensal": pagamentoMensal,
        "saldo restante": saldoRestante
    }
    cronograma.append(pagamentos)

    saldoInicial = saldoRestante

print(tabulate(cronograma, headers="keys", tablefmt="grid"))
