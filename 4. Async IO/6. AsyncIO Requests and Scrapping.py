import asyncio
import aiohttp
import bs4
import aiofiles
from typing import List


async def get_links_from_file(path: str, filename: str) -> List[str]:
    links = []

    async with aiofiles.open(f'{path}/{filename}') as file:
        async for link in file:
            links.append(link.strip())

    return links


async def get_html_from_link(link):
    print(f'⌛ Acessando o HTML da página referente ao link: {link}\n')

    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            response.raise_for_status()

            return await response.text()


def get_title_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    title = soup.select_one('title').text.split('|')[0].strip()

    return title


async def print_titles():
    tasks = []
    links = await get_links_from_file('assets', 'links.txt')

    for link in links:
        tasks.append(asyncio.create_task(get_html_from_link(link)))

    for task in tasks:
        html = await task
        title = get_title_from_html(html)

        print(f'O título do curso é: {title}.')



if __name__ == '__main__':
    asyncio.run(print_titles())
