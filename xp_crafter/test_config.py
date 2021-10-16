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

# Move over inventory
for row in range(4):
    for column in range(9):
        pg.moveTo(
            bl[0] + spacing*column,
            bl[1] - spacing*3 + spacing*row,
        )

# Move over crafting table
for row in range(3):
    for column in range(3):
        pg.moveTo(
            crafting_tl[0] + spacing*column,
            crafting_tl[1] + spacing*row,
        )
pg.moveTo(*crafting_result)