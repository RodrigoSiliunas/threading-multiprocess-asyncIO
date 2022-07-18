import multiprocessing
from time import sleep


def draw_on_screen():
    print('[', end='', flush=True)

    for _ in range(10):
        print('#', end='', flush=True)
        sleep(0.8)

    print(']', end='', flush=True)


def main():
    process = multiprocessing.Process(target=draw_on_screen)
    [process.start(), process.join()]


if __name__ == '__main__':
    main()
