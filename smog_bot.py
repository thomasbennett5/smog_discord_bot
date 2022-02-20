import os
import discord
token = "OTQ0MjUyODQzOTQ1MjMwMzU2.Yg-5_Q.Ou702cBsrzfjh1W3mQWmufzZ6o0"

client = discord.Client()

@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("$hello"):
    await message.channel.send("Hello!")
    
  if message.content.startswith("$inspire"):
    await message.channel.send(' "You are a worthless piece of SHIT - Sun Tzu" ')
  if message.attachments:
    await message.channel.send("You have sent a picture")
    
    
  if ''.join(message.content.split()).lower() == "getoffme":
    await message.channel.send("SON!")


client.run(token)
