import pyautogui
import pandas as pd
import time

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("win", "up")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x=726, y=411)
pyautogui.write("someemail@email.com")
pyautogui.press("tab")
pyautogui.write("my own password")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

database = pd.read_csv("produtos.csv")
print(database)

for entry in database.index:
    pyautogui.PAUSE = 0.1
    pyautogui.click(x=713, y=293)
    pyautogui.write(str(database.loc[entry, "codigo"]))
    pyautogui.press("tab")
        
    pyautogui.write(str(database.loc[entry, "marca"]))
    pyautogui.press("tab")
        
    pyautogui.write(str(database.loc[entry, "tipo"]))
    pyautogui.press("tab")
        
    pyautogui.write(str(database.loc[entry, "categoria"]))
    pyautogui.press("tab")
        
    pyautogui.write(str(database.loc[entry, "preco_unitario"]))
    pyautogui.press("tab")
        
    pyautogui.write(str(database.loc[entry, "custo"]))
    pyautogui.press("tab")

    obs = database.loc[entry, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)