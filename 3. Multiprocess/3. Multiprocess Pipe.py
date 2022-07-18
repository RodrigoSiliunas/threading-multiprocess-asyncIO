import multiprocessing


def ping(conn):
    conn.send('Oh my poosh!')


def pong(conn):
    message = conn.recv()
    print(f'{message} pong.')


def main():
    conn1, conn2 = multiprocessing.Pipe(True)

    processes = [
        multiprocessing.Process(target=ping, args=(conn1,)),
        multiprocessing.Process(target=pong, args=(conn2,))
    ]

    # List compreehnsion;
    [process.start() for process in processes]
    [process.join() for process in processes]


if __name__ == '__main__':
    main()
