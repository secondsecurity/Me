import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# 🔑 توکن جدیدت رو بذار (حتماً عوضش کن!)
TOKEN = "8138562324:AAGS_gDrqdGud9F5u_SzYoaS-DWN9UQsf3U"

OWNER_ID = 1656844563


# ---------- notify owner ----------
async def notify_owner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.effective_user

        name = user.full_name
        username = user.username if user.username else "نداره"
        user_id = user.id

        msg = (
            "🚀 یه نفر بات رو استارت کرد!\n\n"
            f"👤 اسم: {name}\n"
            f"🆔 آیدی: {user_id}\n"
            f"📛 یوزرنیم: @{username}"
        )

        await context.bot.send_message(chat_id=OWNER_ID, text=msg)
    except Exception as e:
        print("Notify error:", e)


# ---------- /start ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await notify_owner(update, context)

    await update.message.reply_text(
        "خوش اومدی 👋\n\n"
        "دستورات:\n"
        "joke\nquote\nroast\nlove\nmood\nhelp"
    )


# ---------- commands ----------
async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("😂 میدونی ماهی‌ها به آبجی‌شون چی میگن؟... آبزی")

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💭 زندگی ساده‌تر از چیزیه که فکر می‌کنی")

async def roast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 هنوز آماده رُست کردن نیستم 😄")

async def love(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❤️ عشق قشنگه ولی واقعی باشه")

async def mood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🙂 حالت چطوره؟ امیدوارم عالی باشی")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start\njoke\nquote\nroast\nlove\nmood\nhelp"
    )


# ---------- text handler ----------
async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
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
        else:
            await update.message.reply_text("دستور رو درست وارد کن 🙃")
    except Exception as e:
        print("Handler error:", e)


# ---------- build bot ----------
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))


# ---------- keep alive (برای Render) ----------
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


# ---------- run forever (ضد کرش) ----------
while True:
    try:
        print("Bot started...")
        app.run_polling(
            poll_interval=3,
            timeout=30,
            drop_pending_updates=True
        )
    except Exception as e:
        print("CRASH:", e)
