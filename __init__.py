import discord
import random
from commandModules import listlist
from commandModules import calculator
from commandModules import googleSearch
from commandModules import jumbler
from commandModules import fishbowl
from discord.ext import commands

bot = commands.Bot(command_prefix = listlist.cmdPrefix)         #An instance of the bot called bot

#Runs when the bot is online.
@bot.event                                       
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(random.choice(listlist.startActivity)))
    print(random.choice(listlist.wokeUp))



# -------------------------COMMANDS-------------------------

#Ping
@bot.command()
async def ping(ctx):
    """Returns the latency in milliseconds between the bot and the server."""
    await ctx.send(f"Pong \({round(bot.latency * 1000)}ms\)")
    
@bot.command()
async def yesno(ctx, *, question):
    """Randomly responds yes, no, or maybe."""
    response = f"{question}\nAnswer: {random.choice(listlist.yesnoReplies)}"
    await ctx.send(f"Question: {response}")
    print(f"Yes or No: {response}")

@bot.command(aliases=["69"])
async def sixtyNine(ctx):
    """Who doesn't say "Nice" when they hear "69", huh?"""
    await ctx.send("Nice.")
    print("69. Nice.")
    
@bot.command()
async def clear(ctx, amount=3, silent=False):
    """Clears a specified number of messages. 3 by default."""
    await ctx.channel.purge(limit=amount)
    if silent == False:
        await ctx.send(f"Deleted {amount} messages.")
    print(f"Deleted {amount} messages.")

@bot.command(aliases = ["calcu", "compute", "math", "calculator"])
async def calculate(ctx, *, equation):
    """A basic string to primitive data-type calculator."""
    try:
        await ctx.send(f"{calculator.doMath(equation,True)}")
        print(f"Calculating: {calculator.doMath(equation,False)}")
    except IndexError as e:
        await ctx.send(listlist.indexErrorMsg)
        print(f"Errorwith: \"{equation}\".\nError message:\"{e}\"")
    except Exception as e:
        await ctx.send(f"{random.choice(listlist.errorPrefixInsult)} `{equation}`.\nError message:`{e}`")
        print(f"Errorwith: \"{equation}\".\nError message:\"{e}\"")

@bot.command(aliases = ["c"])
async def cal(ctx, *, equation):
    """Also a basic string to primitive data-type calculator.
    This one doesn't return a stupid suffix."""
    try:
        await ctx.send(f"{calculator.doMath(equation,False)}")
        print(f"Calculating: {calculator.doMath(equation,False)}")
    except IndexError as e:
        await ctx.send(listlist.indexErrorMsg)
        print(f"Errorwith: \"{equation}\".\nError message:\"{e}\"")
    except Exception as e:
        await ctx.send(f"Errorwith: `{equation}`.\nError message:`{e}`")
        print(f"Errorwith: \"{equation}\".\nError message:\"{e}\"")
        
@bot.command(aliases = ["google", "search", "find"])
async def googleSrch(ctx, *,userQuery="DefinitelyRus"):
    """Returns 8 links relating to the search query."""
    try:
        await ctx.send(googleSearch.srch(userQuery))
        print(f"Showing search results for: \"{userQuery}\".")
    except Exception as e:
        await ctx.send(f"Your search `{userQuery}` caused an error:\n`{e}`")
        print(f"Search \"{userQuery}\" caused an error:\n\"{e}\"")
        
@bot.command(aliases = ["echo", "print"])
async def say(ctx, *, words = "You're gay."):
    """Forces the bot to say words and deletes evidence."""
    await ctx.channel.purge(limit=1)
    await ctx.send(words)
    print(f"Echoing: \"{words}\"")
    

#-------------------------Work in progress-------------------------

@bot.command(aliases=["wrods", "wodrs", "wdros", "wdors"])
async def jumble(ctx, *, words):
    """Jumbles words. Still potentially readable."""
    words = jumbler.jumble(words)
    await ctx.send(words)


#-------------------------Start-------------------------

try:
    print(f"{random.choice(listlist.wakeupcall)} {listlist.botname}...")
    token = open("F:\Personal Files\Project Files\Programming Projects\Git Repositories\Discord Bot\\tokens.txt", "r")
    bot.run(token.readline())
    token.close()
    
#     The token had to be externally stored for security purposes.
#     Discord API uses a token to give bots instructions.
#     We had to hide the token because if others get a hold of it,
#     they could run their own code and grief servers hosting the bots.
#     
#     Other users may simply replace token.readline() with their own bot's
#     token. This also means they'll have to remove the open() and close() functions.

except Exception as e:
    print(f"Exception Caught: {e}")
    while True:
        pass