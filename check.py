import json
import urllib.request
import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("Bot is ready!")


head = {'API-Key': 'R6FJRZWX2BKM5RYMESF4G7HHKTYC3G5JE4VA'}
req = urllib.request.Request(
    "https://api.vultr.com/v1/account/info", headers=head)

with urllib.request.urlopen(req) as url:
    data = json.loads(url.read().decode())
    print(data)
    balance = float(data['balance'])
    pending_charges = float(data['pending_charges'])
    print(balance)
    print(pending_charges)

    positive = 0 - balance


@client.command()
async def status(ctx):
    if positive < 14:
        await ctx.send("@NR We need funds current balance is ${}".format(str(positive)))
    else:
        await ctx.send("Funds are at a healthy level: ${}".format(str(positive)))


@client.command()
async def test(ctx):
    await ctx.send("Hi!")


@client.command()
async def donate(ctx):
    await ctx.send("https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=captainjin95%40gmail.com&item_name=Funding+the+NR+Servers&currency_code=USD")


@client.command()
async def info(ctx):
    await ctx.send("The commands are:\n1. status\n2. donate")

client.run("NzkwNjIzNzUxNTkwNjQxNzE0.X-DTvw.zZJP3hvhFvU9KQNOlN_l1jetKUQ")
