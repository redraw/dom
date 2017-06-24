import shlex
import aiohttp
import asyncio


async def parse(url, selector):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.read()
            return await pup(html, selector)


async def pup(html, args):
    cmd = shlex.split("pup %s json\{\}" % args)

    process = await asyncio.create_subprocess_exec(
        *cmd, stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate(input=html)

    return stdout.decode('utf-8')