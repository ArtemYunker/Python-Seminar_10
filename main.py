from aiogram import Bot, Dispatcher, executor, types
from random import randint

bot = Bot(token='5848794982:AAHlPil8bvGB6G_8XCv7J_WbmMU-CJ3F_pI')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   kb = [
       [
           types.KeyboardButton(text="ОРЕЛ"),
           types.KeyboardButton(text="PЕШКА")
       ],
   ]
   keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
 
   await message.reply("Привет! Игра на выбор ОРЕЛ или РЕШКА", reply_markup=keyboard)

@dp.message_handler()
async def echo(message: types.Message):

    n_comp = randint(1,2)

    print(message.text , n_comp)

    if (message.text == "ОРЕЛ" and n_comp ==1) or (message.text == "PЕШКА" and n_comp ==2) :
        await message.reply(f'ВЫ ВЫИГРАЛИ')

    else:
            await message.reply(f'ВЫ ПРОИГРАЛИ')

print("server start")
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)