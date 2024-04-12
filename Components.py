"""

1.Vac link /
2.News/
.recharge link
  3  jio/
   4 airtel/
.Test Sample Papers
5      Jee m/
 6     Jee ad/
  7    neet/
8.Entrance coaching videos/

9.Covid Status/
10.Python Tutorial videos/
11View Code/
12.Feedback/
13.Flight /
14.NCERT Teextbook



Whatsapp
Hotel
Trivago
Covid
"""
import csv

import pyautogui as pt
from time import sleep
import pyperclip as py

def response(message):
    pt.click(847,693)
    pt.typewrite(message)
    pt.typewrite("\n", interval=.01)

f1 = open("Links.csv", 'a')
f2 = csv.writer(f1)
a1 = ["Vac link", "https://selfregistration.cowin.gov.in"]
a2 = ["News", "https://news.google.com/topstories"]
rec = [a1, a2]
for i in range(2):
    f2.writerow(rec[i])

f1.close

#3.1https://www.jio.com/en-in/no-daily-limit-plans JIO
#3.2https://www.airtel.in/recharge-online Airtel
#1.https://selfregistration.cowin.gov.in/ Vac
#2.https://news.google.com/topstories News
#4.1https://www.vedantu.com/iit-jee/jee-main-sample-papers
#4.2https://www.vedantu.com/iit-jee/jee-advanced-sample-papers
#4.https://medicine.careers360.com/articles/neet-sample-paper
#10.https://www.makemytrip.com/flights/
#5.https://www.youtube.com/c/UnacademyJEE/featured
#5.https://www.youtube.com/channel/UCwdvPgmU5qHPB2NsDLAmS1g ATP Star JEE
#5.https://www.youtube.com/channel/UC8jD2MO_NUnI-TASWQp-7NQ/featured NEET101
#6.https://www.bing.com/search?q=covid+19&cvid=d60d712bf3aa477189f678e7203c2d1b&aqs=edge.2.69i57j0l6.5951j0j1&pglt=2081&FORM=ANSPA1&PC=U531
#https://youtu.be/dQw4w9WgXcQ rickroll
#7.https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ free code
#11.https://ncert.nic.in/textbook.php
