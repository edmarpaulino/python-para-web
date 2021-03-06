def cria_conta(numero, titular, saldo, limite):
    conta = {
        "numero": numero,
        "titular": titular,
        "saldo": saldo,
        "limite": limite
    }
    return conta


def deposita(conta, valor):
    conta["saldo"] += valor


def saca(conta, valor):
    conta["saldo"] -= valor


def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))


conta = cria_conta(111, "edmar", 1.0, 1000.0)

deposita(conta, 15)
saca(conta, 10)
extrato(conta)
