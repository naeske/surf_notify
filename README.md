surf_notify v0.1

A small program to tell me when a surf map I want to play is running on KZG. Notifications sent to your Discord server.

If theres a demand for this I'll actually flesh it out a bit more (GUI, packed .exe) but not bothered right now :~)

Created by dip


REQUIREMENTS:
  - Python 3.x (Download from https://www.python.org/downloads/)
      - Make sure to add python to your PATH during install (checkbox)
  - Python modules (Execute these commands in powershell): 
      - python -m pip install requests 
      - py -3 -m pip install -U discord.py
 
INSTALLATION INSTRUCTIONS:
 
1. Download repo as zip and unzip folder.
2. Specify maps you want to track by editing surf_notify_maplist.txt. Instructions in file.
3. Specify Discord webhook URL by editing surf_notify_webhook.txt. Instructions in file.
    - Webhook create guide here: https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks
4. Navigate to surf_notify folder in powershell and execute surf_notify.py
    - cd 'path_to_folder'
    - python .\surf_notify.py

NOTE: By default script checks maps once when opening then every 15 minutes after. To change this you can open surf_notify.py in an editor and change the value of variable x on line 18. Number taken is in seconds.


![running in shell](https://i.imgur.com/ec8TE4o.png)

![discord push](https://i.imgur.com/As3z57e.png)

Any queries reach me at:

Gumo#7171 (Discord)
