import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("Bot is ready!")


@client.command(aliases=["Clear", "clears", "Clears"])
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command()
async def text(ctx):
    await ctx.send("Hi Ricks!")


@client.command()
async def info(ctx):
    await ctx.send("1. clear\n2. text")


@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)


client.run("ODAxMTIwMzg0NzYxMjAwNjkx.YAcDfw.9OqGLb79BV8JaJF9wYX01f8KEXA")
