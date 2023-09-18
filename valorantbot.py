import discord
import os
import valorant

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith('!hello'):
            await message.reply('Hello!', mention_author=True)

intents = discord.Intents.default()
intents.message_content = True
intents.messages= True

KEY = os.environ["RGAPI-5bf6523b-a056-446f-8193-1ba6b65e6eec"]
valorant_client = valorant.Client(KEY, locale=None)
skins = valorant_client.get_skins()
client = MyClient(intents=intents)
client.run('MTA1NzA4Mzk4Njk1NjAwNTQxNg.GNovx2.d4d76gbFkb2YQrQkb-MqNs41u4RnfMz4V9jvZM')
