import os
import aiohttp
import logging

from app.internal.schemas.currency import Symbols
from app.package.redis_tools.tools import RedisTools

logger = logging.getLogger(__name__)


async def on_startup():
    async with aiohttp.ClientSession() as session:
        async with session.get(os.getenv("ALL_PAIRS_KEY")) as response:
            response_json = await response.json()
            parsed_pairs = Symbols(**response_json)
            cutted_pairs = parsed_pairs.symbols[:20]

            print(f"cutted_pairs: {cutted_pairs}")

            symbols = [pair.symbol for pair in cutted_pairs]

            for symbol in symbols:
                RedisTools.set_pair(symbol, 0)


async def on_loop_startup():
    for symbol in RedisTools.get_keys():
        async with aiohttp.ClientSession() as session:
            async with session.get(os.getenv("CURRENCY_PAIR_KEY")) as response:
                response_json = await response.json()
                RedisTools.set_pair(symbol, response_json["price"])
