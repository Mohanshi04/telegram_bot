import os
import django
from telegram.ext import ApplicationBuilder, CommandHandler
from decouple import config
from asgiref.sync import sync_to_async

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "telegram_bot.settings")
django.setup()

from api.models import TelegramUser

@sync_to_async
def register_user(username, telegram_id):
    obj, created = TelegramUser.objects.get_or_create(telegram_id=telegram_id)
    if created:
        obj.username = username
        obj.save()

async def start(update, context):
    user = update.effective_user
    username = user.username or user.first_name or "Anonymous"
    telegram_id = user.id
    await register_user(username, telegram_id)
    await update.message.reply_text(f"Hello {username}, you are registered!")


def main():
    token = config("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
