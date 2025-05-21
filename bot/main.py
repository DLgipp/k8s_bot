import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import os

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: Message):
    await message.answer("Привет! Отправь /rand <min> <max>, и я выдам тебе случайное число.")


@dp.message_handler(commands=["rand"])
async def rand_command(message: Message):
    try:
        _, min_val, max_val = message.text.strip().split()
        min_val = int(min_val)
        max_val = int(max_val)
        if min_val > max_val:
            raise ValueError
        num = random.randint(min_val, max_val)
        await message.answer(f"🎲 Случайное число: {num}")
    except Exception:
        await message.answer("Неверный формат. Используй: /rand 10 100")

def generate_random_number(low: int, high: int) -> int:
    return random.randint(low, high)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
