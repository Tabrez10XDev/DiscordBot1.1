import discord
import CONST
import time
import asyncio
import random
token = CONST.token
client = discord.Client()


messages = joined = 0
#https://discord.com/oauth2/authorize?client_id=764893385932406804&scope=bot&permissions=0
#739833441649950751

# async def update_stats():
#     await client.wait_until_ready()
#     global messages, joined
#     while not client.is_closed():
#         try:
#             with open("stats.txt","a") as f:
#                 f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")
#             await asyncio.sleep(3600)
#         except Exception as e:
#             print(e)
#             await asyncio.sleep(10)

# @client.event
# async def on_member_update(before,after):
#

@client.event
async def on_member_join(member):
    global joined
    joined+=1
    vasakaal = await client.fetch_channel(739833442119712911)

    await vasakaal.send(f"""A wild {member.mention} appeared""")



@client.event
async def on_message(message):
    global messages, joined
    messages+=1
    bad_words = ["love","kadhal"]
    counters = ["Sir ivana thooki jail la podunga","Dei unnala yaaru ulla vitta","Sangathuku bango vilavikka oruthan vandutandi","Po apdi poi MMBU","Ivan namakku thevaya","Goppa adha pathiye pesadha nee"]
    for word in bad_words:
        if message.content.find(word) != -1:
                await message.channel.purge(limit=1)
                await message.channel.send(counters[random.randint(0,len(counters))])
                #await message.channel.send(counters[len(counters)])
                break

    id = client.get_guild(739833441649950751)


    if message.content.find("!hello") != -1:
        await message.channel.send("Junk here resents your presence, thank you")
    elif message.content == "!help":
        embed = discord.Embed(title="Know the commands better", description="Things you can have Junk do apart from abusing you ")
        embed.add_field(name="!hello",value="Have the BOT greet you")
        embed.add_field(name="!users",value="Find total members in the channel")
        embed.add_field(name="!stats",value="To see how active the server was")
        embed.add_field(name="Anything love",value="Junk might verbally abuse you but you cant sue cuz i dont exist")
        await message.channel.send(content = None, embed=embed)
    elif message.content == "!users":
        await message.channel.send(f"""{id.member_count} mates are in this channel""")
    elif message.content == "!stats":
        await message.channel.send(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}")

#client.loop.create_task(update_stats())
client.run(token)
