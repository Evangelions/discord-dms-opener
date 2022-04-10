
import json
import os
import discord

print("Starting")

with open("config.json", "r") as f:
    config_file = json.load(f)
with open("ignored_channels.json", "r") as f:
    ignored_channels_file = json.load(f)
ignored_channels_list = ignored_channels_file["IGNORED_CHANNELS"]
TOKEN_AUTH = config_file["USER_TOKEN"]
USER_ID = config_file["USER_ID"]
FOLDER_PATH = config_file["FOLDER_PATH"]
user_list = []


for root, dirs, files in os.walk(FOLDER_PATH):
    for main_file in files:
        if main_file.startswith("channel.json"):
            with open(os.path.join(root, main_file), "r") as f:
                main_data = json.load(f)
            if main_data["type"] == 1:
                target_user = main_data["recipients"]
                target_user.remove(f"{USER_ID}")
                user_list.append(target_user[0])

client = discord.Client()


@client.event
async def on_ready():
    for user in user_list:
        if int(user) in ignored_channels_list:
            print(f"Ignoring user {user} ")
            return
        fetched_user = await client.fetch_user(user)
        await fetched_user.create_dm()
        print(f'Created DMS with {user}')
        ignored_channels_list.append(user)
        with open("ignored_channels.json", "w") as f:
            json.dump(ignored_channels_file, f)
        print(f'Added {user} to ignore list')


client.run(
    f"{TOKEN_AUTH}",
    bot=False)
