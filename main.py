from datetime import datetime
from time import sleep
from pyfiglet import figlet_format
from pystyle import Colorate, Colors
from os import system

def displayTime():
    system('cls')
    timeNow = datetime.now()
    h = timeNow.hour
    m = timeNow.minute
    s = timeNow.second
    p = timeNow.strftime('%p')

    timeStr = f'{h} : {m} : {s} {p}'

    timeStr = figlet_format(timeStr)
    timeStr = Colorate.Horizontal(Colors.blue_to_purple, timeStr)

    print(timeStr)

    sleep(1)
    displayTime()

displayTime()