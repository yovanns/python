import dp as dp
import pip
import telegram
import os
import telebot
from telebot import types
import aiosqlite
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import logging
import nextcord
from nextcord.ext import commands
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# client = commands.bot(command_prefix="d!")

# @client.event
# async def on_ready():
#     print("Bot is up and ready!")
#     async with aiosqlite.connect("main.db") as db:
#         async with db.cursor() as cursor:
#             await cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, guild INTEGER)')
#         await db.commit()


# bot = telebot.TeleBot("6076113883:AAFKNotz3XKiYFU1uLQ6WKFYbkXza4iN8hU")
# bot = telebot.TeleBot("6076113883:AAFKNotz3XKiYFU1uLQ6WKFYbkXza4iN8hU", parse_mode="MarkdownV2")
logging.basicConfig(level=logging.INFO)

bot = Bot(token='6272920604:AAFtRscby2eklbjmuk70PP6qSwRF9BA9FTI')
dp = Dispatcher(bot)

button1 = KeyboardButton('Plans')
button2 = KeyboardButton('More info')
keyboard1 = ReplyKeyboardMarkup()
keyboard1.add(button1).add(button2)

# button3 = KeyboardButton('Wise')
# button4 = KeyboardButton('PayPal')
# keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button3).add(button4)

# Define a start handler
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    # Create an inline keyboard markup with two buttons
    keyboard = InlineKeyboardMarkup(row_width=2)
    plans_button = InlineKeyboardButton('Job, Community', callback_data='plans')
    info_button = InlineKeyboardButton('Employee', callback_data='info')
    # employee_button = InlineKeyboardButton('Employee', callback_data='employee')
    keyboard.add(plans_button, info_button)

    # Send a greeting message with the inline keyboard
    await message.answer("Welcome! I'm here to help you connect with like-minded individuals in the IT field. Whether you're looking for a job, searching for employees, or simply seeking new buddies to collaborate with, this bot is designed to assist you."
                         "Please let me know what you are looking for:", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data == 'plans')
async def plans_callback_handler(callback_query: types.CallbackQuery):
    # Create an inline keyboard markup with plan options
    keyboard = InlineKeyboardMarkup(row_width=1)
    month_button = InlineKeyboardButton('1 Month - 40€', callback_data='1month')
    three_months_button = InlineKeyboardButton('3 Months - 99€', callback_data='3months')
    lifetime_button = InlineKeyboardButton('Lifetime - 369€', callback_data='lifetime')
    keyboard.add(month_button, three_months_button, lifetime_button)

    # Send a message with the plan options
    message = "Write your full name:"
    await bot.send_message(callback_query.from_user.id, message, reply_markup=keyboard)


# Define a callback query handler for the plan options
@dp.callback_query_handler(lambda c: c.data in ['1month', '3months', 'lifetime'])
async def plan_callback_handler(callback_query: types.CallbackQuery):
    # Create an inline keyboard markup with payment options
    keyboard = InlineKeyboardMarkup(row_width=1)

    # Define the payment links for each plan option
    if callback_query.data == '1month':
        # wise_link = 'https://wise.com/share/ivanc1233'
        stripe_link = 'https://buy.stripe.com/eVacPO4E7g7lapq8wA'
        paypal_link = 'https://paypal.me/fxcvit?country.x=HR&locale.x=en_US'
    elif callback_query.data == '3months':
        # wise_link = 'https://wise.com/share/ivanc1233'
        stripe_link = 'https://buy.stripe.com/6oEcPO3A3aN11SUbIN'
        paypal_link = 'https://paypal.me/fxcvit?country.x=HR&locale.x=en_US'
    else:
        # wise_link = 'https://wise.com/share/ivanc1233'
        stripe_link = 'https://buy.stripe.com/bIYdTSb2vbR58hi006'
        paypal_link = 'https://paypal.me/fxcvit?country.x=HR&locale.x=en_US'

    # wise_button = InlineKeyboardButton('Wise', url=wise_link)
    stripe_button = InlineKeyboardButton('Stripe', url=stripe_link)
    paypal_button = InlineKeyboardButton('PayPal', url=paypal_link)
    keyboard.add(stripe_button, paypal_button)

    # Send a message with the payment options
    message = "Please choose a payment option:"
    await bot.send_message(callback_query.from_user.id, message, reply_markup=keyboard)



# Define a callback query handler for the 'More info' button
@dp.callback_query_handler(lambda c: c.data == 'info')
async def info_callback_handler(callback_query: types.CallbackQuery):
    # Create an inline keyboard markup with two channel buttons
    keyboard = InlineKeyboardMarkup(row_width=2)
    boris_fx_button = InlineKeyboardButton('Boris', url='https://t.me/bbhumblefx')
    cvit_fx_button = InlineKeyboardButton('Ivan', url='https://t.me/IVANCVITA')
    keyboard.add(boris_fx_button, cvit_fx_button)
    message = "Past performance is not indicative of future results. The number of signal provided may vary each week. Accordingly, performance results may differ substantially from account to account, depending on the number of signals and contracts traded. Atum FX provides general advice that does not take into account your objectives, financial situation or needs. The content of this group must not be construed as personal advice. The possibility exists that you could sustain a loss in excess of your deposited funds and therefore, you should not speculate with capital that you cannot afford to lose. You should be aware of all the risks associated with trading on margin. Visit our website for more information: https://forexatum.com/"
    # Send the message with inline keyboard
    await bot.send_message(callback_query.from_user.id, message, reply_markup=keyboard)


# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)






# @dp.message_handler(commands=['start'])
# async def start(m: types.Message):
#     await m.reply("Welcome {0.first_name}! Im a Atum bot, How can I help you today?", reply_markup=keyboard1)



# @dp.message_handler(commands=('help'))
# async def help(m: types.Message):
#     await m.answer('Ты в попал в хендлер help')
#
#
# @dp.message_handler(commands=('opening_hours'))
# async def open_close(m: types.Message):
#     # показывает сообщение о часах работы магазина/заведения
#     await m.answer('Ты в попал в хендлер open_close')


#
# @dp.message_handler()
# async def kb_answer(message: types.Message):
#     if message.text == 'Plans':
#         await message.answer('Here are the plans: ')
#     elif message.text == 'More info':
#         await message.answer('https://forexatum.com/')
#     else:
#         await message.answer(f'Please choose an appropriate option')

#
# executor.start_polling(dp)

# @bot.message_handler(commands=['start'])
# def handle_command(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     but1 = types.KeyboardButton("Plans")
#     but2 = types.KeyboardButton("More info")
#     markup.add(but1, but2)
#     bot.reply_to(message, "Welcome {0.first_name}!  I'm a Atum bot, How can I help you today?".format(message.from_user), parse_mode='html', reply_markup=markup)
#
# @bot.message_handler(func=lambda message: True)
# def handle_response(message):
#     bot.reply_to(message, message.text)
#
#
# bot.polling()
