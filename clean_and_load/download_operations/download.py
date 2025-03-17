import aiohttp
from tqdm.asyncio import tqdm
import asyncio
from typing import List, Dict, Optional


async def download_query(
    url: str, headers: Optional[Dict[str, str]] = None
) -> Optional[str]:
    headers = headers or {}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            if response.status != 200:
                return None
            return await response.text()


async def gather_connections(
    url_list: List[str], headers: Optional[Dict[str, str]] = None
) -> List[Optional[str]]:
    headers = headers or {}
    tasks = [download_query(url, headers) for url in url_list]

    print("Starting downloads...")
    results: List[Optional[str]] = await tqdm.gather(*tasks, unit="b", unit_scale=True)

    return results


def download_list(
    url_list: List[str], headers: Optional[Dict[str, str]] = None
) -> List[Optional[str]]:
    headers = headers or {}
    return asyncio.run(gather_connections(url_list, headers))
