import asyncio
from telegram.ext import Application, CommandHandler
from bot.config import BOT_TOKEN
from bot.handlers import start

async def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    await application.initialize()
    await application.start()
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
