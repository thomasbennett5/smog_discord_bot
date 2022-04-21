import os
import lightbulb
import hikari
import requests
import json

bot = lightbulb.BotApp(token=os.environ['TOKEN'], default_enabled_guilds=(546030273339588618))

@bot.listen(hikari.StartedEvent)
async def on_started(event):
  print('Bot has started!')

#Ping command now creates an embed.
@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
  embed = hikari.Embed(title="What we do in life, echoes in eternity", description="Russell Crowe")
  embed.add_field("Field name", "Field content (value)")
  embed.set_thumbnail("https://i.imgur.com/EpuEOXC.jpg")
  embed.set_footer("This is the footer")
  await ctx.respond(embed)

#/inspire command that gives you random quotes.
@bot.command
@lightbulb.command('weather','Tells you the weather in Manchester and Durham this weekend')
@lightbulb.implements(lightbulb.SlashCommand)
async def weather(ctx):
  mcr = [53.436516, -2.247194]
  durhm = [54.775696,-1.550438]
  lat = durhm[0]
  lon = durhm[1]
  #part is exclusion list without spaces: current,minutely,hourly,daily,alerts
  part = 'minutely,hourly,daily,alerts'
  API_key = os.environ['api_key']
  url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API_key}'
  data = json.loads(requests.get(url).content)
  await ctx.respond(data)

#Returns random inspirational quote from the zenquotes api
@bot.command
@lightbulb.command('inspire','Gives you some random inspiration!')
@lightbulb.implements(lightbulb.SlashCommand)
async def inspire(ctx):
  data = json.loads(requests.get('https://zenquotes.io/api/random').content)[0]
  await ctx.respond(f'{data["q"]}\n- {data["a"]}')

  
#/calendar command that tells you the SMOG calendar in beautiful embed format

#/weather command that eventually tells you the weather for the next SMOG event - protoype just tells you the weather in Durham and Manchester.





bot.run()