import asyncio
import discord
from redbot.core import commands
from redbot.core.utils.common_filters import filter_mass_mentions


class PressH(commands.Cog):
    """Press some h."""

    def __init__(self, bot):
        self.bot = bot
        self.channels = {}

    @commands.command()
    @commands.bot_has_permissions(add_reactions=True)
    async def pressh(self, ctx, *, user: discord.User = None):
        """Press h for someone"""
        if str(ctx.channel.id) in self.channels:
            return await ctx.send(
                "Oops! I'm still h'ing in this channel, you'll have to wait until I'm done."
            )
        self.channels[str(ctx.channel.id)] = {}

        if user:
            answer = user.display_name
        else:
            await ctx.send("What do you want to press h to?")

            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel

            try:
                pressf = await ctx.bot.wait_for("message", timeout=120.0, check=check)
            except asyncio.TimeoutError:
                del self.channels[str(ctx.channel.id)]
                return await ctx.send("You took too long to reply.")

            answer = pressf.content[:1900]

        message = await ctx.send(
            f"Everyone, let's press h to **{filter_mass_mentions(answer)}**! Press the h reaction on the this message to h."
        )
        await message.add_reaction("\U0001F1ED")
        self.channels[str(ctx.channel.id)] = {'msg_id': message.id, 'reacted': []}
        await asyncio.sleep(120)
        try:
            await message.delete()
        except (discord.errors.NotFound, discord.errors.Forbidden):
            pass
        amount = len(self.channels[str(ctx.channel.id)]['reacted'])
        word = "person has" if amount == 1 else "people have"
        await ctx.send(f"**{amount}** {word} h'd to **{filter_mass_mentions(answer)}**.")
        del self.channels[str(ctx.channel.id)]

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if str(reaction.message.channel.id) not in self.channels:
            return
        if self.channels[str(reaction.message.channel.id)]['msg_id'] != reaction.message.id:
            return
        if user.id == self.bot.user.id:
            return
        if user.id not in self.channels[str(reaction.message.channel.id)]['reacted']:
            if str(reaction.emoji) == "\U0001F1ED":
                await reaction.message.channel.send(f"**{user.name}** has h'd.")
                self.channels[str(reaction.message.channel.id)]['reacted'].append(user.id)
                
    @commands.command()
    async def h(self, ctx, *, user: discord.User = None):
        """h"""
        return await ctx.send(
            "h"
        )