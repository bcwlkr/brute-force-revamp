from pynput import keyboard
from pynput.keyboard import Controller

list = open("list.txt","r")

data = list.read()

data_into_list = data.replace('\n', ' ').split(".") #cleans up the data and puts it into a list

global my_bool
my_bool = False

def on_activ(key):
    global my_bool
    if key == keyboard.Key.f1:
        if my_bool == False:
            my_bool = True
            keyboard = Controller()
            I = 0
            for item in data_into_list:
                keyboard.type(item) 
                keyboard.press(keyboard.enter) 
                I = I + 1
                #if I == 10:   for testing purposes
                    # break     for testing purposes
        elif my_bool == True:
            my_bool = False
        
list.close()
