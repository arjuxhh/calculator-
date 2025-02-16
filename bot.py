from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import logging
import os

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("BOT_TOKEN")

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Send me a math expression, and I'll calculate the result!")

def calculate(update: Update, context: CallbackContext) -> None:
    expression = update.message.text
    try:
        result = eval(expression, {"__builtins__": None}, {})
        update.message.reply_text(f"Result: {result}")
    except Exception as e:
        update.message.reply_text("Invalid expression. Please send a valid math expression.")

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))
    
    application.run_polling()

if __name__ == "__main__":
    main()
  
