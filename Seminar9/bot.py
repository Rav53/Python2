from telegram.ext import ApplicationBuilder, CommandHandler
from bot_commands import hi_command
from bot_commands import time_command
from bot_commands import help_command
from bot_commands import sum_command
from bot_commands import vovan_command

app = ApplicationBuilder().token("5757263924:AAFJZIuluc7KVZ24_sGv-JK4UYU8hC9ATYE").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("vovan", vovan_command))

print('Sever start')
app.run_polling()
