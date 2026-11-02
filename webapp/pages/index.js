import { useState } from 'react';

const QA_DATA = [
  {
    id: 'cost',
    question: 'How much does bot development cost?',
    answer: 'Bot development costs vary based on complexity:\n\n• Simple bot: $100-300\n• Medium complexity: $300-800\n• Advanced features: $800-2000+\n\nContact @eacmiss for a personalized quote!'
  },
  {
    id: 'time',
    question: 'How long does it take to develop a bot?',
    answer: 'Development timeline depends on the project:\n\n• Simple bot: 1-3 days\n• Medium complexity: 1-2 weeks\n• Advanced features: 2-4 weeks\n\nRush delivery is available at additional cost.'
  },
  {
    id: 'payment',
    question: 'What payment methods do you accept?',
    answer: 'I accept:\n\n• Cryptocurrency (USDT, BTC, ETH)\n• Bank transfers\n• PayPal\n\n50% upfront, 50% upon completion.'
  },
  {
    id: 'support',
    question: 'Do you provide post-launch support?',
    answer: 'Yes! I provide:\n\n• 30 days free support after launch\n• Ongoing maintenance packages available\n• Bug fixes and minor updates included'
  },
  {
    id: 'tech',
    question: 'What technologies do you use?',
    answer: 'I work with:\n\n• Python (Telegram Bot API, aiogram, python-telegram-bot)\n• Node.js (telegraf)\n• Web technologies for mini apps\n• Databases (PostgreSQL, MongoDB, Redis)'
  }
];

const PORTFOLIO_BOTS = [
  {
    name: 'Crypto/NFT Token Info',
    description: 'Instant token prices, NFT collection data, and gas prices',
    features: ['Token price lookup', 'NFT collection stats', 'Gas price alerts'],
    status: 'Available'
  },
  {
    name: 'Broadcast Messenger',
    description: 'Mass messaging tool for community management',
    features: ['Scheduled messages', 'User segmentation', 'Analytics'],
    status: 'Available'
  },
  {
    name: 'URL Shortener',
    description: 'Link management and click tracking service',
    features: ['Custom aliases', 'Click analytics', 'QR codes'],
    status: 'Available'
  }
];

export default function Home({ theme, toggleTheme }) {
  const [activeTab, setActiveTab] = useState('home');
  const [selectedQA, setSelectedQA] = useState(null);
  const [selectedBot, setSelectedBot] = useState(null);

  const renderHome = () => (
    <div className="container">
      <h1>👋 Welcome</h1>
      <p>I showcase my Telegram bot development work. Explore my projects, check FAQs, or contact me directly.</p>
      
      <div className="card-grid">
        <div className="card" onClick={() => setActiveTab('qa')}>
          <h3>❓ Q&A</h3>
          <p>Frequently asked questions about bot development</p>
        </div>
        <div className="card" onClick={() => setActiveTab('portfolio')}>
          <h3>🤖 Portfolio</h3>
          <p>View my bot projects</p>
        </div>
        <div className="card" onClick={() => window.open('https://t.me/eacmiss', '_blank')}>
          <h3>💬 Contact</h3>
          <p>Message @eacmiss</p>
        </div>
      </div>
    </div>
  );

  const renderQA = () => (
    <div className="container">
      <button className="back-btn" onClick={() => setActiveTab('home')}>← Back</button>
      <h1>❓ Frequently Asked Questions</h1>
      
      {selectedQA ? (
        <div className="qa-answer">
          <h3>{selectedQA.question}</h3>
          <p className="answer-text">{selectedQA.answer}</p>
          <button className="btn" onClick={() => setSelectedQA(null)}>← Back to Questions</button>
        </div>
      ) : (
        <div className="qa-list">
          {QA_DATA.map(qa => (
            <div key={qa.id} className="qa-item" onClick={() => setSelectedQA(qa)}>
              <h3>{qa.question}</h3>
              <span>Click to view answer →</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );

  const renderPortfolio = () => (
    <div className="container">
      <button className="back-btn" onClick={() => setActiveTab('home')}>← Back</button>
      <h1>🤖 My Bot Portfolio</h1>
      
      {selectedBot ? (
        <div className="bot-details">
          <h2>{selectedBot.name}</h2>
          <p>{selectedBot.description}</p>
          <h3>Features:</h3>
          <ul>
            {selectedBot.features.map((f, i) => <li key={i}>{f}</li>)}
          </ul>
          <p className="status">Status: {selectedBot.status}</p>
          <button className="btn" onClick={() => setSelectedBot(null)}>← Back to Portfolio</button>
        </div>
      ) : (
        <div className="bot-list">
          {PORTFOLIO_BOTS.map((bot, i) => (
            <div key={i} className="bot-card" onClick={() => setSelectedBot(bot)}>
              <h3>{bot.name}</h3>
              <p>{bot.description}</p>
              <span className="status">Status: {bot.status}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );

  return (
    <div className="app">
      <header>
        <h1>Portfolio Bot</h1>
        <button className="theme-toggle" onClick={toggleTheme}>
          {theme === 'light' ? '🌙' : '☀️'}
        </button>
      </header>
      
      <main>
        {activeTab === 'home' && renderHome()}
        {activeTab === 'qa' && renderQA()}
        {activeTab === 'portfolio' && renderPortfolio()}
      </main>
    </div>
  );
}
