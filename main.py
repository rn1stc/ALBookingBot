from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import logging
from instaloader import Instaloader, Profile

token_ini = open('token.ini', 'r')
token = token_ini.read()

L = Instaloader()

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Стройка еще не завершена, и пока мы не принимаем бронирования. Чтобы посмотреть фото со стройплощадки из нашего инстаграма нажми /imgs")


def imgs(update, context):
    profile = Profile.from_username(L.context, 'a_land3')
    count = 0
    for post in profile.get_posts():
        count += 1
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=post.url, caption=post.caption)
        if count == 5:
            break


from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
imgs_handler = CommandHandler('imgs', imgs)
dispatcher.add_handler(imgs_handler)

updater.start_polling()
