import asyncio
from datetime import datetime


async def data_generator(quantity: int, data: asyncio.Queue):
    await asyncio.sleep(5)
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

    tasks = [
        asyncio.create_task(data_processor(total, data)),
        asyncio.create_task(data_processor(total, data)),
        asyncio.create_task(data_generator(total * 2, data))
    ]

    await asyncio.gather(tasks[0], tasks[1], tasks[2])

if __name__ == '__main__':
    asyncio.run(main())

    print(
        'Esse print irá rodar assim que o programa for iniciado, o programa principal não irá aguardar a resposta da função async'
    )
