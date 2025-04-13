from confic import TOKEN
from PIL import Image, ImageOps  # Install pillow instead of PIL
from logic import detect_bird
import telebot
import telebot

bot = telebot.TeleBot(TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    image=Image.open(file_name)
    result, score = detect_bird(image)
    bot.reply_to(message, result + '\n' + str(score))
    if result.startswith('яблоко'):
        bot.send_message(message.chat.id,'Это яблоко!! Оно очень вкусное!')
    elif result.startswith('хлеб'):
        bot.send_message(message.chat.id,'Это хлеб!! Он очень вкусное!')
    elif result.startswith('апельсин'):
        bot.send_message(message.chat.id,'Это апельсин!! Он очень вкусное!')
    elif result.startswith('банан'):
        bot.send_message(message.chat.id,'Это банан!! Он очень вкусное!')
    elif result.startswith('мясо'):
        bot.send_message(message.chat.id,'Это мясо!! Оно очень вкусное!')
    elif result.startswith('морковь'):
        bot.send_message(message.chat.id,'Это морковь!! Она очень вкусное!')
    elif result.startswith('лук'):
        bot.send_message(message.chat.id,'Это лук!! Он очень вкусное!')
    elif result.startswith('молоко'):
        bot.send_message(message.chat.id,'Это молоко!! Оно очень вкусное!')
    elif result.startswith('огурец'):
        bot.send_message(message.chat.id,'Это огурец!! Он очень вкусное!')
    elif result.startswith('креветка'):
        bot.send_message(message.chat.id,'Это креветка!! Она очень вкусное!')



bot.infinity_polling()