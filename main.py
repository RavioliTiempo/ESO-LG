import pyautogui, time, os
IsGW2Gay = True

while IsGW2Gay == True:
        
    launcherplay = pyautogui.locateCenterOnScreen('launcher_play_btn.png', confidence=0.9)
    login = pyautogui.locateCenterOnScreen('login_btn.png', confidence=0.9)
    password_field = pyautogui.locateCenterOnScreen('pass_field.png', confidence=0.9)


    if(launcherplay != None):
        pyautogui.dragTo(launcherplay[0], launcherplay[1], 2, button='left')
        time.sleep(2)
        pyautogui.click(launcherplay[0], launcherplay[1])
        print('Launching Game')

    if(password_field != None):
        pyautogui.write('Password Here')
        pyautogui.dragTo(login[0], login[1], 1, button='left')
        time.sleep(1)
        pyautogui.click(login[0], login[1])
        print('Entering Password and logging in')
        quit()

