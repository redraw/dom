import shlex
import logging
import aiohttp
import subprocess

logger = logging.getLogger(__name__)


async def parse(url, selector):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as result:

            html = await result.read()

            cmd = shlex.split("pup %s json\{\}" % selector)
            logger.info("CMD: %s" % cmd)

            stdout = subprocess.check_output(cmd, input=html)

            return stdout.decode('utf-8')
