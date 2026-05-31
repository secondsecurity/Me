from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8138562324:AAHEQu6m4bOXXhLZH4AKePp-wlybXRY78DQ"

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if "سلام" in text:
        await update.message.reply_text("سلام 👋")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, reply))

app.run_polling()
