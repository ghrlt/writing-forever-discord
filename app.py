import requests
import time

token = None
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

channel_id = None
"""
Obtain like this:
	- Activate Developer Options in your parameters
	- Right click the channel you want to trigger this script
	- Click "Copy ID"
"""

if __name__ == "__main__":
	import sys

	args = sys.argv[1:]
	if args:
		if "-h" in args or "--help" in args:
			print("")
			print("WritingForever for Discord")
			print("by GaHrlt - https://github.com/ghrlt/writing-forever-discord")
			print("")
			print("Usage:")
			print("\t-h, --help\t\tDisplay this message")
			print("\t-t, --token[=<token>]\tProvide your Discord Account Token")
			print("\t-i, --id[=<channel_id>]\tProvide the channel ID to work in")
			sys.exit()

		else:
			_args = []
			for arg in args:
				_args += arg.split('=')

			args = _args

			if "-t" in args:
				token = args[args.index("-t")+1]
			elif "--token" in args:
				token = args[args.index("-t")+1]

			if "-i" in args:
				channel_id = args[args.index("-i")+1]
			elif "--channel_id" in args:
				channel_id = args[args.index("--channel_id")+1]

	if not token:
		token = input("What's your Discord account token? ")
	if not channel_id:
		channel_id = input("What's the channel id? ")


h = {
	"authorization": token,
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
}

while True:
	r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/typing", headers=h)
	if r.status_code == 200:
		time.sleep(2.5)
	else:
		print("Failed.. Retrying in 5m -", r.text)
		time.sleep(5*60)
