import time

import pyautogui as bot

bot.moveTo(783, 800, 1)
bot.rightClick()
# bot.moveTo(879, 1048, 1)
# bot.press('enter')
bot.press('down')
bot.press('down')
bot.press('down')
bot.press('enter')
bot.press('up')
bot.press('up')
bot.press('up')
bot.press('up')
bot.press('enter')
# bot.press('f2')
time.sleep(1)
bot.typewrite('hello')
bot.press('enter')
bot.press('enter')
time.sleep(1)
bot.typewrite('hello')
bot.hotkey('ctrl', 's')
time.sleep(1)
bot.hotkey('ctrl', 'w')