"""
    This is the project's entry point.
"""

import logging
import asyncio
from telegram import Bot
from telegram.constants import ParseMode
from handlers import (constants,rank_handler)
from db import db
import cli_parser

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def main():
    """
        CLI args handling & main logic.
    """
    if cli_parser.args.add:
        if cli_parser.args.username == "":
            cli_parser.parser.error('--add requires --username')
        else:
            db.db_init()
    if cli_parser.args.stats:
        if cli_parser.args.username == "":
            cli_parser.parser.error('--stats requires --username')
        else:
            db.db_init()
    if cli_parser.args.rank:
        bot = Bot(constants.TELEGRAM_TOKEN)
        ranking_msg = await rank_handler.getRankingMsg()
        async with bot:
            await bot.send_message(
                chat_id=constants.GROUP_CHAT_ID,
                text=ranking_msg,
                parse_mode=ParseMode.HTML
            )

if __name__ == '__main__':
    asyncio.run(main())
