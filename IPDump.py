#!/env/Python3.8.10
#!MobCat 2022
# Automaticly dumps your public ip once a minuet
# Saves it to an sqlite database.

import requests # Request data from the internet
import json     # Procuess said data
from datetime import datetime # Get current date and time
import sqlite3  # Our sql database
import os		# read os file system
import schedule # Repeat our scrupt everey 1 mins.
import time
import socket	# Get our local ip

print("IP Auto Dumper 20220121")

def getLocalIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def main():
	# Making a get request, dump json
	#TODO: check if responce is 200 then contune
	#if 404 retry in a min
	print("\nRequesting our IP...")
	response = requests.get('https://myip.wtf/json')
	jsonData = response.json()
	print("Done.")
	
	# Setup our sql database
	# Check if its even a thing first
	print("Loading data.db...")
	if os.path.isfile(f'data.db') == False:
		print("No database found! Making a new one...")
		dbconn = sqlite3.connect('data.db')
		dbcurs = dbconn.cursor()
		dbcurs.execute("CREATE TABLE IPLog (Date text, Local_IP, Public_IP text, Location text, Hostname text, ISP text, Tor text, Country text)")
		dbconn.commit()
	else:
		dbconn = sqlite3.connect('data.db')
		dbcurs = dbconn.cursor()
		print("Done.")
	
	# procuess json data
	#print(jsonData)
	print("Saveing IP to data.db...")
	# Set data to veribals
	todate	    = datetime.now()
	LocalIPstr	= getLocalIP()
	IPstr 		= jsonData["YourFuckingIPAddress"]
	Locationstr = jsonData["YourFuckingLocation"]
	Hostnamestr = jsonData["YourFuckingHostname"]
	ISPstr 		= jsonData["YourFuckingISP"]
	Torstr 		= jsonData["YourFuckingTorExit"]
	Contrystr 	= jsonData["YourFuckingCountryCode"]
	# send and save varibles to database
	dbcurs.execute(f"INSERT INTO IPLog VALUES ('{todate}', '{LocalIPstr}', '{IPstr}', '{Locationstr}', '{Hostnamestr}', '{ISPstr}', '{Torstr}', '{Contrystr}')")
	dbconn.commit()
	# Close DB
	dbcurs.close()
	print("Done.\nSleeping for 1 hour...")

#!START HERE!#
#run main once, then setup the scgeduler and wait
main()
	
# Setup schedual
schedule.every(60).minutes.do(main)

# Run schedual forever
while True:
	schedule.run_pending()
	print(".", end="", flush=True)
	time.sleep(1) # seconds


