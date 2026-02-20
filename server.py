from flask import Flask
import threading
import bot  # это твой основной файл с ботом

app = Flask(__name__)

@app.route('/')
def home():
    return "Бот работает!"

@app.route('/health')
def health():
    return "OK", 200

# Запускаем бота в отдельном потоке
def run_bot():
    bot.bot.infinity_polling()

thread = threading.Thread(target=run_bot)
thread.daemon = True
thread.start()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)