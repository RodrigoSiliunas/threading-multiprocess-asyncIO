import multiprocessing


def ping(queue):
    queue.put('Rodrigo')


def pong(queue):
    message = queue.get()
    print(f'{message} Siliunas')


def main():
    conn = multiprocessing.Queue()

    processes = [
        multiprocessing.Process(target=ping, args=(conn,)),
        multiprocessing.Process(target=pong, args=(conn,))
    ]

    [process.start() for process in processes]
    [process.join() for process in processes]


if __name__ == '__main__':
    main()
