import cv2
import numpy as np
import pyautogui as pyimg


def find_Image(image):


    templates = {
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

    for key, value in templates.iteritems():
        template = cv2.imread(key, 0)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        w, h = template.shape[::-1]
        result = cv2.matchTemplate(image_gray, template, cv2.TM_CCOEFF_NORMED)
        threshhold = .85
        location = np.where(result >= threshhold)
        for pt in zip(*location[::-1]):
            cv2.rectangle(image, pt, (pt[0]+w, pt[1]+h), (0, 255, 255), 2)
            print pt[0], pt[1], value

        cv2.imshow('detected', image)
        cv2.waitKey(10)
