import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

# إعداداتك الخاصة
TOKEN = "7973442964:AAFBinhQsewVIgnoAocyfG87AmWMfofoMkk"
OWNER_ID = 8134275876

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.reply("🛡️ نظام حماية المجموعات متصل الآن بنجاح!")

@dp.message(F.new_chat_members)
async def protect(message: types.Message):
    for member in message.new_chat_members:
        if member.is_bot:
            await message.chat.ban(user_id=member.id)
            await message.answer(f"🚫 تم طرد البوت الغريب!")

@dp.message(F.text.contains("http"))
async def anti_link(message: types.Message):
    user = await message.chat.get_member(message.from_user.id)
    if user.status not in ["administrator", "creator"]:
        await message.delete()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
  
