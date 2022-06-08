# Writing Forever, discord edition

This program will let you being displayed as typing on Discord, for ever!


## How?
The script will mimic a normal user interaction api call.

## How the app can do api call on my behalf?
You'll have to provide your Discord account token to it<br>
Here's how:

1. Open and login into discord, preferably in your browser
2. Open DevTools (Press F12 or Ctrl+Maj+i)
3. Go to "Application" tab
4. Go in Local Storage > https://discord.com
5. In the search bar type "token"
6. Refresh page (Press ctrl+r)
7. When "token" field appear, copy its content


## Installation

```cmd
git clone https://github.com/ghrlt/writing-forever-discord
```

## Usage

```cmd
python3 app.py --token mfa.WpyE...aLzH5 --channel_id 983502343087722546
```
