# Install for =DARJA=
# telegram @corwik

import os
import time
from banners import *

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear()
print(install)
time.sleep(1)
print('Устанавливаю неоходимые библиотеки...')
os.system('pip install colorama')
from colorama import init, Fore
init(autoreset=True)
clear()
time.sleep(1)
print(logo)
print(Fore.BLUE + 'Установлю остальное.')
os.system('pip install pyautogui')
print(Fore.GREEN + 'Установка завершена! По всем вопросам к @corwik')
clear()
time.sleep(5)
exit
