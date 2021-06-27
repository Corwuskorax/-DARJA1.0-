#data for =SPAMMER=
# @corwik
# V 1.0
from colorama import init, Fore
from banners import logo
import os
import time
import pyautogui

init(autoreset=True)

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def a():
    clear()
    print(logo)
    time.sleep(1)
    message=input(Fore.BLUE + 'Введите сообщение для спама на английском языке:')
    print(Fore.BLUE + 'Успейте за 6 секунд открыть окно ввода сообщения!')
    time.sleep(6)
    iterations = 10
    for i in range(iterations):
        pass
    while iterations > 0:
        iterations -=1

        pyautogui.typewrite(message.strip()) 
        pyautogui.press('enter')
    print(Fore.GREEN + 'Готово!')

def b():
    clear()
    print(logo)
    time.sleep(1)
    message=input(Fore.BLUE + 'Введите сообщение для спама на английском языке:')
    print(Fore.BLUE + 'Успейте за 6 секунд открыть окно ввода сообщения!')
    time.sleep(6)
    iterations = 100
    for i in range(iterations):
        pass
    while iterations > 0:
        iterations -=1

        pyautogui.typewrite(message.strip()) 
        pyautogui.press('enter')
    print(Fore.GREEN + 'Готово!')

def c():
    clear()
    print(logo)
    time.sleep(1)
    message=input(Fore.BLUE + 'Введите сообщение для спама на английском языке:')
    print(Fore.BLUE + 'Успейте за 6 секунд открыть окно ввода сообщения!')
    time.sleep(6)
    iterations = 500
    for i in range(iterations):
        pass
    while iterations > 0:
        iterations -=1

        pyautogui.typewrite(message.strip()) 
        pyautogui.press('enter')
    print(Fore.GREEN + 'Готово!')

def d():
    clear()
    print(logo)
    time.sleep(1)
    message=input(Fore.BLUE + 'Введите сообщение для спама на английском языке:')
    print(Fore.BLUE + 'Успейте за 6 секунд открыть окно ввода сообщения!')
    time.sleep(6)
    iterations = 1000
    for i in range(iterations):
        pass
    while iterations > 0:
        iterations -=1

        pyautogui.typewrite(message.strip()) 
        pyautogui.press('enter')
    print(Fore.GREEN + 'Готово!')

def e():
    clear()
    print(logo)
    time.sleep(1)
    message=input(Fore.BLUE + 'Введите сообщение для спама на английском языке:')
    print(Fore.BLUE + 'Успейте за 6 секунд открыть окно ввода сообщения!')
    time.sleep(6)
    iterations = 1500
    for i in range(iterations):
        pass
    while iterations > 0:
        iterations -=1

        pyautogui.typewrite(message.strip()) 
        pyautogui.press('enter')
    print(Fore.GREEN + 'Готово!')

def f():
    clear()
    print(logo)
    time.sleep(1)
    message=input(Fore.BLUE + 'Введите сообщение для спама на английском языке:')
    print(Fore.BLUE + 'Успейте за 6 секунд открыть окно ввода сообщения!')
    time.sleep(6)
    iterations = 2000
    for i in range(iterations):
        pass
    while iterations > 0:
        iterations -=1

        pyautogui.typewrite(message.strip()) 
        pyautogui.press('enter')
    print(Fore.GREEN + 'Готово!')
    
