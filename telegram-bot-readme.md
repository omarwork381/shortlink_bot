# Telegram URL Shortener Bot | بوت تقصير الروابط على تيليجرام

A simple Telegram bot that shortens URLs using the TinyURL API.
بوت تيليجرام بسيط لتقصير الروابط باستخدام TinyURL API.

## Features | المميزات

- Shortens any valid URL using TinyURL service
- Simple and easy to use interface
- Instant response with shortened URL
- Supports any valid web link

تقصير أي رابط صالح باستخدام خدمة TinyURL -
واجهة بسيطة وسهلة الاستخدام -
استجابة فورية مع الرابط المختصر -
يدعم أي رابط ويب صالح -

## Requirements | المتطلبات

```
python-telegram-bot>=20.0
requests>=2.28.0
```

## Setup | التثبيت

1. Clone this repository | انسخ هذا المستودع
```bash
git clone https://github.com/yourusername/telegram-url-shortener.git
cd telegram-url-shortener
```

2. Install dependencies | تثبيت المكتبات المطلوبة
```bash
pip install -r requirements.txt
```

3. Create a Telegram bot and get your token | إنشاء بوت تيليجرام والحصول على التوكن
- Message [@BotFather](https://t.me/BotFather) on Telegram
- Create a new bot using the `/newbot` command
- Copy your bot token

4. Configure the bot | تكوين البوت
- Open `main.py`
- Replace `TELEGRAM_TOKEN` with your bot token:
```python
TELEGRAM_TOKEN = 'your-token-here'
```

5. Run the bot | تشغيل البوت
```bash
python main.py
```

## Usage | طريقة الاستخدام

1. Start a chat with your bot on Telegram | ابدأ محادثة مع البوت على تيليجرام
2. Send `/start` to begin | أرسل `/start` للبدء
3. Send any URL to get a shortened version | أرسل أي رابط للحصول على نسخة مختصرة منه

## Code Structure | هيكل الكود

- `main.py`: Main bot script containing all the logic
- `requirements.txt`: List of Python dependencies
- `README.md`: Documentation file (this file)

## Functions | الدوال

### start()
Handles the /start command and sends a welcome message.
تتعامل مع أمر /start وترسل رسالة ترحيبية.

### shorten_url()
Handles incoming messages containing URLs and returns shortened versions.
تتعامل مع الرسائل الواردة التي تحتوي على روابط وتعيد إصدارات مختصرة منها.

## Error Handling | معالجة الأخطاء

The bot includes basic error handling for:
يتضمن البوت معالجة أساسية للأخطاء:

- Invalid URLs | الروابط غير الصالحة
- API connection issues | مشاكل الاتصال بـ API
- Service unavailability | عدم توفر الخدمة

## Contributing | المساهمة

Feel free to fork this repository and submit pull requests to contribute to this project.
لا تتردد في عمل fork للمستودع وتقديم pull requests للمساهمة في هذا المشروع.

## License | الترخيص

This project is licensed under the MIT License - see the LICENSE file for details.
هذا المشروع مرخص تحت رخصة MIT - راجع ملف LICENSE للتفاصيل.

## Support | الدعم

For support, please open an issue in the GitHub repository.
للدعم، يرجى فتح issue في مستودع GitHub.
