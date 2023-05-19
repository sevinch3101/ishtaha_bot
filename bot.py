from aiogram import Bot,Dispatcher,executor,types
import logging
from api import taom_qaytar
logging.basicConfig(level=logging.INFO)
from googletrans import Translator

bot=Bot(token="5886240811:AAED5HxVvkMpoJx-Nu3rK7QfpCJMCzr6RMw")
dp=Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(mess:types.Message):
    await mess.reply(f"Salom {mess.chat.full_name}.\nTaom hohliysanmi?\n/taom ni bos!!!!")

@dp.message_handler(commands="taom")
async def taom(message:types.Message):
    meals=taom_qaytar()
    nomi=meals['strMeal']
    hudud=meals['strArea']
    categoriya=meals['strCategory']
    rasm=meals['strMealThumb']
    video=meals['strYoutube']
    text=f"{nomi}\n {hudud}\n {categoriya}"
    terjimon=Translator()
    textuz=terjimon.translate(text,dest='uz').text
    await message.answer_photo(photo=rasm,caption=textuz)
    await message.answer(video)

if __name__=="__main__":
    executor.start_polling(dp,skip_updates=False) 


