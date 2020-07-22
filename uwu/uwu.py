import asyncio
import discord
from redbot.core import commands


class Uwu(commands.Cog):
    """uwuify a message"""

    def __init__(self, bot):
        self.bot = bot
        self.channels = {}

    @commands.command()
    async def uwu(self, ctx, *, message: str):
        """uwuifys a message"""
        return await ctx.send(
            self.owo(message.lower())
        )
    dictionary = {'you': 'yuw', 'and': 'awnd', 'lol': 'lawl', 'is': 'ish', 'anybody': 'anybowdy', 'the':'da'}


    def owo(self, text):
        words = text.split()
        for i in range(0, len(words)): 
            word = words[i]
            if word in dictionary:
                words[i] = dictionary[word]
                text = ' '.join(words)

        text = text.replace('l', 'w')
        text = text.replace('r', 'w')

        return text