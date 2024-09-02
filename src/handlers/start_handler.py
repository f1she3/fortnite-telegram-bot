from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode, ChatAction


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(
        f"⚡ Welcome @{update.effective_user.username} !\n\n"
        f"🤖 I'm a <a href='https://www.fortnite.com/'>Fornite</a> bot that allows you to check your in-game stats & get the latest news.\n\n"
        f"🔗 To get started, link your Fortnite account using\n"
        f"/link <i>fortnite_username</i>\n\n"
        f"❔ For more help use /help"
    )
