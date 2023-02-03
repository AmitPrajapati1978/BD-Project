import os

import telebot
import requests
from  bs4 import BeautifulSoup

# from dotenv import load_dotenv

# BOT_TOKEN = os.environ.get('BOT_TOKEN')
# import lxml
bot = telebot.TeleBot('6032868152:AAHsanPdMolphiRDSzQbaRMBhObF-1_zXHY')

# @bot.message_handler(commands=['start', 'hello'])
# def send_welcome(message):
#     bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['Bajaj'])
def bajaj(message):
    link='https://www.bajajallianz.com/about-us/financial-information.html'
    source=requests.get(link).text
    soup=BeautifulSoup(source,"html.parser")
    a=soup.findAll('div',class_="financeDataWrapper")  
    quaters=[]
    for i in range(len(a[-1].findAll("h3"))):
        quaters.append(a[-1].findAll("h3")[i].get_text())
    bot.reply_to(message, f"Last data for Bajaj is found for------> {quaters[-1]}")


@bot.message_handler(commands=['Acko'])
def acko(message):
    link='https://www.acko.com/public-disclosure/'
    source=requests.get(link).text
    soup=BeautifulSoup(source,"html.parser")
    a=soup.findAll('div',class_="sc-bdVaJa sc-bwzfXH sc-dEfkYy fnSFNN")
    # print(soup)
    tp=a[-1].findAll('a',class_="sc-iuDHTM irEgdH")


    # tp[-1].get_text()
    bot.reply_to(message, f"Last data for Acko is found for------> {tp[-1].get_text()}")



@bot.message_handler(commands=['Icici'])
def icici(message):
    link='https://www.icicilombard.com/about-us/public-disclosure'
    source=requests.get(link).text
    soup=BeautifulSoup(source,"html.parser")
    a=soup.find_all('div',class_="col-xs-12 col-sm-12 col-md-8 col-lg-8")
    tp=a[0].findAll('h5')   
    # tp[-1].get_text()
    bot.reply_to(message, f"Last data for Icici is found for------> {tp[-1].get_text()}")


@bot.message_handler(commands=['Magma'])
def magma(message):
    link='https://www.magmahdi.com/public-disclosures'
    source=requests.get(link).text
    soup=BeautifulSoup(source,"html.parser")
    a=soup.find_all('div',class_="tab-content")
    tp=a[1].findAll('div',class_='tab-pane fade in active show')[0].findAll('a')   
    # tp[-1].get_text()
    bot.reply_to(message, f"Last data for Magma is found for------> {tp[-1].get_text()}")

link='https://www.magmahdi.com/public-disclosures'
source=requests.get(link).text
soup=BeautifulSoup(source,"html.parser")
a=soup.find_all('div',class_="tab-content")
tp=a[1].findAll('div',class_='tab-pane fade in active show')[0].findAll('a')


bot.infinity_polling()
