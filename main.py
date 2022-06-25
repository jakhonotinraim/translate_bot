from cgitb import lookup
import logging
from translatebot import getDefinitions
from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator
API_TOKEN = '5401882642:AAGmoOZUeQOzbGxTt1GjzBKxr_rlb5enE5s'
translator=Translator()
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start',])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Hi!\nI'm OxfordTranslateBot!\nSend me what word's definition you want to know. ")

@dp.message_handler(commands=['help',])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    await message.reply("Hi!\nI'm OxfordTranslateBot!\nThis bot sends definitions of a word and its pronunciation")



@dp.message_handler()
async def translatorText(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text) 
    lang=translator.detect(message.text).lang
    if len(message.text.split())>2:
        defn='uz' if lang=='en' else 'en'
        await message.reply(translator.translate(message.text, defn).text)
    else:
        if lang=='en':
            word_id=message.text
        else:
            word_id=translator.translate(message.text, defn='en').text
        
        lookup=getDefinitions(word_id)
        if lookup:
            await message.reply(f' Word: {word_id}\nDefinitions:\n {lookup["definitions"]}')
            if lookup.get('audio'):
                await message.reply_voice(f' Word: {word_id}\nPronunciation:\n {lookup["audio"]}')
        else:
            await message.reply("Bunday so'z topilmadi.")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)