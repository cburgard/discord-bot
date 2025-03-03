import discord
from discord.ext import commands

import utils as ut


### @package misc
#
# Collection of miscellaneus helpers.
#

class Misc(commands.Cog):
    """
    Various useful Commands for everyone
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping', help="Check if Bot available")
    async def ping(self, ctx):
        """!
        ping to check if the bot is available

        @param ctx Context of the message
        """
        print(f"ping: {round(self.bot.latency * 1000)}")

        await ctx.send(
            embed=ut.make_embed(
                name='Poll-Bot is available',
                value=f'`{round(self.bot.latency * 1000)}ms`')
        )


def setup(bot):
    bot.add_cog(Misc(bot))
