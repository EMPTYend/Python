import telebot
import random
# Api BotTelegram
bot = telebot.TeleBot('6840066899:AAEWbUwsYICrL6gt2SDZJVb4yx-UHYp2NjY')
  
# Список вариантов
OPTIONS = ['камень', 'ножницы', 'бумага']

# Функция для обработки команды /start или /help
@bot.message_handler(commands=['start', 'help'])
def send_instructions(message):
    instructions = f"Привет!{message.from_user.first_name} {message.from_user.last_name}, Давай сыграем в игру 'камень, ножницы, бумага'. Просто отправь мне свой выбор!"
    bot.reply_to(message, instructions)

# Функция для обработки сообщений с вариантами пользователя
@bot.message_handler(func=lambda message: True)
def play_game(message):
    user_choice = message.text.lower().strip()

    # Проверяем, что выбор пользователя корректный
    if user_choice not in OPTIONS:
        bot.reply_to(message, "Пожалуйста, выбери один из вариантов: камень, ножницы или бумага.")
        return

    # Рандомный выбор бота
    bot_choice = random.choice(OPTIONS)

    # Сравниваем выборы и определяем победителя
    if user_choice == bot_choice:
        result = "Ничья!"
    elif (user_choice == 'камень' and bot_choice == 'ножницы') or \
         (user_choice == 'ножницы' and bot_choice == 'бумага') or \
         (user_choice == 'бумага' and bot_choice == 'камень'):
        result = "Ты победил! Бот выбрал: " + bot_choice
    else:
        result = "Бот победил! Бот выбрал: " + bot_choice

    # Отправляем результат пользователю
    bot.reply_to(message, result)
        
#bot.infinity_polling()
bot.polling(none_stop=True)