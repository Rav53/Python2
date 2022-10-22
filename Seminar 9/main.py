
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5793996250:AAGw_5gQrj9UrnNVEgQ6Gzv3t12_4R4MKcU").build()
# print("Server start")
app.add_handler(CommandHandler("hello", hello))

app.run_polling()