import asyncio
import aiofiles


async def read_file(path: str, filename: str):
    async with aiofiles.open(f'{path}/{filename}') as file:
        content = await file.read()

    print(content)


async def read_lines_from_file(path: str, filename: str):
    async with aiofiles.open(f'{path}/{filename}') as file:
        async for line in file:
            print(line)


async def main():
    tasks = [
        asyncio.create_task(read_file('assets', 'texto.txt')),
        asyncio.create_task(read_lines_from_file('assets', 'texto.txt'))
    ]

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())

    print('Fim da execução do programa.')
