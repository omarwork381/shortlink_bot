import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ضع هنا التوكن الخاص بك
TELEGRAM_TOKEN = '7716810141:AAHfQJo6SD2f7-Gr2Zz6QzIYr4eA0tao8oM'  # Place your token here

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """يتم تنفيذ هذه الدالة عند بدء المحادثة مع البوت"""
    await update.message.reply_text("مرحبًا! أرسل لي أي رابط لأقوم بتقصيره.")

async def shorten_url(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """يتم تنفيذ هذه الدالة عندما يرسل المستخدم رابطًا"""
    long_url = update.message.text

    # نستخدم TinyURL API لتقصير الرابط
    response = requests.get(f'http://tinyurl.com/api-create.php?url={long_url}')
    
    if response.status_code == 200:
        short_url = response.text
        await update.message.reply_text(f'الرابط المختصر: {short_url}')
    else:
        await update.message.reply_text('حدث خطأ أثناء محاولة تقصير الرابط.')

def main():
    # إعداد البوت باستخدام Application بدلاً من Updater
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # إضافة الأوامر والمعالجات للبوت
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, shorten_url))

    # تشغيل البوت
    application.run_polling()

if __name__ == '__main__':
    main()
