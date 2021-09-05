from os import makedirs, walk, remove, path
from keyboard import wait, add_hotkey
from pathlib import Path
from shutil import copyfile
from time import sleep
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
import glob

# You can change the save Hotkey here :)
saveHotkey = 'c'

# If you want to use a loadHotKey so that you have to press "f + 1" to select slot 1 for example instead of pressing only 1 (currently).
# You have to add a # before line 44 and remove it in line 45 as well as removing the # in line 12
# loadHotKey = 'f'

# get the save file location and create a folder where the save states are gonna be saved to
home = str(Path.home()) + '\\AppData\\LocalLow\\Team Cherry\\Hollow Knight\\'
global foldername
foldername = 'debugPurpose'

makedirs(home + 'saveStatesFolder', exist_ok=True)

# Methods:
#create labels for every created folder
d = {}
def refreshFolderLabels():
    x = [x[0] for x in walk(home + 'saveStatesFolder')]
    for i in range(1,len(x)):
        label = Label(test3, text = x[i][len(home + 'saveStatesFolder')+1:]).grid(row = 1 + i, column = 0)
        d["label{0}".format(i)] = x[i][len(home + 'saveStatesFolder')+1:]
        button = Button(test3, text = "select", command = lambda i=i: selectFolder(i)).grid(row = 1 + i, column = 1)

def createFolder(folder):
    if (not path.exists(home + 'saveStatesFolder\\' + folder)):
        makedirs(home + 'saveStatesFolder\\' + folder, exist_ok = True)
        d["label{0}".format(len(d)+1)] = folder
        labelnew = Label(test3, text = folder).grid(row = len(d) + 2, column = 0)
        button = Button(test3, text = "select", command = lambda: selectFolder(len(d))).grid(row = len(d) + 2, column = 1)
    else:
        print('Folder already exists')


def selectFolder(slot):
    global foldername
    foldername = d["label{0}".format(slot)]
    CurrSelec.set(f'Currently selected: {foldername}')

def searchFile(slot):
    gameFileName = askopenfilename()
    if (content[slot] == gameFileName) : return
    if (not gameFileName) :
        return
    f = open("ChangeSaveFiles.txt", 'w')
    content[slot] = gameFileName
    f.write('\n'.join(str(x) for x in content))
    f.write('\nEnd of SaveFiles\n')
    f.close()
    print(content[slot].rsplit('/', 1)[-1])

def selectFile(slot):
    # If there's no game file selected, it'll just assume it's in the same folder
    if (content[3] == 'Slot 3'):
        if (content[slot] != f'Slot {slot}'):
            copyfile(content[slot],content[slot][:content[slot].index("Managed") + 8] + 'Assembly-CSharp.dll')
    else:
        if (content[slot] != f'Slot {slot}'):
            copyfile(content[slot],content[3])

def selectSaveState(slot):
    copyfile(home + "saveStatesFolder\\" + foldername + f'\\minisavestates-saved{slot}.json', home + 'minisavestates-saved.json')
    varSelect.set("Selected slot: " + str(slot))

def createNewSaveState(slot):
    copyfile(home + 'minisavestates-saved.json', home + "saveStatesFolder\\" + foldername + f'\\minisavestates-saved{slot}.json')
    varCopy.set("Copied file to slot: " + str(slot))
    createSaveStateUI()

def createSaveFileWindow():
    global createSaveStateUI
    def createSaveStateUI():
        global fileIndex
        for filename in glob.iglob(home + 'saveStatesFolder\\' + foldername + '/**/*.json', recursive=True):
            fileIndex = int(filename.split("saved",1)[1][:1])
            label = Label(saveFileWindow, text = filename[len(home + 'saveStatesFolder\\' + foldername) + 1:-5]).grid(row = 1 + fileIndex, column = 0)
            button = Button(saveFileWindow, text = "select", command = lambda fileIndex=fileIndex: selectSaveState(fileIndex)).grid(row = 1 + fileIndex, column = 1)
    saveFileWindow = Toplevel(root)
    createSaveStateUI()
    # buttonCreate = Button(saveFileWindow, text = "Copy into next open slot", command = lambda : createNewSaveState(fileIndex + 1)).grid(row = 0, column = 0)


#Get the file locations from txt
content = ['Slot 0', 'Slot 1', 'Slot 2', 'Slot 3']
if path.exists('ChangeSaveFiles.txt'):
    index = 0
    with open('ChangeSaveFiles.txt') as f:
        for line in f:
            if (line != 'End of SaveFiles\n') and index < len(content):
                content[index] = line.strip('\n')
                index += 1
# Makes it so the code doesn't break when you don't have everything selected (sounds like there should be a better way but you can't make me
if (len(content) != 4):
    while (len(content) != 4):
        content.append(f'Slot {len(content)}')
#Create not UI
root = Tk()
varCopy = StringVar()
varSelect = StringVar()

varCopy.set(F'Press {saveHotkey} + [number] to copy current savestate')
varSelect.set('Press [number] to select a slot')

frame1 = Frame(root).pack()
frame2 = Frame(root).pack()
frame3 = Frame(root).pack()
test = Frame(frame1)
test.pack()
test2 = Frame(frame2)
test2.pack()
test3 = Frame(frame3)
test3.pack()

m = Menu(frame2)
root.config(menu = m)

lblCopy = Label(test2, textvariable = varCopy).grid(row=0, column=0)
lblSelect = Label(test2, textvariable = varSelect).grid(row=0, column=1)

Folder1 = Entry(test,width = 20)
Folder1.grid(row=1,column=0)
Folder1.insert(0, "Create a folder")
ButtonF1 = Button(test, text="Weeee", command = lambda: createFolder(Folder1.get())).grid(row=1, column=1)

chooseFileMenu = Menu(m,tearoff = 0)
chooseFileMenu.add_command(label = 'Search Game Assembly File', command = lambda : searchFile(3))
chooseFileMenu.add_command(label = 'Search Vanilla File', command = lambda : searchFile(0))
chooseFileMenu.add_command(label = 'Search Modded File', command = lambda : searchFile(1))
chooseFileMenu.add_command(label = 'Search Minisavestates File', command = lambda : searchFile(2))
m.add_cascade(label = 'Search Files', menu = chooseFileMenu)

selectFileMenu = Menu(m,tearoff = 0)
selectFileMenu.add_command(label = 'Select Vanilla File', command = lambda : selectFile(0))
selectFileMenu.add_command(label = 'Select Modded File', command = lambda : selectFile(1))
selectFileMenu.add_command(label = 'Select Minisavestates File', command = lambda : selectFile(2))
m.add_cascade(label = 'Select Files', menu = selectFileMenu)

saveStateMenu = Menu(m, tearoff = 0)
saveStateMenu.add_command(label = "Open Window", command = createSaveFileWindow)
m.add_cascade(label = 'Save State Menu', menu = saveStateMenu)

CurrSelec = StringVar()
if (foldername != 'debugPurpose'):
    CurrSelec.set(f'Currently selected: {foldername}')
else:
    CurrSelec.set(f'No Folder selected ):')
lblSelected = Label(test, textvariable = CurrSelec).grid(row=2,column=0)

refreshFolderLabels()

# Thanks for vali's algorithm brain to make me not hardcode this shit <3
def make_copy_function(slot):
    def kb_input_copy_slot():
        # copy the current quick save slot to the save state folder)
        print(foldername)
        if (foldername != 'debugPurpose'):
            copyfile(home + 'minisavestates-saved.json', home + "saveStatesFolder\\" + foldername + f'\\minisavestates-saved{slot}.json')
            varCopy.set("Copied file to slot: " + str(slot))
        sleep(0.2)
    return kb_input_copy_slot

for key in range(10):
    # add Hotkeys for all number-row-keys
    add_hotkey(f'{saveHotkey} + {key}', make_copy_function(key))

def make_paste_function(slot):
    def kb_input_paste_slot():
        try:
            # Paste the save files from the folder to the quickslot
            if (foldername != "debugPurpose"):
                copyfile(home + "saveStatesFolder\\" + foldername + f'\\minisavestates-saved{slot}.json', home + 'minisavestates-saved.json')
                varSelect.set("Selected slot: " + str(slot))
        except:
            varSelect.set("File doesn't exist on slot: " + str(slot))
        sleep(0.2)

    return kb_input_paste_slot

for key in range(10):
    add_hotkey(f'{key}', make_paste_function(key))
    # add_hotkey(f'{loadHotKey} + {key}', make_paste_function(key))

root.mainloop()
wait()
