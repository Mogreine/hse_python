import aiofiles
import aiohttp
import asyncio
import numpy as np


async def download_and_save_pic(url, idx):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            f = await aiofiles.open(f'./artifacts/img_{idx}.png', mode='wb')
            await f.write(await response.read())
            await f.close()


async def main_loop(n_pics):
    url = "https://www.thiswaifudoesnotexist.net/"
    total_pics = int(1e5)

    pic_numbers = np.random.choice(total_pics, size=n_pics, replace=False)

    pic_urls = [f"{url}example-{num}.jpg" for num in pic_numbers]

    await asyncio.wait([download_and_save_pic(pic_url, idx) for idx, pic_url in enumerate(pic_urls)])


if __name__ == "__main__":
    n_pics = 10

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_loop(n_pics))
