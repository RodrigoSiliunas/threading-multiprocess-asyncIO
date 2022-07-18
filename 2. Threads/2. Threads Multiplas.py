from datetime import datetime
from time import sleep
import threading


def main():
    threads = [
        threading.Thread(target=contar, args=('dinheiro', 1000,)),
        threading.Thread(target=contar, args=('momentos', 10,)),
        threading.Thread(target=contar, args=('felicidade', 100,)),
        threading.Thread(target=contar, args=('amigos', 100,)),
    ]

    # Adiciona a nossa Thread na pool de threads prontas para execução.
    [th.start() for th in threads]

    for i in range(0, 11):
        print(
            f'O programa vai sendo executado enquanto a nossa Thread está executando o código.')
        sleep(1)

    # Diz para nosso programa que é para aguardar a Thread ser finalizada antes de continuar.
    [th.join() for th in threads]

    # O print abaixo ou qualquer código abaixo desse print só será executado após o término de execução de nossas Threads. Isso ocorre devido a chamada do método Join na nossa Thread.
    print(
        'No entanto quando chamamos o join da Thread o nosso programa espera a Thread terminar sua execução para que as próximas instruções sejam executadas.')


def contar(name, count):
    for i in range(0, count):
        print(f'{i + 1} {name} pulou a cerca...')
        sleep(1)


if __name__ == '__main__':
    main()
