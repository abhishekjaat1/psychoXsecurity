import discord
from discord.ext import commands


class _logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Welcome commands"""
  
    def help_custom(self):
		      emoji = '<:snow1:1348326529129517067>'
		      label = "Logging"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Logging__(self, ctx: commands.Context):
        """`setuplog` , `resetlog`"""