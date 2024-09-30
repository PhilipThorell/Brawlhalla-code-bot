import os
import random
import keyboard
from random import uniform
import pyautogui
from pynput.mouse import Controller
import pynput
import threading
import time
import pyperclip
import send2trash

mouse = Controller()

running = True
active = False
first_time = True

START_BUTTON = "F8"
STOP_BUTTON = "F7"
EXIT_BUTTON = "DELETE"

INSERT_BOX = (700, 1200, 334, 352)
ENTER_BOX = (886, 1025, 416, 457)
INVALID_CLOSE_BOX = (809, 1086, 609, 634)
DONE_CLAIM_BOX = (872, 1041, 780, 801)
REDEEM_CODE_BOX = (123, 266, 1007, 1014)

CODE_LIST = []
code_count = 0


def check_keys():
    while True:
        global active, running
        if keyboard.is_pressed(START_BUTTON):
            active = True
        if keyboard.is_pressed(STOP_BUTTON):
            active = False
        if keyboard.is_pressed(EXIT_BUTTON):
            running = False


threading.Thread(target=check_keys, daemon=True).start()

directory = "D:\\Downloads\\"
files = os.listdir(directory)

for file in files:
    if file.endswith('.txt'):
        file_path = os.path.join(directory, file)

        with open(file_path, 'r') as f:
            content = f.read()

        content = content.split()
        for row in content:
            if len(row) == 13:
                CODE_LIST.append(row)
        send2trash.send2trash(f"D:\\Downloads\\{file}")
        #with open(file_path, 'w') as f:
        #    f.write("")


while running:
    time.sleep(0.005)
    if len(CODE_LIST) == 0:
        print("list empty")
        break
    if active:
        random_code = CODE_LIST.pop(random.randint(0, len(CODE_LIST)-1))
        pyperclip.copy(random_code)
        pyautogui.moveTo(uniform(INSERT_BOX[0], INSERT_BOX[1]), uniform(INSERT_BOX[2], INSERT_BOX[3]), duration=0.1)
        time.sleep(uniform(0.01, 0.03))
        mouse.press(pynput.mouse.Button.left)
        time.sleep(uniform(0.01, 0.05))
        mouse.release(pynput.mouse.Button.left)
        time.sleep(uniform(0.01, 0.05))
        mouse.press(pynput.mouse.Button.left)
        time.sleep(uniform(0.01, 0.05))
        mouse.release(pynput.mouse.Button.left)
        time.sleep(uniform(0.01, 0.05))
        mouse.press(pynput.mouse.Button.left)
        time.sleep(uniform(0.01, 0.05))
        mouse.release(pynput.mouse.Button.left)
        time.sleep(uniform(0.01, 0.05))
        keyboard.press("ctrl+v")
        time.sleep(uniform(0.01, 0.05))
        keyboard.release("ctrl+v")
        time.sleep(uniform(0.01, 0.05))
        pyautogui.moveTo(uniform(ENTER_BOX[0], ENTER_BOX[1]), uniform(ENTER_BOX[2], ENTER_BOX[3]), duration=0.1)
        time.sleep(uniform(0.01, 0.03))
        mouse.press(pynput.mouse.Button.left)
        time.sleep(uniform(0.01, 0.05))
        mouse.release(pynput.mouse.Button.left)
        time.sleep(0.3)
        screenshot = pyautogui.screenshot()
        color = screenshot.getpixel((INSERT_BOX[0], INSERT_BOX[2]))
        while color == (0, 0, 60):
            screenshot2 = pyautogui.screenshot()
            color = screenshot2.getpixel((INSERT_BOX[0], INSERT_BOX[2]))
            time.sleep(0.5)
        screenshot3 = pyautogui.screenshot()
        color3 = screenshot3.getpixel((INSERT_BOX[0], INSERT_BOX[2]))
        if color3 == (0, 0, 51):
            pyautogui.moveTo(uniform(INVALID_CLOSE_BOX[0], INVALID_CLOSE_BOX[1]),
                             uniform(INVALID_CLOSE_BOX[2], INVALID_CLOSE_BOX[3]), duration=0.1)
            time.sleep(uniform(0.01, 0.03))
            mouse.press(pynput.mouse.Button.left)
            time.sleep(uniform(0.01, 0.05))
            mouse.release(pynput.mouse.Button.left)
        elif color3 == (254, 254, 254):
            print("error but i fixed it")
            pyautogui.moveTo(uniform(REDEEM_CODE_BOX[0], REDEEM_CODE_BOX[1]),
                             uniform(REDEEM_CODE_BOX[2], REDEEM_CODE_BOX[3]), duration=0.1)
            time.sleep(uniform(0.08, 0.12))
            mouse.press(pynput.mouse.Button.left)
            time.sleep(uniform(0.01, 0.05))
            mouse.release(pynput.mouse.Button.left)
        elif color3 == (0, 0, 50):
            print("found a code")
            code_count += 1
            time.sleep(2)
            pyautogui.moveTo(uniform(DONE_CLAIM_BOX[0], DONE_CLAIM_BOX[1]),
                             uniform(DONE_CLAIM_BOX[2], DONE_CLAIM_BOX[3]), duration=0.1)
            time.sleep(uniform(0.01, 0.03))
            mouse.press(pynput.mouse.Button.left)
            time.sleep(uniform(0.01, 0.05))
            mouse.release(pynput.mouse.Button.left)
            pyautogui.moveTo(uniform(REDEEM_CODE_BOX[0], REDEEM_CODE_BOX[1]),
                             uniform(REDEEM_CODE_BOX[2], REDEEM_CODE_BOX[3]), duration=0.1)
            time.sleep(uniform(0.08, 0.12))
            mouse.press(pynput.mouse.Button.left)
            time.sleep(uniform(0.01, 0.05))
            mouse.release(pynput.mouse.Button.left)
            time.sleep(uniform(0.08, 0.12))
            mouse.press(pynput.mouse.Button.left)
            time.sleep(uniform(0.01, 0.05))
            mouse.release(pynput.mouse.Button.left)
            time.sleep(0.9)


        first_time = False

score_file = "score.txt"
with open(score_file, "r") as f:
    score = int(f.read())

score += code_count

with open("score.txt", "w") as file:
    file.write(str(score))
