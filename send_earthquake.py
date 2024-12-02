import bluetooth
# import serial
from telegram import Bot
from telegram.error import TelegramError
import asyncio


addr = "00:19:12:10:0A:73"
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((addr, 1))


async def send_message_to_users(user_ids, message, bot):
    for user_id in user_ids:
        try:
            await bot.send_message(chat_id=user_id, text=message)
        except TelegramError as e:
            print(f'Error sending message to user {user_id}: {e}')


async def main():
    while True:
        BOT_TOKEN = "6155546088:AAF_sBuYKbMSi3XxJUwdSixd-BNaVbB7o3Q"
        bot = Bot(token=BOT_TOKEN)
        # serial_port = serial.Serial('/dev/cu.usbserial-120', 115200)
        data = sock.recv(1024).decode()

        print(data)
        # data = serial_port.readline().decode('utf').rstrip()
        if (data == '1'):
            with open("user_id.txt", "r") as f:
                f_string = f.read()
                f_string = '[' + f_string + ']'
                user_ids = eval(f_string)
                await send_message_to_users(user_ids, "EARTHQUAKEE! RUNNNN (This is a test)", bot)


asyncio.run(main())
