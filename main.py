from discord.ext import commands
from datetime import datetime
import discord
import os
import html

TOKEN = os.environ.get('TOKEN')
channel_handles = {}
client = commands.Bot(command_prefix = "==")
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="dlog.hitsounds.moe"))
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
				os.mkdir("logs")
			except:
				pass
			try:
				os.mkdir(f"logs/{ctx.server.id}")
			except:
				pass
			channel_handles[ctx.channel.id] = open(os.path.join("logs",ctx.server.id,f"{ctx.channel.id}.html"), "a")
			channel_handles[ctx.channel.id].write(r"<head><style>table, th, td {border: 1px solid black;border-collapse: collapse;}; </style></head><body><table style=\"width:100%\"><thead><tr><th>Time</th><th>UserID</th><th>Message</th></tr></thead><tbody>")
	channel_handles[ctx.channel.id].write(f"<tr><td>{datetime.now()}</td><td>{ctx.author.id}</td><td>{html.escape(ctx.content)}</td></tr>")
	channel_handles[ctx.channel.id].flush()
	await client.process_commands(ctx)


@client.command(pass_context=True)
async def me(ctx):
    await client.say("HI, I keep logs so you don't have to!")

@client.command
async def code():
		await client.say("Deployed: https://repl.it/@Hitsounds/replit-bot, Github: https://github.com/Hitsounds/repl.it-bot")

@client.command(pass_context=True)
async def help(ctx):
    await client.send_message(ctx.message.author, "==me")

@client.command(pass_context=True)
async def log(ctx):
	await client.say(f"http://dlog.hitsounds.moe/{ctx.server.id}/{ctx.channel.id}.txt")


client.run(TOKEN)
