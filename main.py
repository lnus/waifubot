import discord
import asyncio
import re
from hentai import get_hentai 
import ascii_art
from key import key # Imports the key from a separate file

client = discord.Client()

class Music:
    def __init__(self, author):
        self.url = None
        self.author = author 
        self.playlist = []
        self.player = None

    def add_song(self, url):
        self.playlist.append(url)

@client.event
async def on_ready():
    print("Logged in as: {}".format(client.user.name))
    print("With ID: {}".format(client.user.id))
    print("-"*(len(client.user.id)+5))
    await client.change_presence(game=discord.Game(name="Overwatch"))

@client.event
async def on_message(message):
    global j

    if message.author == client.user:
        return

    # Test command
    if message.content.startswith("--hello"):
        await client.send_message(message.channel, "Hello {0.author.mention} senpai~!".format(message))
    
    # Hentai command
    if message.content.startswith("--nsfw"):
        tags = message.content.replace("--nsfw", "")
        await client.send_message(message.channel, "{0.author.mention} here's your hentai, senpai~\n{url}".format(message, tags=tags, url=get_hentai(tags)))

    # Music commands    
    if message.content.startswith("--voice"):
        command = message.content.replace("--voice ", "")
        if command.startswith("add"):
            url = command.replace("add ", "")
            j.add_song(url)
        if command.startswith("join"):
            await client.join_voice_channel(message.author.voice_channel)
            j = Music(message.author)
        if command.startswith("leave"):
            voice = client.voice_client_in(message.author.server)
            if voice: await voice.disconnect()
        if command.startswith("play"):
            voice = client.voice_client_in(message.author.server)
            j.playlist.pop(0)
            j.player = await voice.create_ytdl_player(j.playlist[0])
            j.player.start()
        if command.startswith("stop"):
            j.player.stop()
        if command.startswith("skip"):
            if not d.player.is_done():
                d.player.stop()
                j.playlist.pop(0)
                j.player = await voice.create_ytdl_player(j.playlist[0])
                j.player.start()
    
    # Ascii commands
    if message.content.startswith("--ascii"):
        image = message.content.replace("--ascii ", "")
        try:
            await client.send_message(message.channel, ascii_art.art[image])
        except KeyError:
            await client.send_message(message.channel, "No ascii found for: {}".format(image))

client.run(key)    
