from pyautogui import press, typewrite, hotkey

list = open("list.txt","r")
data = list.read()
data_into_list = data.replace('\n', ' ').split(".") 

print(data_into_list)

count = data_into_list.count()

for item in data_into_list:
    I = 0
    typewrite(I in data_into_list)
    I = I + 1
    if I == 10:
        break


list.close()
    # Add an indented block here

