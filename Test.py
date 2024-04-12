
import pyautogui as pt
from time import sleep
import csv
import random
import pickle

def response():
    lfile=open("Link.csv")
    opt=csv.reader(lfile)
    op=random.randint(1,11)
    for row in opt:
        print (row[1])
    lfile.close()


def cross():
    cross = pt.locateOnScreen("cross.png")
    pt.click(cross)

'''
                       elif int(option)==3:
                           msg_write("1.jio\n2.airtel")
                           ot=msg_reciever()
                           if op==int("1"):
                               
                       elif int(option)==4:
                           msg_write("lol")

lfile = open("Link.csv")
opt = csv.reader(lfile)
for row in opt:
   print(row[0])

lfile.close()

option=input("Enter:")
print (type(option))
if (not(option.isdigit())) or int(option) > 14 or int(option)<0 :
    option = 15

print(option)

 
List="Atlas provides the following services:\n1.Vac link\n2.News\n3.Jio Recharge\n4.Airtel Recharge\n5.JEE Mains Test Sample Papers\n6.JEE Advanced Test Sample Papers\n7.NEET Test sample paper\n8.Entrance coaching videos\n9.Covid Status\n10.Python Tutorial videos\n11.View Code\n12.Feedback\n13.Flight \n14.NCERT Textbook"
        msg_write(List)
'''

'''f=input("Enter feedbasvx:")
l=[]
l.append(f)
f1=open("Feedback.dat","ab")
pickle.dump(l,f1)
f1.close()'''

sleep(6)
cross()

