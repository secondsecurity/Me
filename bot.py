from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# 🔑 توکن رباتت از BotFather
TOKEN = "8138562324:AAGS_gDrqdGud9F5u_SzYoaS-DWN9UQsf3U"


# ---------- پیام‌ها ----------
async def reply_to_salam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    # اگر کاربر گفت "سلام"
    if text == "سلام":
        await update.message.reply_text("سلام 👋 خوش اومدی!")


# ---------- ساخت ربات ----------
app = ApplicationBuilder().token(TOKEN).build()

# فقط پیام‌های متنی رو بگیر
app.add_handler(MessageHandler(filters.TEXT, reply_to_salam))


# ---------- اجرا ----------
app.run_polling()
