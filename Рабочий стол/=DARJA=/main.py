#main for =DARJA=
#telegram @corwik
# V 1.0

import time
import os
from colorama import init, Fore
from banners import *
from data import a, b, c, d, e, f
import pyautogui
init(autoreset=True)

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear()
print(menu)
men=input(Fore.BLUE + '>>')
if(men=='1'):
    clear()
    print(kolichestvo)
    kol=input(Fore.BLUE + '>>')
    if(kol=='1'):
        a()
    elif(kol=='2'):
        b()
    elif(kol=='3'):
        c()
    elif(kol=='4'):
        d()
    elif(kol=='5'):
        e()
    elif(kol=='6'):
        f()
    else:
        print(Fore.RED + 'Введено инвалидное значение.')
        time.sleep(1)
        exit
elif(men=='2'):
    time.sleep(1)
    clear()
    exit
else:
    print('Введено инвалидное значение!')
    clear()
    exit

