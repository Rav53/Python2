from telegram import Update
from telegram.ext import ContextTypes
import datetime
from logi import log


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    await update.message.reply_text(f'hi {update.effective_user.first_name}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')
