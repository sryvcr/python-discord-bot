## Python Discord BOT

<br>

### Discord Config
Important: You must have discord account created.  
1. Create a server in Discord.
2. Create a bot in Discord, following the instructions in: https://discordpy.readthedocs.io/en/latest/discord.html and invite you bot to server.
3. Copy the bot token and paste it in DISCORD_APP_SECRET_CLIENT variable in your *.env*.

### Run Bot
1. Clone the repository:  
   `$ git clone https://github.com/sryvcr/python-discord-bot.git`
2. Enter intro cloned repo  
   `$ cd python-discord-bot/`
3. Create a directory for virtualenv  
   `$ mkdir venv`  
   and get in there  
   `$ cd venv`
4. Create virtualenv  
   `$ virtualenv . -p python3`  
   active it  
   `$ source bin/activate`  
   and go back to root dir  
   `(venv)$ cd ../`
5. Install requirements.txt  
   `(venv)$ pip3 install -r requirements.txt`
6. Run bot  
   make sure that .env file is created in root dir and it has the DISCORD_APP_SECRET_CLIENT variable set.  
   `(venv)$ python3 src/bot.py`  
   The bot will ready when you show this message in console: PyBot is ready.
### How to use Bot in Discord
This bot contains 5 commands that you can type in discord:  
1. `>ping`  
    - `>ping`  
    returns a __pong__ response.
2. `>stats`  
    - `>stats`  
    returns a response with the discord server stats.
3. `>sum`  
    - `>sum 10 9 56`  
    returns a response with the sum between n numbers.
4. `>youtube query`
    - `>youtube python`  
    returns the 10 principal videos from youtube according to the query, in this case 10 python videos.
5. `>pokedex query`
    - `>pokedex mewtwo`  
    returns a pokedex info according to the pokemon query, in this case __Mewtwo__ info. 
    - `>pokedex 151`  
    You can find a pokedex info by the pokemon number, that returns, in this case __Mew__ info.

<br>

You can add more bot commands, show the [discord.py](https://github.com/Rapptz/discord.py) GitHub.

---