import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

# База вопросов и ответов
QA_DATABASE = {
    "cost": {
        "question": "Сколько стоит разработка бота?",
        "answer": "Стоимость зависит от конкретного бота 🤖\n\nНапиши мне в личку @eacmiss — расскажи, что нужно, и я назову точную цену!"
    },
    "time": {
        "question": "Сколько времени занимает разработка?",
        "answer": "Обычно разработка занимает 1–3 дня ⚡\n\nТочные сроки зависят от сложности проекта — пиши @eacmiss, обсудим!"
    },
    "payment": {
        "question": "Какие способы оплаты вы принимаете?",
        "answer": "Принимаю:\n\n• Криптовалюту (USDT, BTC, ETH)\n• Банковские переводы\n• PayPal\n\n50% предоплата, 50% по завершении."
    },
    "support": {
        "question": "Есть ли поддержка после запуска?",
        "answer": "Да! Предоставляю:\n\n• 30 дней бесплатной поддержки после запуска\n• Пакеты постоянного обслуживания\n• Исправление ошибок и мелкие обновления включены"
    },
    "tech": {
        "question": "Какие технологии вы используете?",
        "answer": "Работаю с:\n\n• Python (Telegram Bot API, aiogram, python-telegram-bot)\n• Node.js (telegraf)\n• Веб-технологии для мини-приложений\n• Базы данных (PostgreSQL, MongoDB, Redis)"
    }
}

# Портфолио ботов
PORTFOLIO_BOTS = [
    {
        "name": "Crypto/NFT Инфо-бот",
        "description": "Курсы токенов, данные NFT-коллекций и цены газа",
        "features": ["Курсы токенов", "Статистика NFT-коллекций", "Уведомления о ценах газа"],
        "status": "Доступен"
    },
    {
        "name": "Рассыльщик",
        "description": "Массовая рассылка сообщений для управления сообществом",
        "features": ["Отложенные сообщения", "Сегментация пользователей", "Аналитика"],
        "status": "Доступен"
    },
    {
        "name": "Сокращатель ссылок",
        "description": "Управление ссылками и отслеживание кликов",
        "features": ["Свои алиасы", "Аналитика кликов", "QR-коды"],
        "status": "Доступен"
    }
]

def get_webapp_url():
    return os.getenv("WEBAPP_URL", "https://example.com")

def main_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🎮 Зайди сюда, чтобы играть", web_app=WebAppInfo(url=get_webapp_url()))],
        [InlineKeyboardButton("❓ Вопросы и ответы", callback_data="qa_menu")],
        [InlineKeyboardButton("🤖 Мои проекты", callback_data="portfolio")],
        [InlineKeyboardButton("💬 Связаться с разработчиком", callback_data="contact")]
    ])

START_TEXT = (
    "👋 Привет! Это мой бот-портфолио — здесь я показываю свои работы по разработке Telegram-ботов.\n\n"
    "🎮 Зайди сюда, чтобы играть — жми кнопку ниже, откроется мини-приложение!\n\n"
    "Также можешь посмотреть проекты, почитать ответы на вопросы или связаться со мной."
)

BACK_TEXT = (
    "👋 Привет! Это мой бот-портфолио — здесь я показываю свои работы по разработке Telegram-ботов.\n\n"
    "🎮 Зайди сюда, чтобы играть — жми кнопку ниже, откроется мини-приложение!"
)

async def start(update, context):
    """Обработка команды /start"""
    await update.message.reply_text(START_TEXT, reply_markup=main_keyboard())

async def qa_menu(update, context):
    """Показать меню вопросов и ответов"""
    keyboard = [
        [InlineKeyboardButton(f"❓ {qa['question']}", callback_data=f"qa_{key}")]
        for key, qa in QA_DATABASE.items()
    ]
    keyboard.append([InlineKeyboardButton("🔙 Назад в меню", callback_data="back_main")])

    await update.callback_query.edit_message_text(
        "💡 Часто задаваемые вопросы:\n\nВыбери вопрос, чтобы увидеть ответ:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def show_qa_answer(update, context):
    """Показать ответ на конкретный вопрос"""
    query = update.callback_query
    qa_key = query.data.replace("qa_", "")

    if qa_key in QA_DATABASE:
        qa = QA_DATABASE[qa_key]
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 К вопросам", callback_data="qa_menu")],
            [InlineKeyboardButton("🏠 Главное меню", callback_data="back_main")]
        ])
        await query.edit_message_text(
            f"❓ {qa['question']}\n\n💬 {qa['answer']}",
            reply_markup=keyboard
        )

async def show_portfolio(update, context):
    """Показать портфолио ботов"""
    keyboard = [
        [InlineKeyboardButton(f"🤖 {bot['name']}", callback_data=f"bot_{i}")]
        for i, bot in enumerate(PORTFOLIO_BOTS)
    ]
    keyboard.append([InlineKeyboardButton("🔙 Назад в меню", callback_data="back_main")])

    portfolio_text = "🎯 Мои проекты-боты:\n\n"
    for bot in PORTFOLIO_BOTS:
        portfolio_text += f"• {bot['name']}\n  {bot['description']}\n  Статус: {bot['status']}\n\n"

    await update.callback_query.edit_message_text(
        portfolio_text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def show_bot_details(update, context):
    """Показать детали конкретного бота"""
    query = update.callback_query
    bot_index = int(query.data.replace("bot_", ""))
    bot = PORTFOLIO_BOTS[bot_index]

    features_text = "\n".join([f"• {f}" for f in bot['features']])

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 К проектам", callback_data="portfolio")],
        [InlineKeyboardButton("🏠 Главное меню", callback_data="back_main")]
    ])

    text = (
        f"🤖 {bot['name']}\n\n"
        f"📝 {bot['description']}\n\n"
        f"✨ Возможности:\n{features_text}\n\n"
        f"📊 Статус: {bot['status']}"
    )

    await query.edit_message_text(text, reply_markup=keyboard)

async def contact_developer(update, context):
    """Показать контакты разработчика"""
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("💬 Написать @eacmiss", url="https://t.me/eacmiss")],
        [InlineKeyboardButton("🔙 Назад в меню", callback_data="back_main")]
    ])

    await update.callback_query.edit_message_text(
        "📞 Связаться с разработчиком\n\n"
        "Есть конкретный вопрос или хочешь обсудить проект?\n\n"
        "Жми кнопку ниже, чтобы написать мне в Telegram:",
        reply_markup=keyboard
    )

async def back_main(update, context):
    """Вернуться в главное меню"""
    await update.callback_query.edit_message_text(BACK_TEXT, reply_markup=main_keyboard())

async def handle_message(update, context):
    """Обработка текстовых сообщений — поиск по вопросам и ответам"""
    user_message = update.message.text.lower()

    for key, qa in QA_DATABASE.items():
        if key in user_message or any(word in qa['question'].lower() for word in user_message.split()):
            await update.message.reply_text(
                f"❓ {qa['question']}\n\n💬 {qa['answer']}\n\n"
                "Нужна дополнительная информация? Напиши @eacmiss напрямую!"
            )
            return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("💬 Написать @eacmiss", url="https://t.me/eacmiss")],
        [InlineKeyboardButton("❓ Все вопросы", callback_data="qa_menu")]
    ])

    await update.message.reply_text(
        "Не нашёл ответ на твой вопрос в базе.\n\n"
        "По особым вопросам пиши @eacmiss напрямую!",
        reply_markup=keyboard
    )

def register_handlers(application):
    """Регистрация обработчиков для polling и webhook"""
    from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, filters

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(qa_menu, pattern="^qa_menu$"))
    application.add_handler(CallbackQueryHandler(show_qa_answer, pattern="^qa_"))
    application.add_handler(CallbackQueryHandler(show_portfolio, pattern="^portfolio$"))
    application.add_handler(CallbackQueryHandler(show_bot_details, pattern="^bot_"))
    application.add_handler(CallbackQueryHandler(contact_developer, pattern="^contact$"))
    application.add_handler(CallbackQueryHandler(back_main, pattern="^back_main$"))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
