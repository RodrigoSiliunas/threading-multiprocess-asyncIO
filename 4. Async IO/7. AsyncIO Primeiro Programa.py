import asyncio
import math
from datetime import datetime
from multiprocessing import cpu_count


async def main():
    start = datetime.now()
    tasks = []
    num_of_cores = cpu_count()

    for i in range(num_of_cores):
        inicio = 50_000_000 * (i - 1) / num_of_cores
        fim = 50_000_000 * i / num_of_cores

        tasks.append(asyncio.create_task(compute(fim, inicio)))

    await asyncio.gather(*tasks)

    print(
        f'O tempo de execução do programa foi de {(datetime.now() - start).total_seconds():.2f} segundos.')


async def compute(end, start=1):
    pos = start
    fator = 1000 * 1000

    while pos < end:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


if __name__ == "__main__":
    asyncio.run(main())


"""
    Terminou em 20.58 segundos.
"""
