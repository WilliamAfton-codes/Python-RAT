# Python-RAT
Remote Administration Tool written in Python for local computer management

Made for library testing (Testing shutil, socket and pyuac)

# Usage
1) Download `Python-RAT-x.x.zip` from [releases](https://github.com/WilliamAfton-codes/Python-RAT/releases)

2) Install pyuac library in command prompt: 
```
pip install pyuac
```

3) Run `admin_server.py` on administrator device, and client_pc.py on device ou would like to administrate

# Features
> Download command, downloads a file from current directory of client_pc.py onto admin's device
```
Command: download file.txt
```

> CD command functionality, to change directory (use dir to look inside whatever directory you're in)
```
Command: cd folder
Changed directory: cd folder
```

> MKDIR command, to create directory with specified name on the client's PC
```
Command: mkdir folder
Directory made: mkdir folder
```

> DELDIR command, to delete a folder and all files and subfolders within the client's PC
```
Command: deldir folder
Directory deleted: deldir folder
```

# Notes
Thanks for using Python-RAT, please star my page on GitHub; It really helps out!
