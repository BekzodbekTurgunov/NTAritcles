from aiogram import Bot, Dispatcher, executor, types
from pprint import pprint as print
import logging
from article import getArticles

logging.basicConfig(level=logging.INFO)
API_TOKEN = '1833260329:AAHPCCgVIc10q9WiXRTkcOMEpl2nezXEhdU'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def startMessage(message: types.Message):
    await message.reply(
        f"Assalomu alaykum {message['from']['first_name']}\nNew York Times maqolalarni qidirish bolimiga xush kelibsiz!")


@dp.message_handler()
async def sendAritcles(message: types.Message):
    try:
        articles = getArticles(message.text)
        print(len(articles))
        i = 0
        for article in articles:
            await message.reply(article['web_url'])
            i +=1
            if i >=3:
                break
    except:
        await message.reply("Ushbu so'zlarga mos maqola topa olmadik.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
