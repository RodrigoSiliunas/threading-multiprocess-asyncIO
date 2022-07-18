import multiprocessing
from time import sleep


def function_one(val, stat):
    if stat:
        res = val + 10
        stat = False
    else:
        res = val + 20
        val = 200
        stat = True

    print(f'O retorno da função um foi de {res}.')  # Esperamos um retorno de 120;
    sleep(0.001)


def function_two(val, stat):
    if stat:
        res = val + 30
        stat = False
    else:
        res = val + 40
        val = 400
        stat = True

    print(f'O retorno da função dois foi de {res}.')  # Esperamos um retorno de 140;
    sleep(0.001)


def main():
    valor = 100
    status = False

    processes = [
        multiprocessing.Process(target=function_one, args=(valor, status)),
        multiprocessing.Process(target=function_two, args=(valor, status))
    ]

    [process.start() for process in processes]
    [process.join() for process in processes]


if __name__ == '__main__':
    main()
