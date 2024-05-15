import telebot #Импорт главной библеотеки
from telebot import types

bot = telebot.TeleBot('7044171753:AAHqvew9NM89ki-Hbze7Ep1DhDURPcEYVqw') #Токен бота для того чтобы код и бот связались


@bot.message_handler(commands=['start']) #Реакция на команду /start
def start(message):
    markup = types.ReplyKeyboardMarkup()
    webapp = types.WebAppInfo("https://finnickjas.github.io/TelegramBot/")
    markup.add(types.KeyboardButton('Магазин',web_app=webapp))
    bot.send_message( message.chat.id, 'Телеграм бот магазина "Дачница".Предлагаем заранее создать карзину товаров, и оплатить её.', reply_markup=markup)



@bot.message_handler(content_types=["web.app.data"])
async def webapp(message: types.Message):
   bot.send_message(message.WebAppData.data)

bot.polling(non_stop=True) #Команда для бесконечной работы бота до выключения программы
