'''
Created on 13 Mar 2021

@author: Rus

This is a python module for all commands involving fishbowl.

Fishbowl is a list of items added by members.
They can add and remove items from the fishbowl as they wish.
The bot can randomly choose from the list and either remove a
single item or empty the list upon choosing.

A list locker is planned where individual members can have a list of their own.
'''

print("Preparing Fishbowl Module [ALPHA]...")

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