import os
import keyboard
from pathlib import Path
from shutil import copyfile
from time import sleep

#You can change the save Hotkey here :)
saveHotkey = 'c'

# If you want to use a loadHotKey so that you have to press "f + 1" to select slot 1 for example instead of only 1 (currently).
# You gotta add a # before line 44 and remove it in line 45 as well as removing the # in line 12
#loadHotKey = 'f'

# get the save file location and create a folder where the save states are gonna be saved to
home = str(Path.home()) + '\\AppData\\LocalLow\\Team Cherry\\Hollow Knight\\'
os.makedirs(home + 'saveStatesFolder', exist_ok=True)

#Thanks for vali's algorithm brain to make me not hardcode this shit <3
def make_copy_function(slot):
    def kb_input_copy_slot():
        #copy the current quick save slot to the save state folder)
        copyfile(home + 'minisavestates-saved.json', home + f'saveStatesFolder\\minisavestates-saved{slot}.json')
        print("Copied file to slot: " + str(slot))
        sleep(0.5)

    return kb_input_copy_slot

for key in range(10):
    #add Hotkeys for all number-row-keys
    keyboard.add_hotkey(f'{saveHotkey} + {key}', make_copy_function(key))

def make_paste_function(slot):
    def kb_input_paste_slot():
        try:
            #Paste the save files from the folder to the quickslot
            copyfile(home + f'saveStatesFolder\\minisavestates-saved{slot}.json', home + 'minisavestates-saved.json')
            print("Selected slot: " + str(slot))
        except:
            print("File doesn't exist on slot: " + str(slot))
        sleep(0.5)

    return kb_input_paste_slot

for key in range(10):
    keyboard.add_hotkey(f'{key}', make_paste_function(key))
    #keyboard.add_hotkey(f'{loadHotKey} + {key}', make_paste_function(key))

keyboard.wait()