import discord
import json
from discord.ext import commands

with open('json/setting.json','r',encoding='utf8')as jfile:
    jdata=json.load(jfile)

class Menu(discord.ui.View):
    def __init__(self, inv: str):
        super().__init__()
        # self.inv = inv
        # self.add_item(discord.ui.Button(label="but-1",url = self.inv))

    @discord.ui.button(label="ping",style=discord.ButtonStyle.blurple)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("顯示現在ping值", ephemeral=True)

    @discord.ui.button(label="time",style=discord.ButtonStyle.blurple)
    async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("顯示台灣現在時間", ephemeral=True)

    @discord.ui.button(label="猜拳",style=discord.ButtonStyle.blurple)
    async def menu3(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("跟海倫進行猜拳", ephemeral=True)

    @discord.ui.button(label="lucky",style=discord.ButtonStyle.blurple)
    async def menu4(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("運勢", ephemeral=True)

    @discord.ui.button(label="bot",style=discord.ButtonStyle.blurple)
    async def menu5(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("機器人基本資料", ephemeral=True)

class help_select(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="通用指令",emoji="🟦",description="cmds"),
            discord.SelectOption(label="RPG指令",emoji="🟥",description="RPG_cod"),
        ]
        super().__init__(placeholder="請選指令",max_values=1,min_values=1,options=options)
    async def callback(self,interaction:discord.Integration):

        if str(self.values[0]) == "通用指令":
            await interaction.response.send_message("通用指令",view=Menu(),ephemeral=True)
            
            
        elif str(self.values[0]) == "RPG":
            await interaction.response.send_message("RPG指令",ephemeral=True)
            

class help_SelectView(discord.ui.View):
    def __init__(self, *, timeout=30):
        super().__init__(timeout=timeout)
        self.add_item(help_select())

class Help(commands.Cog):

    @commands.Cog.listener()
    async def on_ready(self):
        print(">>>> Help Is Online <<<<")

    @commands.command()
    async def help(self,ctx):
        await ctx.send("Help!",view = help_SelectView())


async def setup(bot):
    await bot.add_cog(Help(bot))