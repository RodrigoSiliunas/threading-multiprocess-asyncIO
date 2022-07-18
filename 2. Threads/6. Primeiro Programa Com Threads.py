from datetime import datetime
import math

import multiprocessing
import threading


def main():
    cores = multiprocessing.cpu_count()
    print(f'Realizando o processamento matemático utilizando {cores} core(s).')

    start = datetime.now()
    # compute(50_000_000) # Antigamente;

    threads = []

    for i in range(1, cores + 1):
        inicio = 50_000_000 * (i - 1) / cores
        fim = 50_000_000 * i / cores

        print(
            f'O core número {i} está processando de: {inicio} até {fim}.')

        threads.append(
            threading.Thread(target=compute, kwargs={
                             'start': inicio, 'end': fim}, daemon=True)
        )

    # Start the process;
    [[th.start(), th.join()] for th in threads]

    time = datetime.now() - start
    print(
        f'A execução dessa função durou {time.total_seconds():.2f} segundos.')


def compute(end, start=1):
    pos = start
    fator = 1000 * 1000

    while pos < end:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


if __name__ == '__main__':
    main()

"""
    1. A execução dessa função deurou 33.73 segundos.
"""
