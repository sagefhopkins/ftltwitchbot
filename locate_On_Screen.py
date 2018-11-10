import pyautogui
import numpy as np
import cv2 as cv
import time
import match_By_Pixel as mbp
import database_Controller as dbc

#pyautogui.click(button='right')
#img = pyautogui(region=(0,0,300,400))


"""dbc.database_Insert('Medic', 1, 1)
dbc.database_Insert('Weapons', 1, 1)
dbc.database_Insert('Characters', 1, 1)
dbc.database_Insert('Cockpit', 1, 1)
dbc.database_Insert('Doors', 1, 1)
dbc.database_Insert('Engine', 1, 1)
dbc.database_Insert('Oxygen', 1, 1)
dbc.database_Insert('Shield', 1, 1)
dbc.database_Insert('ftl_Logo', 1, 1)
dbc.database_Insert('enemy_Cockpit', 1, 1)
dbc.database_Insert('enemy_Engine', 1, 1)
dbc.database_Insert('enemy_Oxygen', 1, 1)
dbc.database_Insert('enemy_Shield', 1, 1)
dbc.database_Insert('enemy_Target', 1, 1)
dbc.database_Insert('enemy_Weapon', 1, 1)"""



while True:
    enemy_Targets = []
    ftl = dbc.database_Read('ftl_Logo')
    for name, x, y in ftl:
        print name , x, y
    enemy_Target = dbc.database_Read('enemy_Target')
    for name, x, y in enemy_Target:
        enemy_Targets.insert(0, name)
        enemy_Targets.insert(1, x)
        enemy_Targets.insert(2, y)


    image = np.array(pyautogui.screenshot())
    mbp.find_Image(image)

    image_Enemy = np.array(pyautogui.screenshot(region=(enemy_Targets[1], enemy_Targets[2],432 , 787)))
    mbp.find_Enemy_Image(image_Enemy)
