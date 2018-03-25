import requests
import os
import telebot
from decoder import *


TOKEN = os.environ['TELEGRAM_TOKEN']
CLOUD_API = os.environ['CLOUD_TOKEN']

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    if 'найди' or 'поиск' in message:
        bot.send_message(message.chat.id, 'Начинаю парсинг клиентов по запросу')
    else:
        bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    file_info = bot.get_file(message.voice.file_id)
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path))
    try:
        # обращение к нашему новому модулю
        text = speech_to_text(bytes=file.content)
        bot.send_message(message.chat.id, 'Распознал команду ' + text)
    except SpeechException:
        bot.send_message(message.chat.id, 'Извините, не удалось распознать запрос')
    else:
        bot.send_message(message.chat.id, 'Почему-то выпал в блок else!')

if __name__ == '__main__':
     bot.polling(none_stop=True)
