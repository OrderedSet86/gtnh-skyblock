import json
import pyautogui as pg
from collections import deque
from itertools import chain
from time import sleep


with open('config.json', 'r') as f:
    data = json.load(f)
bl, crafting_tl, spacing, crafting_result = (
    data['bottom_left'],
    data['crafting_top_left'],
    data['spacing'],
    data['crafting_result'],
)

BUCKET_PATTERN = [
    [1, 0, 1],
    [0, 0, 0],
    [0, 0, 0]
]
pg.PAUSE = 0.03
DRY_RUN = False
TARGET_QUANTITY = 10

# CURRENT_LEVEL = 30 # This assumes the tank is already full
recipe_buckets = sum([sum(x) for x in BUCKET_PATTERN])
tank_buckets = recipe_buckets * TARGET_QUANTITY + 9 + 1

# Set up: look against tank bottom edge flat against drain

bucket_tape = list(chain.from_iterable(BUCKET_PATTERN)) # Flatten list, we can just use modulo to simplify things
num_buckets = sum(bucket_tape)

# https://www.wolframalpha.com/input/?i=sum+110+%2B+9+%28n+-+30%29&assumption=%7B%22C%22%2C+%22sum%22%7D+-%3E+%7B%22SumWord%22%7D
# if CURRENT_LEVEL <= 15:
#     available_xp = CURRENT_LEVEL**2 + 6 * CURRENT_LEVEL
# elif CURRENT_LEVEL <= 30:
#     available_xp = 5/2 * (CURRENT_LEVEL**2 - 15 * CURRENT_LEVEL) + 315
# else:
#     available_xp = 1/2 * (9 * CURRENT_LEVEL**2 - 311 * CURRENT_LEVEL) + 1440 + 496

# from https://github.com/InnovativeOnlineIndustries/Industrial-Foregoing/issues/137
essence_rate = 14 # 1 xp = 20 essence
# available_essence = available_xp * essence_rate + 16000
available_essence = tank_buckets * 1000
first_run = True
empty_bucket_counter = 9

# Focus window
pg.click(crafting_result[0], crafting_result[1] + spacing)
sleep(0.5)
pg.press('esc')

# while available_essence >= num_buckets * 1000 + 9 % num_buckets:
while available_essence >= 9000:
    print(available_essence)
    # Refill buckets
    pg.press('1') # Make sure leftmost buckets are selected
    sleep(0.1)
    for i in range(empty_bucket_counter):
        if available_essence >= 1000:
            empty_bucket_counter -= 1
            available_essence -= 1000
            if not DRY_RUN:
                pg.rightClick()
                sleep(0.1)

    # Scoot forward into crafting table
    with pg.hold('w'):
        sleep(0.5)
    pg.rightClick()
    sleep(2) # Wait for crafting window to pop up

    available_buckets = deque([(bl[0] + spacing*x, bl[1]) for x in range(0 if empty_bucket_counter == 0 else 1, 9 - empty_bucket_counter)])
    while len(available_buckets) >= num_buckets:
        # Move buckets into correct position for recipe
        for idx, pos in enumerate(bucket_tape):
            if pos == 1:
                bucket_pos = available_buckets.popleft()
                empty_bucket_counter += 1
                pg.moveTo(*bucket_pos)
                if not DRY_RUN:
                    pg.click()
                crafting_pos = divmod(idx, 3) # Returns division result w/remainder
                pg.moveTo(
                    crafting_tl[0] + crafting_pos[1]*spacing,
                    crafting_tl[1] + crafting_pos[0]*spacing
                )
                if not DRY_RUN:
                    pg.click()

        # Actually craft item
        if not DRY_RUN:
            with pg.hold('shift'):
                pg.click(*crafting_result)
                sleep(0.05)

    # Now buckets should be in bottom left and output in bottom left + 1 slot
    # Move product to inventory
    if not DRY_RUN:
        if first_run and num_buckets == 1:
            sleep(0.2)
            # bucket is in top left, product is in bottom left. need to swap
            pg.moveTo(*bl)
            with pg.hold('shift'):
                pg.click()
            pg.click(
                bl[0],
                bl[1] - spacing*3
            )
            pg.click(*bl)
        elif num_buckets > 1:
            sleep(0.2)
            pg.moveTo(
                bl[0] + spacing*(num_buckets-1),
                bl[1]
            )
            with pg.hold('shift'):
                pg.click()
        sleep(0.2)

    pg.press('esc')
    # Refill tank
    # Back up into tank
    with pg.hold('s'):
        sleep(0.2)
    
    sleep(1)

    # if available_essence > 7000: # Some xp left in player, 16 - 9 = 7
    #     # Jump
    #     with pg.hold('space'):
    #         sleep(0.1)
    #     # Move forward onto drain
    #     with pg.hold('w'):
    #         sleep(0.3)
    #     # Wait for xp drain (6 seconds to drain 9000 xp)
    #     sleep(
    #         min(
    #             max(0, 6*(available_essence-7000)/9000), # Time to drain all player XP
    #             6*empty_bucket_counter/9 # Time to drain enough to refill tank
    #         )
    #     )
    #     # Scoot back into tank position
    #     with pg.hold('s'):
    #         sleep(0.2)
    #     sleep(0.4) # Need to fall back to ground
    #     with pg.hold('w'):
    #         sleep(0.2)

    first_run = False
