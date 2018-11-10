import pyautogui
import numpy as np
import cv2 as cv
import time
import draw_On_Screen as draw
import match_By_Pixel as mbp

#pyautogui.click(button='right')
#img = pyautogui(region=(0,0,300,400))
images = {
    "C:/Users/sagef/Documents/Development/FTL Chat Bot/target/medic.png" : "Medic",
    "C:/Users/sagef/Documents/Development/FTL Chat Bot/target/weapon.png" : "Weapons",
    "C:/Users/sagef/Documents/Development/FTL Chat Bot/target/character.PNG" : "Characters",
    "C:/Users/sagef/Documents/Development/FTL Chat Bot/target/cockpit.png" : "Cockpit",
    "C:/Users/sagef/Documents/Development/FTL Chat Bot/target/door.png" : "Doors",
    "C:/Users/sagef/Documents/Development/FTL Chat Bot/target/engine.png" : "Engine",
    "C:/Users/sagef/Documents/Development/FTL Chat Bot/target/oxygen.png" : "Oxygen",
    "C:/Users/sagef/Documents/Development/FTL Chat Bot/target/shield.png" : "Shield",
    "C:/Users/sagef/Documents/Development/FTL Chat Bot/target/ftl_Logo.png" : "FTL Logo"
    }

"""while True:
    img = pyautogui.screenshot('out.png')
    submit = {}
    for key, value in images.iteritems():
        detection = pyautogui.locateCenterOnScreen(key, grayscale=True)
        if detection != None:
            print(value + ' detected')
            submit[value] = '[{},{}]'.format(detection[0], detection[1])
            print submit
        else:
            print "Nothing Detected!"
    draw.box_Image(submit, 'out.png')"""
while True:
    image = np.array(pyautogui.screenshot())
    mbp.find_Image(image)
