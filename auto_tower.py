
import pyautogui #pip install pyautogui
import time
import os
import pygetwindow as gw

#After each pyautogui instruction waits
pyautogui.PAUSE = 0.1
#If you drag your mouse to the upper left will not abort program
pyautogui.FAILSAFE = True

def focus_window(window_title):
    try:
        window = gw.getWindowsWithTitle(window_title)[0]
        window.activate()
        center_x = window.left + window.width // 2
        center_y = window.top + window.height // 2            
        pyautogui.click(center_x,center_y)

    except IndexError:
        print("Emulator window not found")

focus_window("Bluestacks App Player")

level_counter=0

def locate_and_click(path,conf=0.6):

    location=pyautogui.locateCenterOnScreen(path,confidence=conf)
    pyautogui.doubleClick(location)
    print("Clicked on", path)

def image_detected(image_path, confidence=0.6):
    """Check if the image is detected on the screen."""
    try:
        # Attempt to locate the image on the screen
        return pyautogui.locateOnScreen(image_path, confidence=confidence) is not None
    except Exception as e:
        #print(f"Image not found {e}")
        return False  # Return False in case of an error

start_time=time.time()

while level_counter <= 25 :

    try :
        locate_and_click("C:/Users/wangc/OneDrive/Documents/auto_tower/commencer_combat.png")
    except:
        print("commencer_combat.png non trouvé")
        break

    while not image_detected("C:/Users/wangc/OneDrive/Documents/auto_tower/detect_fin.png"):

        time.sleep(0.5)
        # print("Waiting for combat end")
 
    active_window = gw.getActiveWindow()

    if active_window is not None:
        time.sleep(1)
        center_x = active_window.left + active_window.width // 1.9 
        center_y = active_window.top + active_window.height // 2            
        pyautogui.doubleClick(center_x,center_y)

    time.sleep(0.7)

    locate_and_click("C:/Users/wangc/OneDrive/Documents/auto_tower/confirmer_le_dispositif.png",0.7)

    time.sleep(1.2)
    
    locate_and_click("C:/Users/wangc/OneDrive/Documents/auto_tower/etage_suivant.png")

    time.sleep(1.7)

    level_counter +=1
    print("level_counter",level_counter)
    print("time",(time.time()-start_time)/60)

end_time=time.time()

print("Tour automate terminée")
print("Temps mis",end_time-start_time)