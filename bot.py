import discord
import random
from discord.ext import commands

emoji_list = ["\U0001F600", "\U0001F606", "\U0001F607", "\U0001F61A", "\U0001F975","\U0001F976","\U0001F97A","\U0001F62B","\U0001F621","\U0001F47B", 
            "\U0001F916","\U0001F47A","\U00002764","\U0001F9E1","\U0001F49B","\U0001F49A","\U0001F499","\U0001F49C","\U0001F4AF","\U0001F4A6","\U0001F4A4",
            "\U0001F44D", "\U0001F44E", "\U0001F440", "\U0001F52A", "\U00002705", "\U0000274C"]


trackimages = {"mks" : "mks.jpg", "wp" : "wp.jpg", "ssc" : "ssc.jpg", "tr" : "tr.jpg",
                "mc" : "mc.jpg", "th" : "th.jpg", "tm" : "tm.jpg", "sgf" : "sgf.jpg",
                "sa" : "sa.jpg", "ds" : "ds.jpg", "ed" : "ed.jpg", "mw" : "mw.jpg",
                "cc" : "cc.jpg", "bdd" : "bdd.jpg", "bc" : "bc.jpg", "rr" : "rr.jpg",
                "rmmm" : "rmmm.jpg", "rmc" : "rmc.jpg", "rccb" : "rbbc.jpg", "rtt" : "rtt.jpg",
                "rddd" : "rddd.jpg", "rdp3" : "rdp3.jpg", "rrr" : "rrr.jpg", "rdkj" : "rdkj.jpg",
                "rws" : "rws.jpg", "rsl" : "rsl.jpg", "rmp" : "rmp.jpg", "ryv" : "ryv.jpg",
                "rttc" : "rttc.jpg", "rpps" : "rpps.jpg", "rgv" :"rgv.jpg", "rrrd" : "rrrd.jpg",
                "dyc" : "dyc.jpg", "dea": "dea.jpg", "ddd" : "ddd.jpg", "dmc" : "dmc.jpg",
                "dwgm" : "dwgm.jpg", "drr" : "drr.jpg", "diio" : "diio.jpg", "dhc" : "dhc.jpg",
                "dcl" : "dcl.jpg", "dww" : "dww.jpg", "dac" : "dac.jpg",
                "dnbc" : "dnbc.jpg", "drrd" : "drrd.jpg", "dsbs" : "dsbs.jpg", "dbb" : "dbb.jpg"}

client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
    print("Bot is Ready.")

@client.command()
async def test(ctx):
    await ctx.send("Message sent successfully.")

@client.command(aliases = ["flipcoin", "FLIPCOIN", "flip", "fc", "FLIP", "FC"])
async def _flipcoin(ctx):
    coin = random.randrange(1,3)
    print(coin)
    if coin == 1:
        await ctx.send("Heads!")
    else:
        await ctx.send("Tails!")

@client.command(aliases = ["baggingimage", "bag", "BAGGINGIMAGE", "BAG"])
async def _baggingimage(ctx, *, track):
    track = track.lower()

    try:
        image = trackimages[track]
        print(image)
        await ctx.send(file = discord.File("images\\" + image))
    except:
        if track == "help":
            embed = discord.Embed(
            title = "Bagging Images Help",
            description = "These images show how far behind the player in first one must be at each item set in order to be able to obtain a star or shock. \nThe colour of the item corresponds to the coloured boxes, and are the minimum distance from first required to obtain these items.\nIn this example, on the second set of Mario Kart Stadium, a player can obtain a star when first has completed the turn after the box set, and shock when first has partially completed the u-turn before the glider.\n\nNOTE: In order to obtain shock a player must be in ninth or below.",
            colour = discord.Colour.blue()
        )

            embed.set_image(url="https://media.discordapp.net/attachments/484439154529271829/846780724710342696/example.png")
            await ctx.send(embed=embed)
           
        elif track == "dbp":
            await ctx.send("Bagging image does not exist for GCN Baby Park.")
        else:
            await ctx.send("Track does not exist. Check track name has been inputted correctly.")

@commands.has_permissions(administrator=True)
@client.command(aliases = ['gather', 'GATHER', 'Gather'])
async def _gather(ctx, startingTime, endingTime, timeZone):

    #input validation for the args
    validTimeZones = ["EST","GMT","CST","CET", "CEST", "CEST", "GMT+0","GMT+1", "GMT+2", "GMT+3","GMT+4","GMT+5","GMT+6","GMT+7","GMT+8","GMT+9","GMT+10","GMT+11","GMT-1","GMT-2","GMT-3","GMT-4","GMT-5","GMT-6","GMT-7","GMT-8","GMT-9","GMT-10","GMT-11"]
    try:                
        intStartingTime = int(startingTime)
    except:
        await ctx.send("Error, starting time must be an integer.")
        return

    if intStartingTime < 0 or intStartingTime > 24:
        await ctx.semd("Error, starting time must be between 0 and 24.")
    
    try:
        intEndingTime = int(endingTime)
    except:
        await ctx.send("Error, ending time must be an integer.")
        return
    if intEndingTime < 0 or intStartingTime > 24:
        await ctx.send("Error, ending time must be between 0 and 24.")
        return

    intStartingTime = int(startingTime)
    intEndingTime = int(endingTime)

    updatedTime = timeZone.upper()

    if updatedTime not in validTimeZones:
        await ctx.send("Error, time must be a valid time zone, try .timeZones for a list of valid time zones.")
        return
    

    #Test and impliment the amount of time lines the bot should print.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    if intStartingTime == intEndingTime:
        hourDifference = 1
    elif intStartingTime < intEndingTime:
        hourDifference = intEndingTime - intStartingTime
    elif intStartingTime > intEndingTime:
        hourDifference = intStartingTime + intEndingTime - 24
    
    if hourDifference > 12:
        await ctx.send("Error, time in between the starting and ending time must be 12 hours or less.")
        return
    
    emojiList = []
    while len(emojiList) <= hourDifference:
        chosenEmoji = random.randint(0, (len(emoji_list)-1))
        if chosenEmoji in emojiList:
            pass
        else:
            emojiList.append(chosenEmoji)
    
    timeList = []
    listTime = int(startingTime)
    for i in range(hourDifference + 1):
        if listTime < 24:
            timeList.append(listTime)
            listTime += 1
        else:
            timeList.append(str(int(listTime)-24))
            listTime += 1

    print(emojiList)
    print(timeList)

    await ctx.send("@everyone , React with the corresponding emoji for times you are able to war!")

    msg = ''

    for i in range(len(timeList)):
        msg =  msg + str(timeList[i])+ str(timeZone) + ":    " + emoji_list[emojiList[int(i)]] + '\n'
    await ctx.send(msg)

    for i in range(len(timeList)):
        await ctx.message.add_reaction(emoji_list[emojiList[i]])

@client.command()
async def frameranking(ctx):
    await ctx.send(file = discord.File("images\\frameranking.png"))

@client.command()
async def tireranking(ctx):
    await ctx.send(file = discord.File("images\\tireranking.png"))

@client.command()
async def gliderranking(ctx):
    await ctx.send(file = discord.File("images\\gliderranking.png"))

@client.command()
async def coordinates(ctx):
    await ctx.send("Nether Portal/Ocean Monument : -481, 63, 233")
    await ctx.send("Base : 12, 68, 1510")
    await ctx.send("Nether Tunnel :  -76, 80, 211")


client.run("ODQ2NzUyMzM0MzcyNDA1Mjc5.YK0FkA.alTyrnTPXrRyvjxH87O1S_mi0Zo")
