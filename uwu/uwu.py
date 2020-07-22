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
            message.lower().replace('r', 'w').replace('l', 'w').replace('n', 'ny')
        )