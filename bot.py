# -*- coding: utf-8 -*-
import os
import telebot
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = '535465059:AAH8_auvLbReBgKn0ziME2gNjIrtD76cMUY'
#some_api_token = os.environ['SOME_API_TOKEN']
#             ...


#       Your bot code below
# bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)
