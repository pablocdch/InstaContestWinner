import pyautogui
import random

i=0

def accion():
    pyautogui.hotkey('ctrl', 'c')                                    #Copia la celda
    pyautogui.click(x=588, y=1751, duration = 3)  #Abre Brave
    pyautogui.click(x=1912, y=1350, duration= 3)  #Click en add a comment
    pyautogui.hotkey('ctrl', 'v')                                    #Pega la celda
    pyautogui.click(x=2216, y=1351, duration= random.randint(25,30))  #Click en post

while i < 30:
    randNum = random.randint(0, 13)
    print(randNum)
    
    if randNum == 0:
        pyautogui.click(x=285, y=1768, duration=1)  #click excel
        pyautogui.click(x=272, y=574, duration=1)   #click celda a1
\        accion()
        i = i + 1
    elif randNum == 1:
        pyautogui.click(x=285, y=1768, duration=1)  #click excel
        pyautogui.click(x=305, y=616, duration=1)   #click celda a2
        accion()
        i = i + 1
    elif randNum == 2:
        pyautogui.click(x=285, y=1768, duration=1)  #click excel
        pyautogui.click(x=304, y=666, duration=1)   #click celda a3
        accion()
        i = i + 1
    elif randNum == 3:
        pyautogui.click(x=285, y=1768, duration=1)  #click excel
        pyautogui.click(x=200, y=707, duration=1)   #click celda a4
        accion()
        i = i + 1
    elif randNum == 4:
        pyautogui.click(x=285, y=1768, duration=1)  #click excel
        pyautogui.click(x=200, y=751, duration=1)   #click celda a5
        accion()
        i = i + 1
    elif randNum == 5:
        pyautogui.click(x=285, y=1768, duration=1)  #click excel
        pyautogui.click(x=200, y=795, duration=1)   #click celda a6
        accion()
        i = i + 1
    elif randNum == 6:
        pyautogui.click(x=285, y=1768, duration=1)  #click excel
        pyautogui.click(x=200, y=839, duration=1)   #click celda a7
        accion()
        i = i + 1
    elif randNum == 7:
        pyautogui.click(x=285, y=1768, duration=1)  #click excel
        pyautogui.click(x=318, y=903, duration=1)   #click celda a8
        accion()
        i = i + 1
    elif randNum == 8:
        pyautogui.click(x=285, y=1768, duration=1)  #click excel
        pyautogui.click(x=305, y=949, duration=1)   #click celda a9
        accion()
        i = i + 1
    elif randNum == 9:
        pyautogui.click(x=285, y=1768, duration=1)  #click excel
        pyautogui.click(x=335, y=997, duration=1)   #click celda a10
        accion()
        i = i + 1
    elif randNum == 10:
        pyautogui.click(x=285, y=1768, duration=1)  #click excel
        pyautogui.click(x=409, y=1050, duration=1)  #click celda a11
        accion()
        i = i + 1
    elif randNum == 11:
        pyautogui.click(x=285, y=1768, duration=1)  #click excel
        pyautogui.click(x=522, y=1103, duration=1)  #click celda a12
        accion()
        i = i + 1
    elif randNum == 12:
        pyautogui.click(x=285, y=1768, duration=1)  #click excel
        pyautogui.click(x=480, y=1139, duration=1)  #click celda a13
        accion()
        i = i + 1
    elif randNum == 13:
        pyautogui.click(x=285, y=1768, duration=1)  #click excel
        pyautogui.click(x=452, y=1195, duration=1)  #click celda a14
        accion()
        i = i + 1
    else:
        print('No salio ningun numero')
