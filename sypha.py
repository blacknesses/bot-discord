import os
import discord
import asyncio


os.system("clear")

class MyClient(discord.Client):    
    # logando no bot
    async def on_ready(self):
        print('Logamos como: {0}'.format(self.user))

    # respondendo os client
    async def on_message(self, message):
        username = str(message.author).split("#")[0]
        user_message = str(message.author.name)
        channel = str(message.channel.name)
        print(f"{username}: {message.content} ({channel})")
        
        if message.author == client.user:
            return
        
        msg = message.content

        if msg.lower() == "sypha":
            await message.channel.send(f"Olá {message.author.name}!! como posso ajudá-lo??👩‍🦰")
            
        if msg.startswith("menu:"):
            await message.channel.send(f"segue o menu")
            
            
    # boas vindas aos membros novos
    async def on_member_join(self, member):
        guild = member.guild
        msg = await guild.system_channel.send(f"👩‍🦰 uhuuu !! bem vindo(a) {member.mention}, se apresente para nós, diga de onde vens, a onde quer chegar, seu objetivo em entrar aqui, seu nivel de conhecimento e também leia as regras do servidor.😁")
        await asyncio.sleep(60)
        await msg.delete()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = MyClient(intents=intents)
client.run("TOKEN")
