from keep_alive import keep_alive
from discord.ext import commands
from datetime import datetime
import discord
import os

TOKEN = os.environ.get('TOKEN')

channel_handles = {}
client = commands.Bot(command_prefix = "\\")
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="\help"))
    print ("Bot is ready")
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(ctx):
	if ctx.channel.id not in channel_handles.keys():
		if os.path.isfile(os.path.join("logs",ctx.server.id, f"{ctx.channel.id}.txt")):
			channel_handles[ctx.channel.id] = open(os.path.join("logs",ctx.server.id, f"{ctx.channel.id}.txt"), "a")
		else:
			try:
				os.mkdir(f"logs/{ctx.server.id}")
			except:
				pass
			channel_handles[ctx.channel.id] = open(os.path.join("logs",ctx.server.id,f"{ctx.channel.id}.txt"), "a")
			channel_handles[ctx.channel.id].write("Time | UserID | Message_Content")
	channel_handles[ctx.channel.id].write(f"\n{datetime.now()} | {ctx.author.id} | {ctx.content}")
	channel_handles[ctx.channel.id].flush()


@client.command(pass_context=True)
async def me(ctx):
    await client.say("HI, I keep logs so you don't have to!")

@client.command(pass_context=True)
async def help(ctx):
    await client.send_message(ctx.message.author, "\\me")

@client.command(pass_context=True)
async def log(ctx):
	await client.say(f"https://UrbanAwareStatistics--hitsounds.repl.co/{ctx.server.id}/{ctx.channel.id}.txt")


keep_alive()
client.run(TOKEN)
