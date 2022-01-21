# Automatic IP Logger
Automatic public and local IP logging.

## What is this? ##
This is a simple python script and accompanying crappy php script to
automatically dump and record the IP's of your servers.<br>
Then when you visit the php web page it will pull all the logs from the sql file
and render them to a nice ish table for you.<br>

## Why? ##
Well there are a few reasons but most of them all resolve to dynamic IP addresses.<br>
It is very rare or very expensive to get a static public IP address from your ISP.<br>
Tracking how often your ISP changes your IP can be useful information for the servers you might be running.<br><br>
You could also use this script as a jumping off point eg.<br>
Detect and log when your public IP has changed then update a DNS record or domain name.<br>
Detect and log when your local IP has changed and restart your web server or send you a message saying something has restarted.<br>
It's up to you what you want to do with it, How it works right now serves my needs fine though.<br>

## How? ##
Python will use request to `requests.get('https://myip.wtf/json')`<br>
Then python json to pass that data<br>
Then we use sqlite3 to make a new database file if we don't have one (a db file will be automatically made if one is not found aswell)<br>
we also need to grab oue local ip so that is done with socket in the `getLocalIP()` function<br>
On first run `main()` function will run, setup a new scheduler, set the schedule time to 60 mins<br>
Then drop into a while loop<br>
The loop will check if the schedule is ready to be ran, if not it will wait 1 second and check again.<br>
The console will output a little . heartbeat to let you know the script is still running.<br>

## How do I set it up / run it? ##
The python script was made with Python 3.8.10 So you will need to have python 3.8 or higher installed first.<br>
If you choose to use the php web page your web server will need to be running php and have access to the folder
to read the db file.<br>(Testing was done with php 7.4 and apache 2.4)<br>
Your php web server may also need to have the sqlite3 module installed and running aswell.<br><br>
List of stupid librarys the python scrip uses are<br>
`OS`<br>
`time`<br>
`json`<br>
`sqlite3`<br>
`datetime`<br>
`pip install requests`<br>
`pip install schedule`<br>
`pip install socket`<br><br>

**To run this script:**<br>
And if you are using the php page.<br>
make a new folder in your servers `www` or `htdocs` folder called something like `IPDump`<br>
Then just download and unpack this github project into your new folder<br>
Then run `python IPDump.py` or if for some reason you still have python 2 installed `python3 IPDump.py`<br>
The python script will run, make a new db, dump our IPs, then chill out for an hour. Rinse'n'repeat in an hour.<br>
If you want to change how long or short you want the schedule to run, you can find the timer at the bottom of the script line 77 ish `schedule.every(60).minutes.do(main)` change it to something like `schedule.every(1).minutes.do(main)` and you will now dump your IPs every minute or every hour.<br>
I might make this a user editable value at the top of the script but really how often do you need to change it?<br>
one minute or one hour should be fine, and if your just checking on things no need to hit that nice server really hard for no good reason.<br>
Then just goto your web server eg. `http:\\myserver.why\IPDump` and you should see a nice table of the IPs the script as logged so far.<br>
If your not using the php page then thats fine too, you can just unpack this github project anywhere and run it.<br>
The script and db files are independent of the php file and web server.<br>

## !DISCLAIMER! ##
I AM NOT RESPONSIBLE FOR YOUR CRAPPY SETUPS!<br>
DO NOT put that web page on the open internet, it's intended for local networks or vpns only.<br>
Or allow another computer other then localhost to be allow to touch that py script.<br>
If you pwn yourself by uploading all your data to the open internet, that's on you buddy.

## Extra ##
I am logging the tor exit node info that myip.wtf spits out however the php page does not render that info.<br>
It is simple enough to edit the php to add it however that info was not relevant for my setup so it was always false for me.<br>
