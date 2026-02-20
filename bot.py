import telebot
import schedule
import time
import threading
import random

# ============== ТВОИ ДАННЫЕ ==============
TOKEN = "8572567290:AAF45D7twXa3uz8hKqeEoE7XyiHeap3Htdk"  
CHAT_ID = "-1003713334432"  
# =========================================

bot = telebot.TeleBot(TOKEN)

topics = [
    "🍫 Шоколад или карамель?",
    "☕ Кофе или чай?",
    "🐱 Кошки или собаки?",
    "🎬 Какой фильм посоветуете на вечер?",
    "🌊 Море или горы?",
    "🍕 Любимая пицца?",
    "🎵 Что в плейлисте?",
    "💼 Как прошёл день?"
]

def send_topic():
    topic = random.choice(topics)
    bot.send_message(CHAT_ID, f"🌙 Вечерний вопрос\n\n{topic}\n\nНе забудьте про норму!")
    print(f"✅ Отправили: {topic}")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для вечерних тем 🤖")

@bot.message_handler(commands=['chatid'])
def send_chatid(message):
    bot.reply_to(message, f"ID этого чата: {message.chat.id}")

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Запуск планировщика
#schedule.every().day.at("22:00").do(send_topic)
schedule.every().minute.do(send_topic)  # тестовая отправка КАЖДУЮ МИНУТУ
thread = threading.Thread(target=run_schedule)
thread.start()

print("🚀 Бот запущен!")
#bot.infinity_polling()