import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content == '!hello':
            await message.channel.send('Hello!', mention_author=True)
            
            

intents = discord.Intents.default()
intents.message_content = True
intents.messages= True

KEY = os.environ["RGAPI-5bf6523b-a056-446f-8193-1ba6b65e6eec"]
client = MyClient(intents=intents)
client.run('MTA1NzA4Mzk4Njk1NjAwNTQxNg.GNovx2.d4d76gbFkb2YQrQkb-MqNs41u4RnfMz4V9jvZM')
