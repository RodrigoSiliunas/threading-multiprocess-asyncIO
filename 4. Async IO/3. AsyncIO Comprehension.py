import asyncio
from datetime import datetime


async def data_generator(quantity: int, data: asyncio.Queue):
    print(f'Aguarde estamos gerando um total de {quantity} dados.\n')

    for index in range(quantity):
        await data.put((index * index, datetime.now()))
        await asyncio.sleep(0.001)

    print(f'{quantity} dados gerados com sucesso.')


async def data_processor(quantity: int, data: asyncio.Queue):
    print(f'Aguarda estamos processando um total de {quantity} dados.\n')

    processed = 0

    while processed < quantity:
        await data.get()
        processed += 1
        await asyncio.sleep(0.001)

    print(f'Foram processados um total de {quantity} dados com sucesso.')


async def main():
    total = 5_000
    data = asyncio.Queue()

    print(f'Computando um total de {total} dados de uma vez.')

    await data_generator(total, data)
    await data_processor(total, data)


if __name__ == '__main__':
    asyncio.run(main())
