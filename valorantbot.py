import discord
import os
import valorant
import asyncio

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

        #VALORANT Testing
        if message.content == '!rank':
            await message.reply("Please type the name of the player you wish to see. Format is : user_name#tag_line")

            def check(msg):
                return msg.author == message.author and msg.channel == message.channel

            try:
                #Get a username and tagline by input
                response = await self.wait_for('message', check = check, timeout=60)
                user_name = response.content
                account = valorant_client.get_user_by_name(user_name)
                #Find their most recent ranked match
                match=account.matchlist().history.find(queueID="competitive")
                #Check if match exists
                if match == None:
                    await message.channel.send("No ranked match in recent history!")
                else:
                    match = match.get()
                #Print everyone's ranks
                for team in match.teams:
                    print(f"{team.teamID} Team's ranks: ")
                    #Find all players on the same team
                    players = match.players.get_all(teamId=team.teamID)

                    for player in players:
                        print(f"\t{player.gameName} - {player.rank}")
            except asyncio.TimeoutError:
                await message.channel.send("You took too long to respond")

        
KEY = os.environ["RIOT_TOKEN"]   
valorant_client = valorant.Client(KEY, locale='en-US')

intents = discord.Intents.default()
intents.message_content = True
intents.messages= True

client = MyClient(intents=intents)
client.run('DISCORD_TOKEN')
