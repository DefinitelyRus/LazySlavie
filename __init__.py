import discord
import random
from commandModules import listlist
from commandModules import calculator
from commandModules import googleSearch
from discord.ext import commands

bot = commands.Bot(command_prefix = listlist.cmdPrefix)         #An instance of the bot called bot

def randomStart():
    return random.choice(listlist.startActivity)

@bot.event                                       
async def on_ready():                           #Runs the following code when the bot has fully loaded.
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(randomStart()))
    print(random.choice(listlist.wokeUp))

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong \({round(bot.latency * 1000)}ms\)")
    
@bot.command()
async def yesno(ctx, *, question):
    response = f"{question}\nAnswer: {random.choice(listlist.yesnoReplies)}"
    await ctx.send(f"Question: {response}")
    print(f"Yes or No: {response}")

@bot.command(aliases=["69"])
async def sixtyNine(ctx):
    await ctx.send("Nice.")
    print("69. Nice.")
    
@bot.command()
async def clear(ctx, amount=3, silent=False):
    await ctx.channel.purge(limit=amount)
    if silent == False:
        await ctx.send(f"Deleted {amount} messages.")
    print(f"Deleted {amount} messages.")

@bot.command(aliases = ["calcu", "compute", "math", "calculator"])
async def calculate(ctx, *, equation):
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
    try:
        await ctx.send(googleSearch.srch(userQuery))
        print(f"Showing search results for: \"{userQuery}\".")
    except Exception as e:
        await ctx.send(f"Your search `{userQuery}` caused an error:\n`{e}`")
        print(f"Search \"{userQuery}\" caused an error:\n\"{e}\"")
        
@bot.command(aliases = ["echo", "print"])
async def say(ctx, *, words = "You're gay."):
    await ctx.channel.purge(limit=1)
    await ctx.send(words)
    print(f"Echoing: \"{words}\"")
    
"""
These commands work, but they need further work to be more optimized.

@bot.command(aliases=["spinthewheel", "roulette", "raffle", "fishbowl"])
async def add(ctx, *, item):
    global itemList
    itemList.append(item)
    await ctx.send(f"Added {item} to the list.")
    
@bot.command()
async def uchoose(ctx):
    global itemList
    if itemList == []:
        await ctx.send("The list is empty. Type `slv add [item]` to add items to the list.")
    else:
        await ctx.send(f"I choose **{str(random.choice(itemList))}**.")
    itemList = []

@bot.command()
async def ichoose(ctx, member, *, choice):
    global itemList
    if choice in itemList:
        await ctx.send(f"{member} chose **{str(choice)}**.")
        itemList = []
    elif itemList == []:
        await ctx.send("The list is empty. Type `slv add [item]` to add items to the list.")
    else:
        await ctx.send("This item is not in the list. (Case sensitive)")

@bot.command()
async def upick(ctx):
    global itemList
    choice = random.choice(itemList)
    if itemList == []:
        await ctx.send("The list is empty. Type `slv add [item]` to add items to the list.")
    else:
        await ctx.send(f"I pick **{str(random.choice(itemList))}** from the list.")
    itemList.remove(choice)

@bot.command()
async def ipick(ctx, member, *, choice):
    global itemList
    if choice in itemList:
        await ctx.send(f"{member} picked **{str(choice)}** from the list.")
        itemList.remove(choice)
    elif itemList == []:
        await ctx.send("The list is empty. Type `slv add [item]` to add items to the list.")
    else:
        await ctx.send("This item is not in the list. (Case sensitive)")

@bot.command()
async def choicelist(ctx):
    global itemList
    list_in_string = ""
    for i in itemList:
        list_in_string += ("- " + str(i) + " \n")
    if list_in_string == "":
        await ctx.send("The list is empty. Type `slv add [item]` to add items to the list.")
    else:
        await ctx.send(f"Choice list:\n{list_in_string}")
"""


"""
#Work in progress
@bot.command(aliases=["wrods", "wodrs", "wdros", "wdors"])
async def jumble(ctx, *, words):
    toJumble = []
    jumbleStc = str()
    jumbleWord = str()
    holdWord = str()
    
    for c in words:
        if c != " ":
            holdWord += str(c)
        elif c == " ":
            toJumble.append(holdWord)
            holdWord = str()
        print("holdWord: " + str(holdWord))
        print("toJumble: " + str(toJumble))
    
    for w in toJumble:
        for c in w:
"""
#Other prerequisites
print(f"{random.choice(listlist.wakeupcall)} {listlist.botname}...")

#Final
try:
    token = open("F:\Personal Files\Project Files\Programming Projects\Git Repositories\Discord Bot\\tokens.txt", "r")
    bot.run(token.readline())
    token.close()
except Exception as e:
    print(f"Exception Caught: {e}")
    while True:
        pass