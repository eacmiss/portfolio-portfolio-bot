# 🤖 Портфолио Бот

Telegram бот для демонстрации моих проектов по разработке ботов с Q&A интерфейсом и мини-приложением.

## ✨ Возможности

- **Q&A Секция** - Часто задаваемые вопросы о разработке ботов
- **Интерактивное меню** - Удобная навигация
- **Мини-приложение (Web App)** - Современный интерфейс с темной/светлой темой
- **Портфолио проектов** - Демонстрация других ботов
- **Связь с разработчиком** - Прямая ссылка на @eacmiss

## 📦 Установка

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd portfolio-bot
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл `.env`:
```bash
cp .env.example .env
```

4. Добавьте токен бота в `.env`:
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
WEBAPP_URL=https://your-vercel-app.vercel.app
```

## 🚀 Запуск

### Локально (polling):
```bash
python src/bot.py
```

### На Vercel (webhook):
1. Разверните на Vercel
2. Установите webhook:
```bash
curl -F "url=https://your-app.vercel.app/api/webhook" https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook
```

## 📁 Структура проекта

```
portfolio-bot/
├── src/
│   └── bot.py          # Основной код бота
├── api/
│   └── webhook.py      # Webhook для Vercel
├── pages/              # Мини-приложение (Next.js)
├── styles/
├── package.json
├── requirements.txt
└── .env.example
```

## 🎨 Мини-приложение

Мини-приложение построено на Next.js и включает:
- Переключение тем (светлая/тёмная)
- Q&A секция с поиском
- Портфолио проектов
- Адаптивный дизайн

## 📝 Вопросы и ответы

Бот содержит готовые ответы на частые вопросы:
- Стоимость разработки
- Сроки выполнения
- Способы оплаты
- Пост-поддержка
- Используемые технологии

## 👨‍💻 Разработчик

Разработано @eacmiss

## 📄 Лицензия

MIT License
