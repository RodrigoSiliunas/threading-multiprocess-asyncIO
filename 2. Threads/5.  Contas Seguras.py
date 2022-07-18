from random import randint, choice
from threading import Thread, RLock
from time import sleep

from typing import List


lock = RLock()


class Conta:
    def __init__(self, saldo=0) -> None:
        self.saldo = saldo


def criar_contas() -> List[Conta]:
    return [
        Conta(randint(5_000, 10_000)), Conta(randint(5_000, 10_000)),
        Conta(randint(5_000, 10_000)), Conta(randint(5_000, 10_000)),
        Conta(randint(5_000, 10_000)), Conta(randint(5_000, 10_000)),
        Conta(randint(5_000, 10_000)), Conta(randint(5_000, 10_000)),
        Conta(randint(5_000, 10_000)), Conta(randint(5_000, 10_000)),
    ]


def transferir(origem: Conta, destino: Conta, valor: int):
    if (origem.saldo < valor):
        return None

    with lock:
        origem.saldo -= valor
        destino.saldo += valor


def valida_banco(contas: List[Conta], total: int):
    with lock:
        saldo_atual = sum(conta.saldo for conta in contas)

    if (saldo_atual != total):
        print(
            f'Erro! Balanço bancário inconsistente: BRL {saldo_atual:.2f} vs BRL {total:.2f}.', flush=True)
    else:
        print(
            f'Tudo certo. Balanço bancário consistente: BRL {total:.2f}.', flush=True)


def pega_duas_contas(contas: List[Conta]):
    contaUm, contaDois = choice(contas), choice(contas)

    while (contaUm == contaDois):
        contaDois = choice(contas)

    return contaUm, contaDois

def servicos(contas, total):
    for _ in range(1, 10_000):
        contaUm, contaDois = pega_duas_contas(contas)

        valor = randint(100, 500)
        transferir(contaUm, contaDois, valor)
        valida_banco(contas, total)


if __name__ == '__main__':
    contas = criar_contas()

    with lock:
        total = sum(conta.saldo for conta in contas)

    threads = [
        Thread(target=servicos, args=(contas, total,)),
        Thread(target=servicos, args=(contas, total,)),
        Thread(target=servicos, args=(contas, total,)),
        Thread(target=servicos, args=(contas, total,))
    ]

    [th.start() for th in threads]
    [th.join() for th in threads]

    print(
        f'Transferências realizadas com sucesso...')
    valida_banco(contas, total)
