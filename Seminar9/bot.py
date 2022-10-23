from telegram.ext import ApplicationBuilder, CommandHandler
from bot_commands import hi_command
from bot_commands import time_command
from bot_commands import help_command
from bot_commands import sum_command


app = ApplicationBuilder().token("5793996250:AAGw_5gQrj9UrnNVEgQ6Gzv3t12_4R4MKcU").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

print('Sever start')
app.run_polling()
