surf_notify v0.1

A small program to tell me when a surf map I want to play is running on KZG.
If theres a demand for this I'll actually flesh it out a bit more (GUI, packed .exe) but not bothered right now :~)

Created by dip


REQUIREMENTS:
  - Python 3.x (Download from https://www.python.org/downloads/)
      - Make sure to add python to your PATH during install (checkbox)
  - Python library's (Execute these commands in powershell): 
      - python -m pip install requests 
      - py -3 -m pip install -U discord.py
 
INSTALLATION INSTRUCTIONS:
 
1. Download and unzip folder.
2. Specify maps you want to track by editing surf_notify_maplist.txt. Instructions in file.
3. Specify Discord webhook URL by editing surf_notify_webhook.txt. Instructions in file.
    - Webhook create guide here: https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks
4. Navigate to surf_notify folder in powershell and execute surf_notify.py  --->  cd 'path_of_folder' followed by python .\surf_notify.py

NOTE: By default script checks maps once when opening then every 15 minutes after. To change this you can open surf_notify.py in an editor and change the value of x on line 61. Number taken is in seconds.


![running in shell](https://i.imgur.com/MTtwGIL.png)

![discord push](https://i.imgur.com/ZdB406o.png)

Any queries reach me:

Gumo#7171 (Discord)

