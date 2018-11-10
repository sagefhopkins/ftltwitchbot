import cv2
import numpy as np
import pyautogui as pyimg
import database_Controller as dbc

def find_Enemy_Image(image):
    templates = {
            "C:/Users/sagef/Documents/Development/ftltwitchbot/target/enemy_Cockpit.png" : "enemy_Cockpit",
            "C:/Users/sagef/Documents/Development/ftltwitchbot/target/enemy_Engine.png" : "enemy_Engine",
            "C:/Users/sagef/Documents/Development/ftltwitchbot/target/enemy_Oxygen.png" : "enemy_Oxygen",
            "C:/Users/sagef/Documents/Development/ftltwitchbot/target/enemy_Shield.png" : "enemy_Shield",
            "C:/Users/sagef/Documents/Development/ftltwitchbot/target/enemy_Weapon.png" : "enemy_Weapon"
    }
    for key, value in templates.iteritems():
        template = cv2.imread(key, 0)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        w, h = template.shape[::-1]
        result = cv2.matchTemplate(image_gray, template, cv2.TM_CCOEFF_NORMED)
        threshhold = .50
        location = np.where(result >= threshhold)
        for pt in zip(*location[::1]):
            cv2.rectangle(image, pt, (pt[0]+w, pt[1]+h), (0, 255, 255), 2)
            print pt[0], pt[1], value
        #cv2.namedWindow('enemy_Detected', cv2.WINDOW_NORMAL)
        #cv2.resizeWindow('enemy_Detected', 576, 324)
        cv2.imshow('enemy_Detected', image)
        cv2.waitKey(10)
def find_Image(image):


    templates = {
        "C:/Users/sagef/Documents/Development/ftltwitchbot/target/medic.png" : "Medic",
        "C:/Users/sagef/Documents/Development/ftltwitchbot/target/weapon.png" : "Weapons",
        "C:/Users/sagef/Documents/Development/ftltwitchbot/target/character.PNG" : "Characters",
        "C:/Users/sagef/Documents/Development/ftltwitchbot/target/cockpit.png" : "Cockpit",
        "C:/Users/sagef/Documents/Development/ftltwitchbot/target/door.png" : "Doors",
        "C:/Users/sagef/Documents/Development/ftltwitchbot/target/engine.png" : "Engine",
        "C:/Users/sagef/Documents/Development/ftltwitchbot/target/oxygen.png" : "Oxygen",
        "C:/Users/sagef/Documents/Development/ftltwitchbot/target/shield.png" : "Shield",
        "C:/Users/sagef/Documents/Development/ftltwitchbot/target/ftl_Logo.png" : "ftl_Logo",
        "C:/Users/sagef/Documents/Development/ftltwitchbot/target/enemy_Target.png" : "enemy_Target"
        }

    for key, value in templates.iteritems():
        template = cv2.imread(key, 0)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        w, h = template.shape[::-1]
        result = cv2.matchTemplate(image_gray, template, cv2.TM_CCOEFF_NORMED)
        threshhold = .90
        location = np.where(result >= threshhold)
        for pt in zip(*location[::-1]):
            cv2.rectangle(image, pt, (pt[0]+w, pt[1]+h), (0, 255, 255), 2)
            print pt[0], pt[1], value
            dbc.database_Update(value, pt[0], pt[1])
        cv2.namedWindow('detected',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('detected',576, 324 )
        cv2.imshow('detected', image)
        cv2.waitKey(10)
