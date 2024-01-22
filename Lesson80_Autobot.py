import pyautogui as bot
import keyboard

x0, y0 = bot.position()
while True:
    a = bot.size()
    x, y = bot.position()
    if x != x0 or y != y0:
        print(a, x, y)
    x0, y0 = x, y
    if keyboard.is_pressed('alt'):
        break
