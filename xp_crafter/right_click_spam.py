import json
import pyautogui as pg
from time import sleep

with open('config.json', 'r') as f:
    data = json.load(f)
bl, crafting_tl, spacing, crafting_result = (
    data['bottom_left'],
    data['crafting_top_left'],
    data['spacing'],
    data['crafting_result'],
)

pg.PAUSE = 0.01

USE_ALL_SLOTS = True

pg.moveTo(bl[0], bl[1]+spacing)
pg.click()
sleep(1) # Need to wait for window focus
pg.press('esc')

if USE_ALL_SLOTS:
    for slot in range(1, 10):
        pg.press(str(slot))
        sleep(0.5)
        for i in range(80):
            pg.rightClick()
else:
    for i in range(64):
        pg.rightClick()