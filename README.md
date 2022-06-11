# discord-dms-opener

A simple tool to open all your discord DMs using your discord data folder(you will have to request your data from discord itself)  
This tool is extremely helpful when mass purging your discord messages

### Disclaimer
Any sort of automation violates [Discord's TOS](https://support.discord.com/hc/en-us/articles/115002192352-Automated-user-accounts-self-bots) and can result in account termination.  
Use it at your own risk.

## Usage 

#### Clone this project 
```bash
git clone https://github.com/Empyreann/discord-dms-opener
cd discord-dms-opener
```
#### Install Dependencies
```bash
pip install -r requirements.txt
```
#### Configure `config.json`
```json
{
        "USER_ID": " your user ID here ",
        "USER_TOKEN": " your discord token here ",
        "FOLDER_PATH": "your discord data message folder"
}
```
#### [OPTIONAL] Ignore users by adding their ids in `ignored_channels.json`
```json
{
        "IGNORED_CHANNELS": []
}
```
#### Run `main.py`
*You will need Python 3+ to use this*
```bash
python main.py
```

## Mass deletion 
If you're using this tool for mass purging messages, It is recommended to first use this tool and open all your DMs and then use a tool like [discord-delete](https://github.com/adversarialtools/discord-delete) to purge all your discord messages from DMs and servers.
