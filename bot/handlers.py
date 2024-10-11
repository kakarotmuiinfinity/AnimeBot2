import asyncio
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from .config import WELCOME_IMAGE_URL, STICKER_ID

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # React with fire emoji
    await update.message.react("🔥")
    await asyncio.sleep(2)

    # Send and then delete sticker
    sticker_message = await update.message.reply_sticker(STICKER_ID)
    await asyncio.sleep(2)
    await sticker_message.delete()

    # Send and edit loading message
    loading_message = await update.message.reply_text("▣☐☐")
    await asyncio.sleep(2)
    await loading_message.edit_text("☐▣☐")
    await asyncio.sleep(2)
    await loading_message.edit_text("☐☐▣")
    await asyncio.sleep(2)

    # Send welcome image with caption and buttons
    keyboard = [
        [InlineKeyboardButton("✇ Aɴɪᴍᴇ Gʀᴏᴜᴘ ✇", url="https://t.me/Cartoon_Heaven")],
        [InlineKeyboardButton("❁ Aɴɪᴍᴇ Cʜᴀɴɴᴇʟ ❁", url="https://t.me/Cartoon_Carnival")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    caption = f"Hᴇʟʟᴏ {update.effective_user.full_name}✨\n"
    caption += f"Mʏsᴇʟғ {context.bot.first_name}\n"
    caption += "Wᴀɴᴛ ᴛᴏ ᴡᴀᴛᴄʜ Aɴɪᴍᴇ?\n"
    caption += "I ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ Aɴɪᴍᴇ ʏᴏᴜ ᴡᴀɴᴛ!"

    await update.message.reply_photo(
        photo=WELCOME_IMAGE_URL,
        caption=caption,
        reply_markup=reply_markup
    )
