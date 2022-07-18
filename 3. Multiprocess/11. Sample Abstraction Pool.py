import multiprocessing

# We just need change the import and the script will execute fine;
# from concurrent.futures.thread import ThreadPoolExecutor as Executor
from concurrent.futures.process import ProcessPoolExecutor as Executor

from time import sleep


def draw_on_screen():
    print('[', end='', flush=True)

    for _ in range(10):
        print('#', end='', flush=True)
        sleep(0.8)

    print(']', end='', flush=True)

    return 42


def main():
    with Executor() as executor:
        future = executor.submit(draw_on_screen)

    print(f'\nO resultado da função foi de: {future.result()}')


if __name__ == '__main__':
    main()
