import pyautogui
from time import time, sleep
from sys import platform
from subprocess import call, check_output
from typing import Union


def focus_windows():
    # Switch windows to minecraft
    if "linux" in platform:
        cmd = "xdotool search --name Minecraft".split()
        stdout = check_output(cmd)
        cmd2 = "xdotool windowactivate "+stdout.strip().decode("UTF-8")
        cmd2 = cmd2.split()
        call(cmd2)


def multiple_keyhold(keys: Union[str, list], hold_time: Union[int, float] = 0):
    if type(keys) == str:
        keys = [k for k in keys]

    start = time()
    while time() - start < hold_time:
        for key in keys:
            pyautogui.keyDown(key)

    for key in keys:
        pyautogui.keyUp(key)


def write_to_chat(text: str = 'Testing PyAG executed'):
    pyautogui.press('enter')
    pyautogui.write(text)
    pyautogui.press('enter')


def flip_switch():
    pyautogui.move(-65, 25, duration=1)
    pyautogui.press("e")
    pyautogui.move(65, -25, duration=1)


def swipe_per_sec(swipe: int = 50):
    pyautogui.click(clicks=swipe, interval=1)


def eating(weapon_slot: Union[int, str] = 1, food_slot: Union[int, str] = 9):
    weapon_slot = str(weapon_slot)
    food_slot = str(food_slot)

    pyautogui.press(food_slot)
    multiple_keyhold("e", 2)
    pyautogui.press(weapon_slot)


def reset_tower(eat: bool = False):
    multiple_keyhold("as", 0.5)
    multiple_keyhold("wd", 0.5)
    sleep(2)
    multiple_keyhold("sd", 5)
    if eat:
        eating()
        sleep(5)
    else:
        sleep(7)
    multiple_keyhold("as", 3)
    multiple_keyhold("d", 0.5)
    multiple_keyhold("wd", 0.5)


def one_loop(**kwargs):
    # Turn off water
    flip_switch()
    reset_tower(**kwargs)
    # Wait for horn
    sleep(8)
    flip_switch()
    swipe_per_sec(55)


def main(debug=False):

    focus_windows()
    sleep(1)

    timer_start = time()

    i = 0
    eating = False

    while True:

        # Eat every 15 mins
        timer_stop = time()
        if timer_stop - timer_start > 15*60:
            timer_start = time()
            eating = True

        one_loop(eat=eating)

        i += 1
        if debug and (i == 1 or i % 10 == 0):
            write_to_chat(text=f'[Raid Farm Bot] Completed {i} loop')
        
        # break


if __name__ == "__main__":
    main()
