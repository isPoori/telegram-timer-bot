# 🤖 Telegram Timer Bot

A beautiful and efficient Telegram bot that automatically updates profile status with stylish time display and responds to commands.

## ✨ Features

- 🕒 Real-time profile status updates with fancy fonts
- 🌍 Tehran timezone support
- 💫 Automatic online status maintenance
- ⚡ Fast response to ping commands
- 🛡️ Admin-only command system
- 🔔 Error reporting system

## 🚀 Installation

1. **Clone the repository**
```bash
git clone https://github.com/isPoori/telegram-timer-bot.git
cd telegram-timer-bot
```

2. **Install required packages**
```bash
pip install -r requirements.txt
```

### 📦 Required Packages
- pyrogram
- tgcrypto

## ⚙️ Configuration

1. Get your Telegram API credentials:
   - Visit [my.telegram.org](https://my.telegram.org)
   - Create a new application
   - Copy your `api_id` and `api_hash`

2. Open `main.py` and configure admin settings:
```python
ADMINS = [YOUR USER ID]
REPORT_USERNAME = "@YOUR USERNAME"
```

## 🎯 Usage

Run the bot:
```bash
python3 main.py
```

### 📝 Available Commands
- `/ping` - Check if bot is alive
- `#ping` - Alternative ping command
- `!ping` - Alternative ping command
- `.ping` - Alternative ping command
- `ping` - Alternative ping command
- `Ping` - Alternative ping command
- `bot` - Alternative ping command
- `omga` - Alternative ping command
- `ربات` - Persian ping command

## 👨‍💻 Developer

**Pouria Hosseini**
- 📧 Email: [PouriDev@gmail.com]
- 🌐 GitHub: [@isPoori]
- 📱 Telegram: [@isPoori]

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/isPoori/telegram-timer-bot.git/issues).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Support

If you found this project helpful, please give it a star! ⭐

## 🙏 Acknowledgments

Special thanks to:
- Telegram for providing the API
- Pyrogram team for their amazing library
- All contributors who help improve this project

---
Made with ❤️ by Pouria Hosseini
