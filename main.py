import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Load token
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Supremesaint AI core
def ask_ai(text):
    return f"Supremesaint: {text}"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Supremesaint AI is ONLINE 🔥")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.text
    reply = ask_ai(user)
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle))

print("Supremesaint running...")
app.run_polling()
