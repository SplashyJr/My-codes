import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("Bot is ready!")


@client.command(aliases=["Quote", "quotes", "Quotes"])
async def quote(ctx):
    possible = ["Help me, Obi-Wan Kenobi. You’re my only hope.", "I find your lack of faith disturbing.", "It's over Anakin. I have the high ground!",
                "It’s the ship that made the Kessel run in less than twelve parsecs. I’ve outrun Imperial starships. Not the local bulk cruisers, mind you. I’m talking about the big Corellian ships, now. She’s fast enough for you, old man.",
                "The Force will be with you. Always.", "Why, you stuck-up, half-witted, scruffy-looking nerf herder!", "Never tell me the odds!", "I’ll never turn to the dark side. You’ve failed, your highness. I am a Jedi, like my father before me.",
                "You can’t stop the change, any more than you can stop the suns from setting.", "Fear is the path to the dark side. Fear leads to anger; anger leads to hate; hate leads to suffering. I sense much fear in you.",
                "Hello there.", "The dark side of the Force is a pathway to many abilities some consider to be unnatural.", "Power! Unlimited power!", "You were my brother, Anakin. I loved you.", "To die for one’s people is a great sacrifice. To live for one’s people, an even greater sacrifice. I choose to live for my people.",
                "You are the Chosen One. You have brought balance to this world. Stay on this path, and you will do it again for the galaxy. But beware your heart.", "Remember, my dear Obi-Wan. I’ve loved you always. I always will.", "The Sith killed each other, victims of their own greed. But from the ashes of their destruction, I was the last survivor. I chose to pass my knowledge on to only one. I created a legacy so resilient that now you come before me.",
                "Always two there are — a master and an apprentice.", "The Sith took everything from me. Ripped me from my mother’s arms, murdered my brother, used me as a weapon, and then cast me aside. Abandoned me. Once, I had power — now I have nothing.", "I am no Jedi.", "If you define yourself by your power to take life, your desire to dominate, to possess, then you have nothing.", "I should have known the jedi were plotting to take over.", "Anakin Chancellor Palpatine is evil!", "From my point of view the jedi are evil!", "Well then you are lost!"]

    await ctx.send(random.choice(possible))


@client.command()
async def info(ctx):
    await ctx.send("The commands are info, pizza, office")


@client.command()
async def count(ctx):

    while True:
        computer = random.randint(1, 10)
        await ctx.send('Guess my number')

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and int(msg.content) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        msg = await client.wait_for("message", check=check)

        if int(msg.content) == computer:
            await ctx.send("Correct")
        else:
            await ctx.send(f"Nope it was {computer}")


@client.command()
async def fact(ctx):
    await ctx.send("I can't think of any facts lol! :)")


@client.command()
async def pizza(ctx):
    await ctx.send("https://tenor.com/view/spider-man-pizza-time-pizza-day-pizza-dinner-gif-16271126")


@client.command(aliases=["Clear", "clears", "Clears"])
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command()
async def text(ctx):
    await ctx.send("Hi!")


@client.command()
async def burn(ctx):
    await ctx.send("https://media.tenor.co/videos/0e59454e0ae9bdab1b0c13938840412e/mp4")


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member.mention}")


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return


@client.command()
async def office(ctx):
    await ctx.send("https://tenor.com/view/the-office-steve-carell-michael-scott-why-are-you-the-way-you-are-pissed-gif-5226128")

client.run("Hi")
