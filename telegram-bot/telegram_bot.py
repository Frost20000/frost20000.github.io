from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Bot token
BOT_TOKEN = '7997181910:AAH9evzrRN0QknfBFIzdx_9sjuNqe9rKP2o'

# Command: /start or /hello
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello World!")

# Command: /about
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm a bot created by Mike Haruna!")

# Command: /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Available commands:\n/start - Say Hello\n/about - Info about me\n/help - Show help\n/fact - Get a fun fact"
    )

# Command: /fact
async def fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    facts = [
        "Honey never spoils.",
        "Bananas are berries, but strawberries aren't.",
        "A group of flamingos is called a flamboyance."
    ]
    import random
    await update.message.reply_text(random.choice(facts))

# Set up the bot and handlers
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hello", start))
app.add_handler(CommandHandler("about", about))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("fact", fact))

print("Bot is running...")
app.run_polling()
