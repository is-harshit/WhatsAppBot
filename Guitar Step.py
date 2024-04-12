import pyautogui as pt
from time import sleep

sleep(5)
for i in range(300):
    sleep(0.5)
    cr=pt.position()
    pt.click(cr)