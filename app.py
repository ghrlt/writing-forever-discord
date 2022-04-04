import requests
import time

"""
Obtain like this:
	- Open and login into discord in your browser
	- Press F12
	- Go to "Application" tab
	- Go in Local Storage > https://discord.com
	- In the search bar type "token"
	- Press ctrl+r
	- when "token" field appear, copy its content
		/!\ Be fast, it will disappear
"""

"""
Obtain like this:
	- Activate Developer Options in your parameters
	- Right click the channel you want to trigger this script
	- Click "Copy ID"
"""

token = input("What's your Discord account token? ")
channel_id = input("What's the channel id? ")


h = {
	"authorization": token,
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
}

while True:
	r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/typing", headers=h)
	print(r, r.content)
	time.sleep(2.5)