import logging
from telegram.ext import Application, CommandHandler
import os

# Логирование для отладки
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)
logger.info("Бот стартовал")

# Токен бота
TOKEN = os.getenv("7776537523:AAEbw4JzuTZW3G5UiDgrwpCgH3G4mpZXziE")
if not TOKEN:
    logger.error("Токен не найден!")
    raise ValueError("Токен не найден!")

# Webhook URL (будет задан на Render)
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Команда /start
async def start(update, context):
    logger.info("Получена команда /start")
    await update.message.reply_text("Привет! Я твой бот, работаю на Render.com!")

def main():
    logger.info("Настройка приложения")
    # Создаём приложение
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчик /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем webhook
    logger.info("Запуск webhook")
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),  # Render задаёт PORT
        url_path="/webhook",
        webhook_url=WEBHOOK_URL
    )

if __name__ == "__main__":
    main()
