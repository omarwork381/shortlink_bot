import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Use os.environ to fetch the token from the environment
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Executes when the conversation with the bot starts."""
    await update.message.reply_text("مرحبًا! أرسل لي أي رابط لأقوم بتقصيره.")

async def shorten_url(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Executes when the user sends a link."""
    long_url = update.message.text

    # Use TinyURL API to shorten the link
    response = requests.get(f'http://tinyurl.com/api-create.php?url={long_url}')
    
    if response.status_code == 200:
        short_url = response.text
        await update.message.reply_text(f'الرابط المختصر: {short_url}')
    else:
        await update.message.reply_text('حدث خطأ أثناء محاولة تقصير الرابط.')

def main():
    # Set up the bot using Application
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Add commands and handlers to the bot
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, shorten_url))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
