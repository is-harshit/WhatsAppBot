import pyautogui as pt
from time import sleep
import pyperclip as py
import csv

def msg_det():
    cords = ()
    cords = pt.locateCenterOnScreen("H:\Whatsapp Bot CS\Green_dot.png", confidence=.85)
    print(cords)
    if cords is None:
        cords = [0, 0]
    else:
        pt.click(cords)


def get_message():
    py.copy("No reply")
    sleep(2)
    pt.click(442, 700)  # emoji
    sleep(2)
    pt.tripleClick(528, 310)  # select text
    pt.rightClick()
    pt.click(545, 324)  # copy
    sleep(1)
    whatsapp_message = py.paste()

    print("Message Recieved")
    print("Message is :", whatsapp_message)
    return (whatsapp_message)


def cords_get():
    while (True):
        sleep(2)
        posxy = pt.position()
        print(posxy)
        if posxy[0] == 0:
            break


def open_wa():
    pt.click(565, 749)


def response(message):
    pt.click(847, 693)
    pt.typewrite(message)
    pt.typewrite("\n", interval=.01)




def wa():

    wcord = pt.locateOnScreen("Whatsapp_logo.png", confidence=.85)
    if wcord is None:
        wcord = pt.locateCenterOnScreen("Whatsapp_logoh.png", confidence=.70)
    pt.click(wcord)

def msg_det():
    cords = pt.locateCenterOnScreen("Green_dot1.png", confidence=.92)
    print(cords)
    if cords is None:

        cords = (0, 0)
    else:
        pt.click(cords[0]-99,cords[1])
    return cords

def msg_write(msg):
    cords= pt.locateOnScreen("message_write.png",confidence=.85)
    pt.click(cords)
    pt.typewrite(msg)
    pt.typewrite("\n", interval=.01)

def msg_reciever():
    py.copy("No reply")
    global pos
    pos=pt.locateOnScreen("message_write.png",confidence=.85)
    pt.tripleClick(pos[0],pos[1]-65)
    sleep(.6)
    pt.rightClick(pos[0],pos[1]-65)
    pt.click(762,919)
    message=py.paste()
    print("the message is:",message)
    return message

