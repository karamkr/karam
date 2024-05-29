
import telebot
from telebot import types,util
from flask import Flask, request 
from threading import Thread

app = Flask(  )

took = "7015496456:AAE6KWrOxjRgBOj1PBR6vofdJqw8z-gHvjE"
bot = telebot.TeleBot(took)

@bot.message_handler(commands=["start","help"])
def startBot(message):
 bot.send_message(message.chat.id,"هلا بيك")
 ##############################################
@bot.my_chat_member_handler()
def leave(message:types.ChatMemberUpdated):
 update = message.new_chat_member
 if update.status == "member":
  bot.send_message(message.chat.id,"هذا البوت لا يعمل لانه خاص بمطور مجموعة شبكة بحر التعليمية يمكنك مراسلة المطور للحصول على بوت شبيه له  وداعاً 👋 ")
  bot.leave_chat(message.chat,id)
##########################################################
@bot.message_handler(func=lambda m:True)
def reply(message):
 words = message.text.split()
 if words[0] in "بوت":
  bot.reply_to(message,"ها شتريد")
 elif words[0] in "هيج":
  bot.reply_to(message,"هيج لو دجاج ههههه")
 elif words[0] in "احبك":
  bot.reply_to(message,"ليش تحبني")
###########################################

@app.route( / )
def home():
    return "<b>telegram</b>"
def run():
    app.run(host= 0.0.0.0 , port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__": #تشغيل البوت
    keep_alive() #تشغيل الوب
    bot.infinity_polling(skip_pending=True) #تشغيل الوب
