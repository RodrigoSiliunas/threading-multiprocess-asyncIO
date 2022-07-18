from time import sleep
from queue import Queue
from threading import Thread


def data_generator(queue: Queue):
    for i in range(1, 11):
        print(f'Dado número {i} gerado.')
        queue.put(i)
        sleep(2)


def data_consumer(queue: Queue):
    while queue.qsize() > 0:
        value = queue.get()

        print(
            f'Dado de valor {value * 2} processado.')
        queue.task_done()
        sleep(1)


if __name__ == '__main__':
    queue = Queue()

    threads = [
        Thread(target=data_generator, args=(queue,)),
        Thread(target=data_consumer, args=(queue,))
    ]

    # What the fuck is your limit Python?
    [[th.start(), th.join()] for th in threads]
