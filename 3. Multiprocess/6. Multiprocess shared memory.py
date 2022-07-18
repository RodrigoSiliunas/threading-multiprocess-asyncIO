import multiprocessing
from time import sleep
import ctypes


def function_one(val, stat):
    if stat.value:
        res = val.value + 10
        stat.value = False
    else:
        res = val.value + 20
        val.value = 200
        stat.value = True

    print(f'O retorno da função um foi de {res}.')  # Esperamos um retorno de 120;
    sleep(0.001)


def function_two(val, stat):
    if stat:
        res = val.value + 30
        stat.value = False
    else:
        res = val.value + 40
        val.value = 400
        stat.value = True

    print(f'O retorno da função dois foi de {res}.')  # Esperamos um retorno de 230;
    sleep(0.001)


def main():
    valor = multiprocessing.Value(ctypes.c_int, 100)
    status = multiprocessing.Value(ctypes.c_bool, False)

    processes = [
        multiprocessing.Process(target=function_one, args=(valor, status)),
        multiprocessing.Process(target=function_two, args=(valor, status))
    ]

    [process.start() for process in processes]
    [process.join() for process in processes]


if __name__ == '__main__':
    main()
