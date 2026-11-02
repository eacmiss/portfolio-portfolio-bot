import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
from fastapi import FastAPI, Request
import json

load_dotenv()

# Q&A Database
QA_DATABASE = {
    "cost": {
        "question": "How much does bot development cost?",
        "answer": "Bot development costs vary based on complexity:\n\n• Simple bot: $100-300\n• Medium complexity: $300-800\n• Advanced features: $800-2000+\n\nContact @eacmiss for a personalized quote!"
    },
    "time": {
        "question": "How long does it take to develop a bot?",
        "answer": "Development timeline depends on the project:\n\n• Simple bot: 1-3 days\n• Medium complexity: 1-2 weeks\n• Advanced features: 2-4 weeks\n\nRush delivery is available at additional cost."
    },
    "payment": {
        "question": "What payment methods do you accept?",
        "answer": "I accept:\n\n• Cryptocurrency (USDT, BTC, ETH)\n• Bank transfers\n• PayPal\n\n50% upfront, 50% upon completion."
    },
    "support": {
        "question": "Do you provide post-launch support?",
        "answer": "Yes! I provide:\n\n• 30 days free support after launch\n• Ongoing maintenance packages available\n• Bug fixes and minor updates included"
    },
    "tech": {
        "question": "What technologies do you use?",
        "answer": "I work with:\n\n• Python (Telegram Bot API, aiogram, python-telegram-bot)\n• Node.js (telegraf)\n• Web technologies for mini apps\n• Databases (PostgreSQL, MongoDB, Redis)"
    }
}

# Portfolio Bots
PORTFOLIO_BOTS = [
    {
        "name": "Crypto/NFT Token Info",
        "description": "Instant token prices, NFT collection data, and gas prices",
        "features": ["Token price lookup", "NFT collection stats", "Gas price alerts"],
        "status": "Available"
    },
    {
        "name": "Broadcast Messenger",
        "description": "Mass messaging tool for community management",
        "features": ["Scheduled messages", "User segmentation", "Analytics"],
        "status": "Available"
    },
    {
        "name": "URL Shortener",
        "description": "Link management and click tracking service",
        "features": ["Custom aliases", "Click analytics", "QR codes"],
        "status": "Available"
    }
]

app = FastAPI()

# Initialize bot application
bot_app = None

def get_bot_app():
    global bot_app
    if bot_app is None:
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        if not token:
            raise ValueError("TELEGRAM_BOT_TOKEN not found")
        bot_app = Application.builder().token(token).build()
        
        # Register handlers
        bot_app.add_handler(CommandHandler("start", start))
        bot_app.add_handler(CallbackQueryHandler(qa_menu, pattern="^qa_menu$"))
        bot_app.add_handler(CallbackQueryHandler(show_qa_answer, pattern="^qa_"))
        bot_app.add_handler(CallbackQueryHandler(show_portfolio, pattern="^portfolio$"))
        bot_app.add_handler(CallbackQueryHandler(show_bot_details, pattern="^bot_"))
        bot_app.add_handler(CallbackQueryHandler(contact_developer, pattern="^contact$"))
        bot_app.add_handler(CallbackQueryHandler(back_main, pattern="^back_main$"))
        bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    return bot_app

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    keyboard = [
        [InlineKeyboardButton("🌐 Open Mini App", web_app=WebAppInfo(url=os.getenv("WEBAPP_URL", "https://example.com")))],
        [InlineKeyboardButton("❓ View Q&A", callback_data="qa_menu")],
        [InlineKeyboardButton("🤖 My Portfolio", callback_data="portfolio")],
        [InlineKeyboardButton("💬 Contact Developer", callback_data="contact")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "👋 Welcome to my Portfolio Bot!\n\n"
        "I showcase my Telegram bot development work. "
        "Explore my projects, check FAQs, or contact me directly.\n\n"
        "Click the button below to open the mini app!",
        reply_markup=reply_markup
    )

async def qa_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show Q&A menu"""
    keyboard = []
    for key, qa in QA_DATABASE.items():
        keyboard.append([InlineKeyboardButton(f"❓ {qa['question']}", callback_data=f"qa_{key}")])
    keyboard.append([InlineKeyboardButton("🔙 Back to Main Menu", callback_data="back_main")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query = update.callback_query
    await query.edit_message_text(
        "💡 Frequently Asked Questions:\n\nSelect a question to see the answer:",
        reply_markup=reply_markup
    )

async def show_qa_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show specific Q&A answer"""
    query = update.callback_query
    qa_key = query.data.replace("qa_", "")
    
    if qa_key in QA_DATABASE:
        qa = QA_DATABASE[qa_key]
        keyboard = [
            [InlineKeyboardButton("🔙 Back to Q&A", callback_data="qa_menu")],
            [InlineKeyboardButton("🏠 Main Menu", callback_data="back_main")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            f"❓ {qa['question']}\n\n💬 {qa['answer']}",
            reply_markup=reply_markup
        )

async def show_portfolio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show portfolio of bots"""
    keyboard = []
    for i, bot in enumerate(PORTFOLIO_BOTS):
        keyboard.append([InlineKeyboardButton(f"🤖 {bot['name']}", callback_data=f"bot_{i}")])
    keyboard.append([InlineKeyboardButton("🔙 Back to Main Menu", callback_data="back_main")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query = update.callback_query
    portfolio_text = "🎯 My Bot Portfolio:\n\n"
    for bot in PORTFOLIO_BOTS:
        portfolio_text += f"• {bot['name']}\n  {bot['description']}\n  Status: {bot['status']}\n\n"
    
    await query.edit_message_text(portfolio_text, reply_markup=reply_markup)

async def show_bot_details(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show details of a specific bot"""
    query = update.callback_query
    bot_index = int(query.data.replace("bot_", ""))
    bot = PORTFOLIO_BOTS[bot_index]
    
    features_text = "\n".join([f"• {f}" for f in bot['features']])
    
    keyboard = [
        [InlineKeyboardButton("🔙 Back to Portfolio", callback_data="portfolio")],
        [InlineKeyboardButton("🏠 Main Menu", callback_data="back_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    text = f"🤖 {bot['name']}\n\n" \
           f"📝 {bot['description']}\n\n" \
           f"✨ Features:\n{features_text}\n\n" \
           f"📊 Status: {bot['status']}"
    
    await query.edit_message_text(text, reply_markup=reply_markup)

async def contact_developer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show contact information"""
    keyboard = [
        [InlineKeyboardButton("💬 Message @eacmiss", url="https://t.me/eacmiss")],
        [InlineKeyboardButton("🔙 Back to Main Menu", callback_data="back_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query = update.callback_query
    await query.edit_message_text(
        "📞 Contact Developer\n\n"
        "Have a specific question or want to discuss a project?\n\n"
        "Click below to send me a direct message on Telegram:",
        reply_markup=reply_markup
    )

async def back_main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Return to main menu"""
    keyboard = [
        [InlineKeyboardButton("🌐 Open Mini App", web_app=WebAppInfo(url=os.getenv("WEBAPP_URL", "https://example.com")))],
        [InlineKeyboardButton("❓ View Q&A", callback_data="qa_menu")],
        [InlineKeyboardButton("🤖 My Portfolio", callback_data="portfolio")],
        [InlineKeyboardButton("💬 Contact Developer", callback_data="contact")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query = update.callback_query
    await query.edit_message_text(
        "👋 Welcome to my Portfolio Bot!\n\n"
        "I showcase my Telegram bot development work. "
        "Explore my projects, check FAQs, or contact me directly.",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle text messages - search in Q&A"""
    user_message = update.message.text.lower()
    
    # Search for matching Q&A
    for key, qa in QA_DATABASE.items():
        if key in user_message or any(word in qa['question'].lower() for word in user_message.split()):
            await update.message.reply_text(
                f"❓ {qa['question']}\n\n💬 {qa['answer']}\n\n"
                "Need more info? Contact @eacmiss directly!"
            )
            return
    
    # If no match found
    keyboard = [
        [InlineKeyboardButton("💬 Message @eacmiss", url="https://t.me/eacmiss")],
        [InlineKeyboardButton("❓ View All Q&A", callback_data="qa_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "I couldn't find an answer to your question in my database.\n\n"
        "For specific inquiries, please contact @eacmiss directly!",
        reply_markup=reply_markup
    )

@app.post("/webhook")
async def webhook(request: Request):
    """Handle Telegram webhook"""
    application = get_bot_app()
    data = await request.json()
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"status": "bot is running"}
