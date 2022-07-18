import multiprocessing
import ctypes as types


def deposit(balance, lock):
    for _ in range(10_000):
        with lock:
            balance.value += 1


def withdraw(balance, lock):
    for _ in range(10_000):
        with lock:
            balance.value -= 1


def do_transaction(balance, lock):
    processes = [
        multiprocessing.Process(target=deposit, args=(balance, lock)),
        multiprocessing.Process(target=withdraw, args=(balance, lock))
    ]

    [process.start() for process in processes]
    [process.join() for process in processes]


def main():
    balance = multiprocessing.Value(types.c_int, 100)
    print(f'O saldo inicial da conta é de: {balance.value}')

    lock = multiprocessing.RLock()

    for _ in range(10):
        do_transaction(balance, lock)

    print(f'O saldo final da conta é de: {balance.value}')


if __name__ == '__main__':
    main()
