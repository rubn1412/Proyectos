import yfinance
import webbrowser
import pyperclip
import pyautogui
import time

time.sleep(5)
print(pyautogui.position())


destinatario = input("Introduzca Correo: ")
asunto = input("Introduzca el asunto: ")
ticker = input("Introduzca Ticker: ")
tiempo = input("Introduzca Tiempo: ")
descripcion = input("Introduzca cuerpo del Mensaje: ")

data=yfinance.Ticker(ticker).history(tiempo)
cierre = data.Close

max = round(cierre.max(),2)
min = round(cierre.min(),2)
medio = round(cierre.mean(),2)
datos = f""" \nAccion evaulada {ticker}\n
Valor Maximo: USD {max}\n
Valor Minimo: USD {min}\n
Valor Medio: USD {medio}\n

"""


webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
time.sleep(10)
pyautogui.click(x=135, y=183)

pyautogui.PAUSE(6)
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl","v")

pyautogui.hotkey("tab")

pyperclip.copy(asunto)
pyautogui.hotkey("ctrl","v")

pyautogui.hotkey("tab")
pyperclip.copy(descripcion)
pyautogui.hotkey("ctrl","v")

pyperclip.copy(datos)
pyautogui.hotkey("ctrl","v")

pyautogui.click(x=860, y=837)
