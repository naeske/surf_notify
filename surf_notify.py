#########################################################################################

# surf_notify
# v0.1

# A small program to tell me when a surf map I want to play is running on KZG.
# If theres a demand for this I'll actually flesh it out a bit more but not bothered right now :~)
# Created by dip

#########################################################################################

import requests
import re
from discord import Webhook, RequestsWebhookAdapter
from datetime import datetime
from time import time, sleep

x = 900

print('\nWelcome to surf_notify, made by dip')
print('Please keep this window open. Fetching server status now. \n')

# html search function
def is_map_in(map, text):
    return re.search(r"\b{}\b".format(map), text, re.IGNORECASE) is not None

# Defining some stuff
url = "https://www.gametracker.com/search/csgo/AU/?query=KZG"
urltop200 = "https://sourcequery.yepoleb.at/query?server=202.130.34.223%3A27060"

# Loading webhook url
file = open("surf_notify_webhook.txt")
webhooklink = file.read().replace("\n", " ")
file.close()

# Loading maplist
with open('surf_notify_maplist.txt') as f:
    maps = [line.rstrip() for line in f]

# Pull html from servers page and convert to text
f = requests.get(url)
ftext = f.text
f2 = requests.get(urltop200)
ftext2 = f2.text

xstr = str(x / 60)

# Search for specified maps in html text and send response
for map in maps:
    result = is_map_in(map, ftext)
    result2 = is_map_in(map, ftext2)
    if result == True or result2 == True:
        webhook = Webhook.from_url(webhooklink, adapter=RequestsWebhookAdapter())
        timestamp = datetime.today()
        strtimestamp = timestamp.strftime("%d/%m/%Y %H:%M:%S")
        webhook.send('Map of interest [' + map + '] is currently running!' + ' --- ' + strtimestamp)
        print(map + ' detected. Pushing notification to Discord. \n')
    else:
        maprunning = False

if maprunning == False:
    timestamp = datetime.today()
    strtimestamp = timestamp.strftime("%d/%m/%Y %H:%M:%S")
    print("No [more] maps of interest currently running. --- " + strtimestamp + '\n')
    print("Checking maps every " + xstr + " minutes. \n")

# Check maps every x seconds
while True:
    sleep(x - time() % x)

# Re-pull html from servers page and convert to text
    f = requests.get(url)
    ftext = f.text
    f2 = requests.get(urltop200)
    ftext2 = f2.text

    for map in maps:
        result = is_map_in(map, ftext)
        result2 = is_map_in(map, ftext2)
        if result == True or result2 == True:
            webhook = Webhook.from_url(webhooklink, adapter=RequestsWebhookAdapter())
            timestamp = datetime.today()
            strtimestamp = timestamp.strftime("%d/%m/%Y %H:%M:%S")
            webhook.send('Map of interest [' + map + '] is currently running!' + ' --- ' + strtimestamp)
            print(map + ' detected. Pushing notification to Discord.')
        else:
            maprunning = False

    if maprunning == False:
        timestamp = datetime.today()
        strtimestamp = timestamp.strftime("%d/%m/%Y %H:%M:%S")
        print("No [more] maps of interest currently running. --- " + strtimestamp + '\n')
