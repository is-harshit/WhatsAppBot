import pyautogui as pt
import pyperclip as py
from time import sleep
import csv


def wa():
    wcord = pt.locateOnScreen("Whatsapp_logo.png", confidence=.85)
    if wcord is None:
        wcord = pt.locateCenterOnScreen("Whatsapp_logoh.png", confidence=.70)
    pt.click(wcord)

def msg_det():
    cords = pt.locateCenterOnScreen("Green_dot2.png", confidence=.92)
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
    pt.tripleClick(pos[0]-75,pos[1]-70)
    sleep(.6)
    pt.rightClick(pos[0]-75,pos[1]-70)
    print(pos)
    pt.doubleClick(pos[0]-45,pos[1]-400)
    sleep(1)
    message=py.paste()
    print("the message is:",message)
    return message

def cords_get():
   while (True):
        sleep(2)
        posxy = pt.position()
        print(posxy)
        if posxy[0] == 0:
            break


def cross():
    cross = pt.locateOnScreen("cross.png")
    pt.click(cross)

def Continue():
    msg_write("Would You Like to Continue?")
    while True:
        sleep(5)
        res = msg_reciever()
        print(res)
        if res.upper() == "NO REPLY":
            cross()
        elif not(res.upper()=="YES" or res.upper()=="Y" or res.upper()=="NO" or res.upper()=="N"):
            cross()
            msg_write("Yes/No?")
        else:
           return res

flag=0
wa()
while True:
    msg_det()
    msg=msg_reciever()
    if msg.upper()=="START BOT":
        msg_write("Welcome to Atlas!")
        msg_write("---------------------------------")
        lfile = open("Link.csv")
        opt = csv.reader(lfile)
        for row in opt:
            msg_write(row[0])
        lfile.close()
        msg_write("---------------------------------")
        msg_write("Enter Your Option:")
        while True:
            sleep(15)
            option=msg_reciever()
            if option.upper()=="NO REPLY":
                cross()
                continue
            else:
                if not option.isdigit() or int(option) > 14 or int(option)<0:
                    option=15
                lfile = open("Link.csv")
                opt = csv.reader(lfile)
                for row in opt:
                    if option!="12":
                        if opt.line_num==int(option):
                            msg_write(row[1])
                    else:
                            msg_write("Enter your Feedback:")
                            msg_write("(No Emoji's)")
                            sleep(50)
                            fd=msg_reciever()
                            if fd=="No reply":
                                msg_write("FeedBack Not Received!")
                                break
                            else:
                                msg_write("Feedback Received")
                                f1=open("Feedback.txt","a")
                                f1.write(fd)
                                f1.write("\n")
                                f1.close()
                            break
                lfile.close()
            rep=Continue()
            if rep[0].upper()=="NO" or rep[0].upper()=="N":
                msg_write("Thank You!!")
                flag=1
                break
            elif rep[0].upper()=="YES" or rep[0].upper()=="Y":
                msg_write("Enter Your Option:")
                continue
    else:
        cross()
        sleep(5)
    if flag==1:
        break
