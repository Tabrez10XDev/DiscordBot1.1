import discord
import CONST
token = CONST.token
client = discord.Client()

#https://discord.com/oauth2/authorize?client_id=764893385932406804&scope=bot&permissions=0

@client.event
async def on_message(message):
    print(message.content)
    print(message)

client.run(token)
