
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import os

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8138562324:AAH13BWZG-VJnnMmjjPu9U2TP7yZQZJWoh4"

# ---------- /start ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "خوش اومدی 👋\n\n"
        "دستورات ربات ایناست:\n"
        "Joke\n"
        "Quote\n"
        "Roast\n"
        "Love\n"
        "Mood\n"
        "help"
    )

# ---------- handlers ----------
async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("😂 هنوز جوک ندارم ولی بعداً اضافه میشه")

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💭 زندگی ساده‌تر از چیزیه که فکر می‌کنی")

async def roast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 هنوز آماده رُست کردن نیستم 😄")

async def love(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❤️ عشق قشنگه ولی باید واقعی باشه")

async def mood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🙂 حالت خوبه؟ امیدوارم روزت عالی باشه")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "دستورات:\n"
        "/start\n"
        "joke\n"
        "quote\n"
        "roast\n"
        "love\n"
        "mood\n"
        "help"
    )

# ---------- text fallback ----------
async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if text == "joke":
        await joke(update, context)
    elif text == "quote":
        await quote(update, context)
    elif text == "roast":
        await roast(update, context)
    elif text == "love":
        await love(update, context)
    elif text == "mood":
        await mood(update, context)
    elif text == "help":
        await help_cmd(update, context)

# ---------- bot ----------
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, text_handler))

# ---------- keep alive server ----------
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

def run_web():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()

threading.Thread(target=run_web, daemon=True).start()

# ---------- run ----------
app.run_polling()
