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

pg.moveTo(bl[0], bl[1]+spacing)
pg.click()
sleep(0.5) # Need to wait for window focus
pg.press('esc')
for i in range(64):
    pg.rightClick()