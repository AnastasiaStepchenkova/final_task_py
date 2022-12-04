import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types


bot = telebot.TeleBot('5893498909:AAGdGCTax-1zjZzMJLDj5qYlNL8aN5F7xIo')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    dishes = types.InlineKeyboardMarkup(row_width=1)
    dishes_falafel = types.InlineKeyboardButton(text='фалафель', callback_data='falafel')
    dishes_shakshuka = types.InlineKeyboardButton(text='шакшука', callback_data='shakshuka')
    dishes_kugel = types.InlineKeyboardButton(text='иерусалимский кугель', callback_data='kugel')
    dishes_forshmak = types.InlineKeyboardButton(text='фаршмак', callback_data='forshmak')
    dishes_humus = types.InlineKeyboardButton(text='хумус', callback_data='humus')
    dishes_pirog = types.InlineKeyboardButton(text='миндально-апельсиновый пирог', callback_data='pirog')
    dishes_dolma = types.InlineKeyboardButton(text='долма', callback_data='dolma')
    dishes.add(dishes_falafel, dishes_shakshuka, dishes_kugel, dishes_forshmak, dishes_humus, dishes_pirog, dishes_dolma)
    bot.send_message(m.chat.id, 'Hi, choose smth that u want to cook.', reply_markup=dishes)

@bot.callback_query_handler(func=lambda call: True)
def handle_button(call):
    if call.data == 'falafel':
        r = requests.get('https://www.gastronom.ru/recipe/2616/falafel')
        photo = open('фалафель.jpg', 'rb')
        bot.send_photo(call.from_user.id, photo)
        soup = BeautifulSoup(r.text, 'html.parser')
        ingridients = soup.find_all('li', class_='recipe__ingredient')
        cooking = soup.find_all('div', class_='recipe__step-text')
        clear_ing = []
        clear_coo = []
    elif call.data == 'shakshuka':
        r = requests.get('https://www.gastronom.ru/recipe/55888/shakshuka')
        photo = open('шакшука.jpg', 'rb')
        bot.send_photo(call.from_user.id, photo)
        soup = BeautifulSoup(r.text, 'html.parser')
        ingridients = soup.find_all('li', class_='recipe__ingredient')
        cooking = soup.find_all('div', class_='recipe__step-text')
        clear_ing = []
        clear_coo = []
    elif call.data == 'kugel':
        r = requests.get('https://www.gastronom.ru/recipe/25586/ierusalimskij-kugel')
        photo = open('кугель.jpg', 'rb')
        bot.send_photo(call.from_user.id, photo)
        soup = BeautifulSoup(r.text, 'html.parser')
        ingridients = soup.find_all('li', class_='recipe__ingredient')
        cooking = soup.find_all('div', class_='recipe__step-text')
        clear_ing = []
        clear_coo = []
    elif call.data == 'forshmak':
        r = requests.get('https://www.gastronom.ru/recipe/25524/forshmak')
        photo = open('фаршмак.jpg', 'rb')
        bot.send_photo(call.from_user.id, photo)
        soup = BeautifulSoup(r.text, 'html.parser')
        ingridients = soup.find_all('li', class_='recipe__ingredient')
        cooking = soup.find_all('div', class_='recipe__step-text')
        clear_ing = []
        clear_coo = []
    elif call.data == 'humus':
        r = requests.get('https://www.gastronom.ru/recipe/50690/teplyj-humus-s-ostrymi-kedrovymi-oreshkami')
        photo = open('хумус.jpg', 'rb')
        bot.send_photo(call.from_user.id, photo)
        soup = BeautifulSoup(r.text, 'html.parser')
        ingridients = soup.find_all('li', class_='recipe__ingredient')
        cooking = soup.find_all('div', class_='recipe__step-text')
        clear_ing = []
        clear_coo = []
    elif call.data == 'pirog':
        r = requests.get('https://www.gastronom.ru/recipe/54305/mindalno-apelsinovyj-pirog')
        photo = open('минсдальн.jpg', 'rb')
        bot.send_photo(call.from_user.id, photo)
        soup = BeautifulSoup(r.text, 'html.parser')
        ingridients = soup.find_all('li', class_='recipe__ingredient')
        cooking = soup.find_all('div', class_='recipe__step-text')
        clear_ing = []
        clear_coo = []
    elif call.data == 'dolma':
        r = requests.get('https://www.gastronom.ru/recipe/26382/dolma')
        photo = open('долма.jpg', 'rb')
        bot.send_photo(call.from_user.id, photo)
        soup = BeautifulSoup(r.text, 'html.parser')
        ingridients = soup.find_all('li', class_='recipe__ingredient')
        cooking = soup.find_all('div', class_='recipe__step-text')
        clear_ing = []
        clear_coo = []
    for i in cooking:
          clear_coo.append(i.getText())
    for y in ingridients:
          clear_ing.append(y.getText())
    bot.send_message(call.from_user.id, '\n'.join(clear_ing))
    bot.send_message(call.from_user.id, '\n'.join(clear_coo))


bot.polling(none_stop=True, interval=0)


