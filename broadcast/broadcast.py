import asyncio
import discord
from redbot.core import commands, Config
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import box

class Broadcast(commands.Cog):
    """Broadcast
       Broadcasts into a group of channels.

       (You might want to set up permissions properly using the Permissiosn cog)"""

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=10385)
        default_guild = {
            "domains": {}
        }
        self.config.register_guild(**default_guild)

    @commands.group(name=domain)
    @commands.guild_only()
    async def domain(self,ctx):
        """Options for broadcast domains"""
        pass
    @domain.command(name="list")
    async def domainlist(self, ctx):
        """Lists all domains

           Usage: [p]domain list"""
        server = ctx.guild
        user = ctx.author
        title = "Domains in {}\n".format(server.name)
        icon_url = server.icon_url
        msg = ""
        doms = await self.config.guild(ctx.guild).domains()
        if len(doms) == 0:
            await ctx.send('❌ No domains created yet, create one with \'domain create\'')
        else:
            async for domain in doms:
                msg += domain + "\n"
        em = discord.Embed(description=box(msg), colour=user.colour)
        em.set_author(name=title, icon_url=icon_url)

        await ctx.send(embed=em)

    async def asyncit(self, iterable):
        for i in iterable:
            yield i
            await asyncio.sleep(0)