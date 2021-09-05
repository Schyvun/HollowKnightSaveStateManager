Download the Python File and execute it (requires python to be installed, which windows usually already has, otherwise you can install it here https://www.python.org/downloads/
Other otherwise you can download the exe file in Release and it'll work either way

This script manages your save states created by Yuri's save state mod found here: https://github.com/Yurihaia/MiniSavestates/releases
You can edit the hotkeys by right clicking the python file and editing it with notepad++ (for example). Then follow the instructions in the file (The hotkey's are right on top of the file :)
Current hotkeys are: "c + [top row number key 0-9]" to save and "[top row number keys 0-9]" to select

New in 1.1:
You can now change between modded and unmodded Hollow Knight. Simply search for all versions you want to change between:

-Game Assembly File: Your game's currently used game file. This is solely for the program to know where it's located. Otherwise if your other Assembly Files are in the same folder it'll assume it's in the same folder (I wouldn't trust it myself though lol)

-Vanilla File: The "Vanilla" unmodded AssemblyCSharp.dll file or whatever else you wanna have

-Modded File: The modded AssemblyCSharp.dll file or whatever else you wanna have

-Minisavestates File: The AssemblyCSharp.dll fie from Yuri's Minisavestates (https://github.com/Yurihaia/MiniSavestates/releases)


Afterwards the locations will be saved in a text file so that you don't have to select them with every restart. Then you can go into the dropdown menu for select files and select the version you want to play! (It'll basically copy your selected file path and replaces it with the Game's Assembly File, **so make sure to make a copy of your currently used Assembly File if you haven't**)
