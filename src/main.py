#!/usr/bin/env python

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
    db.db_init()
    if cli_parser.args.add:
        if cli_parser.args.username != "" and cli_parser.args.id != 0:
            db.db_add_player(
                tg_id=cli_parser.args.id,
                fortnite_username=cli_parser.args.username
            )
        else:
            cli_parser.parser.error('--add requires USERNAME and ID')

    if cli_parser.args.rank:
        bot = Bot(constants.TG_BOT_TOKEN)
        ranking_msg = await rank_handler.get_ranking_msg()
        async with bot:
            await bot.send_message(
                chat_id=constants.TG_CHAT_ID,
                text=ranking_msg,
                parse_mode=ParseMode.HTML
            )

if __name__ == '__main__':
    asyncio.run(main())
