from datetime import datetime
from time import sleep
import threading


def main():
    th = threading.Thread(target=contar, args=('elefante', 10,))

    # Adiciona a nossa Thread na pool de threads prontas para execução.
    th.start()

    for i in range(0, 11):
        print(
            f'O programa vai sendo executado enquanto a nossa Thread está executando o código.')
        sleep(1)

    # Diz para nosso programa que é para aguardar a Thread ser finalizada antes de continuar.
    th.join()

    print(
        'No entanto quando chamamos o join da Thread o nosso programa espera a Thread terminar sua execução para que as próximas instruções sejam executadas.')


def contar(name, count):
    for i in range(0, count):
        print(f'{i + 1} {name} pulou a cerca...')
        sleep(1)


if __name__ == '__main__':
    main()
