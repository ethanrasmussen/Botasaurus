import pyautogui
import cv2
import time

def start_game():
    start = None
    while start == None:
        try:
            start = pyautogui.locateOnScreen('start_dino.png', confidence=0.9)
        except:
            pass
    pyautogui.press('space')
    print("Game started!")

def find_dino():
    dino = pyautogui.locateCenterOnScreen('dino.png', confidence=0.9)
    print("Found dino!")
    print("Location: "+str(dino[0])+", "+str(dino[1]))
    return dino

def detect_cactus(dino):
    x = int(dino[0] + 100)
    y = int(dino[1])
    #img = pyautogui.screenshot()
    pix = pyautogui.pixel(x, y)
    #print(pix)
    if pix[0] == 83 and pix[1] == 83 and pix[2] == 83:
        print("Cactus detected!")
        return True
    else:
        return False

def jump():
    pyautogui.press('space')
    print("Jumped!")

def main():
    try:
        start_game()
    except:
        print("Could not start.")
        quit()
    playing = True
    time.sleep(0.5)
    dino = find_dino()
    while playing:
        if detect_cactus(dino):
            jump()
        else:
            pass

main()
        
