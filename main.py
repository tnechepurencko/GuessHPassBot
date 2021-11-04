import random
import telebot

bot = telebot.TeleBot('2061807493:AAGp5GxwU-Es6sO9tFMaa6sK2YF3rhLBdCo')


class Password:
    def __init__(self):
        self.password = random.randint(1, 100000000)

    def change_password(self):
        self.password = random.randint(1, 100000000)


password = Password()


@bot.message_handler(content_types=['text', 'document', 'audio'])  # получает
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Hint: the password consists of integers")
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Guess the password -> get the channel link! That's easy!")
    elif message.text == str(password.password):
        bot.send_message(message.from_user.id, "Congratulations! Resend this message to @pinkgoos, "
                                               "and she gives you the invitation link!")
    else:
        bot.send_message(message.from_user.id, "Wrong password! Try again!")
    password.change_password()


bot.polling(none_stop=True, interval=0)