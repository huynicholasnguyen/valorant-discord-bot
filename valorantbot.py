import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content == '!hello':
            author_name = message.author.name
            print(author_name)
            await message.channel.send('hello')
        
        if message.content == '!testing':
            await message.reply('More Testing')
        
        
            
            

intents = discord.Intents.default()
intents.message_content = True
intents.messages= True

client = MyClient(intents=intents)
client.run('MTA1NzA4Mzk4Njk1NjAwNTQxNg.GNovx2.d4d76gbFkb2YQrQkb-MqNs41u4RnfMz4V9jvZM')
