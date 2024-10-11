from .config import WELCOME_IMAGE_URL, STICKER_ID
await update.message.reply_photo(
    photo=WELCOME_IMAGE_URL,
    caption=caption,
    reply_markup=reply_markup
)
