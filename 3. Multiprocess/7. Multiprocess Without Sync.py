import multiprocessing
import ctypes as types


def deposit(balance):
    for _ in range(10_000):
        balance.value += 1


def withdraw(balance):
    for _ in range(10_000):
        balance.value -= 1


def do_transaction(balance):
    processes = [
        multiprocessing.Process(target=deposit, args=(balance,)),
        multiprocessing.Process(target=withdraw, args=(balance,))
    ]

    [process.start() for process in processes]
    [process.join() for process in processes]


def main():
    balance = multiprocessing.Value(types.c_int, 100)
    print(f'O saldo inicial da conta é de: {balance.value}')

    for _ in range(10):
        do_transaction(balance)

    print(f'O saldo final da conta é de: {balance.value}')


if __name__ == '__main__':
    main()
