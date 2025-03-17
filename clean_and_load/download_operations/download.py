import aiohttp
from tqdm.asyncio import tqdm
import asyncio


async def download_query(url, headers={}):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            if response.status != 200:
                return None
            read = await response.text()
            return read


async def gather_connections(url_list, headers={}):
    tasks = []
    results = []

    for url in url_list:
        print(f"- Downloading {url}")
        tasks.append(download_query(url, headers))

    results = await tqdm.gather(*tasks, unit="b", unit_scale=True)

    return results


def download_list(url_list, headers={}):
    return asyncio.run(gather_connections(url_list, headers))
