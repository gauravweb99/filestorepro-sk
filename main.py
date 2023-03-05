import asyncio
from bot import Bot
from config import MULITPLE_BOT_TOKENS
from nest_asyncio import apply
from pyrogram import idle


apply()

if __name__ == "__main__":

    async def start_bots():
        bots = []
        for token in MULITPLE_BOT_TOKENS:
            bot = Bot(bot_token=token)
            await bot.start()
            bots.append(bot)

        await idle()

        for app in bots:
            await app.stop()

    asyncio.run(start_bots())