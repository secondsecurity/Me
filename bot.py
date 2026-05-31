from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8138562324:AAHEQu6m4bOXXhLZH4AKePp-wlybXRY78DQ"

# --- Telegram bot logic ---
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "سلام" in text:
        await update.message.reply_text("سلام 👋")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, reply))

# --- Web server (for Render port requirement) ---
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

def run_web():
    server = HTTPServer(("0.0.0.0", 10000), Handler)
    server.serve_forever()

threading.Thread(target=run_web, daemon=True).start()

# --- Start bot ---
app.run_polling()
