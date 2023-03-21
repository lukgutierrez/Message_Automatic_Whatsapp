# import keyboard
# import time
# ENTER = "enter"
# HOTKEY = "esc"
# NAME_FILE = "miarchivo.txt"
# SALE = False
# def salir() -> None:
#     global SALE
#     SALE = True
#     print("ACTIVE PROGRAM")
# def massagesms(msj:str = "hello") -> None: 
#     keyboard.write(msj)
#     keyboard.press(ENTER)
# def main() -> None:
#     keyboard.add_hotkey(HOTKEY, lambda: salir())
#     while True:
#      time.sleep(5)
#      print("")
#     with open(NAME_FILE,"r") as file:
#        for linea in file:
#           list_words = linea.split()
#           for word in list_words:
#              if SALE:
#                 exit()
#             massagesms(palabra.strip())

# main()