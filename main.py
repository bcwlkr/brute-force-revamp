from pynput import keyboard
from pynput.keyboard import Controller

list = open("list.txt","r")
data = list.read()
data_into_list = data.replace('\n', ' ').split(".") #cleans up the data and puts it into a list

print(data_into_list)

count = len(data_into_list)

keyboard = Controller()
I = 0
for item in data_into_list:
    keyboard.type(item) 
    keyboard.press(keyboard.enter) 
    I = I + 1
    if I == 10:
        break


list.close()
