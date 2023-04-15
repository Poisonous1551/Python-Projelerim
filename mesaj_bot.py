import pyautogui
import time 

x=int(input('Bir Sayı Giriniz: '))

time.sleep(10)

while x>0:
    pyautogui.write('<Message>')
    pyautogui.press('enter')
    x-=1
    time.sleep(1)