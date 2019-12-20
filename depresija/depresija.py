import json
import os
import re
from redbot.core import commands
import discord
# import urllib.request

BaseCog = getattr(commands, "Cog", object)

class Depresija(BaseCog):
    """Reply with today's name-days"""

    def __init__(self, bot):
        self.bot = bot
        self.emoji = None

        for i in bot.emojis:
            if "depresija" in i.name:
                self.emoji = i
                break

    @commands.Cog.listener()
    async def on_message(self, msg) -> None:
        if msg.author.id == 225915965769121792:
            if "depresija" in msg.content:
                await msg.channel.send(content=f"{msg.author.mention} {self.emoji}")

    # @commands.command()
    # async def vd(self, ctx, msg: str = None):
    #     """
    #     vd - Atgriež šodienas vārda dienu jubilārus
    #     vd [vārds] - Atgriež datumu kurā [vārds] svin vārda dienu
    #     vd [datums] - Atgriež [datums] vārda dienas jubilārus (formāts: dd.mm; dd/mm; dd,mm)
    #     """

    #     if msg is not None:
    #         date_regex = re.match(r"^(0[1-9]|1[0-9]|2[0-9]|3[0-1])(\.|\/|\,)(0[1-9]|1[0-2])$", msg)

    #     if msg is None:
    #         day = datetime.datetime.now().strftime("%d")
    #         month = datetime.datetime.now().strftime("%m")
    #         result = findByDate(self.data, day, month)

    #         included = result[0].replace(" ", ", ")
    #         excluded = result[1].replace(" ", ", ")

    #         if result:
    #             await ctx.send(f"{emoji} Šodien vārda dienu svin: `{included}`\n\n{emoji2} Kalendārā neiekļautie: *`{excluded}`*")
    #         else:
    #             await ctx.send(f"Kļūda! `{msg}` netika atrasts!")

    #     elif date_regex:
    #         day = date_regex.group(1)
    #         month = date_regex.group(3)
    #         result = findByDate(self.data, day, month)

    #         included = result[0].replace(" ", ", ")
    #         excluded = result[1].replace(" ", ", ")

    #         if result:
    #             await ctx.send(f"{emoji} Šodien vārda dienu svin: `{included}`\n\n{emoji2} Kalendārā neiekļautie: *`{excluded}`*")
    #         else:
    #             await ctx.send(f"Kļūda! `{msg}` netika atrasts!")

    #     else:
    #         result = findByName(self.data, msg)
    #         if result:
    #             await ctx.send(f"{emoji} {msg.title()} vārda dienu svin `{result}` datumā.")
    #         else:
    #             await ctx.send(f"Kļūda! `{msg}` netika atrasts!")
