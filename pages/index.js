import { useState } from 'react';

const QA_DATA = [
  {
    id: 'cost',
    question: 'Сколько стоит разработка бота?',
    answer: 'Стоимость зависит от конкретного бота 🤖\n\nНапиши мне в личку @eacmiss — расскажи, что нужно, и я назову точную цену!'
  },
  {
    id: 'time',
    question: 'Сколько времени занимает разработка?',
    answer: 'Обычно разработка занимает 1–3 дня ⚡\n\nТочные сроки зависят от сложности проекта — пиши @eacmiss, обсудим!'
  },
  {
    id: 'payment',
    question: 'Какие способы оплаты вы принимаете?',
    answer: 'Принимаю:\n\n• Криптовалюту (USDT, BTC, ETH)\n• Банковские переводы\n• PayPal\n\n50% предоплата, 50% по завершении.'
  },
  {
    id: 'support',
    question: 'Есть ли поддержка после запуска?',
    answer: 'Да! Предоставляю:\n\n• 30 дней бесплатной поддержки после запуска\n• Пакеты постоянного обслуживания\n• Исправление ошибок и мелкие обновления включены'
  },
  {
    id: 'tech',
    question: 'Какие технологии вы используете?',
    answer: 'Работаю с:\n\n• Python (Telegram Bot API, aiogram, python-telegram-bot)\n• Node.js (telegraf)\n• Веб-технологии для мини-приложений\n• Базы данных (PostgreSQL, MongoDB, Redis)'
  }
];

const PORTFOLIO_BOTS = [
  {
    name: 'Crypto/NFT Инфо-бот',
    description: 'Курсы токенов, данные NFT-коллекций и цены газа',
    features: ['Курсы токенов', 'Статистика NFT-коллекций', 'Уведомления о ценах газа'],
    status: 'Доступен',
    url: 'https://t.me/eacmiss_crypto_bot'
  },
  {
    name: 'Рассыльщик',
    description: 'Массовая рассылка сообщений для управления сообществом',
    features: ['Отложенные сообщения', 'Сегментация пользователей', 'Аналитика'],
    status: 'Доступен',
    url: 'https://t.me/eacmiss_broadcast_bot'
  },
  {
    name: 'Сокращатель ссылок',
    description: 'Управление ссылками и отслеживание кликов',
    features: ['Свои алиасы', 'Аналитика кликов', 'QR-коды'],
    status: 'Доступен',
    url: 'https://t.me/eacmiss_shortener_bot'
  }
];

export default function Home() {
  const [activeTab, setActiveTab] = useState('home');
  const [selectedQA, setSelectedQA] = useState(null);
  const [selectedBot, setSelectedBot] = useState(null);

  const renderHome = () => (
    <div className="container">
      <h1 className="neon-title">👋 Привет!</h1>
      <p className="neon-subtitle">Это мой бот-портфолио — здесь я показываю свои работы по разработке Telegram-ботов.</p>

      <div className="card-grid">
        <div className="card neon-card" onClick={() => setActiveTab('qa')}>
          <h3>❓ Вопросы и ответы</h3>
          <p>Частые вопросы о разработке ботов</p>
        </div>
        <div className="card neon-card" onClick={() => setActiveTab('portfolio')}>
          <h3>🤖 Проекты</h3>
          <p>Посмотреть моих ботов</p>
        </div>
        <div className="card neon-card" onClick={() => window.open('https://t.me/eacmiss', '_blank')}>
          <h3>💬 Связаться</h3>
          <p>Написать @eacmiss</p>
        </div>
      </div>
    </div>
  );

  const renderQA = () => (
    <div className="container">
      <button className="back-btn" onClick={() => setActiveTab('home')}>← Назад</button>
      <h1 className="neon-title">❓ Частые вопросы</h1>

      {selectedQA ? (
        <div className="qa-answer neon-card">
          <h3>{selectedQA.question}</h3>
          <p className="answer-text">{selectedQA.answer}</p>
          <button className="btn neon-btn" onClick={() => setSelectedQA(null)}>← К вопросам</button>
        </div>
      ) : (
        <div className="qa-list">
          {QA_DATA.map(qa => (
            <div key={qa.id} className="qa-item neon-card" onClick={() => setSelectedQA(qa)}>
              <h3>{qa.question}</h3>
              <span>Нажми, чтобы увидеть ответ →</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );

  const renderPortfolio = () => (
    <div className="container">
      <button className="back-btn" onClick={() => setActiveTab('home')}>← Назад</button>
      <h1 className="neon-title">🤖 Мои проекты-боты</h1>

      {selectedBot ? (
        <div className="bot-details neon-card">
          <h2>{selectedBot.name}</h2>
          <p>{selectedBot.description}</p>
          <h3>Возможности:</h3>
          <ul>
            {selectedBot.features.map((f, i) => <li key={i}>{f}</li>)}
          </ul>
          <p className="status">Статус: {selectedBot.status}</p>
          <button className="btn neon-btn" onClick={() => window.open(selectedBot.url, '_blank')}>
            🤖 Открыть бота
          </button>
          <button className="btn neon-btn" onClick={() => setSelectedBot(null)}>← К проектам</button>
        </div>
      ) : (
        <div className="bot-list">
          {PORTFOLIO_BOTS.map((bot, i) => (
            <div key={i} className="bot-card neon-card" onClick={() => setSelectedBot(bot)}>
              <h3>{bot.name}</h3>
              <p>{bot.description}</p>
              <span className="status">Статус: {bot.status}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );

  return (
    <div className="app">
      <header className="neon-header">
        <h1 className="neon-logo">⚡ Портфолио Бот</h1>
      </header>

      <main>
        {activeTab === 'home' && renderHome()}
        {activeTab === 'qa' && renderQA()}
        {activeTab === 'portfolio' && renderPortfolio()}
      </main>
    </div>
  );
}
