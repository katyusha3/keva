import discord
import json
from discord import File
from discord.ext import commands
from easy_pil import Editor, load_image_async ,Font

with open('json/setting.json','r',encoding='utf8')as jfile:
    jdata=json.load(jfile)

class Menu(discord.ui.View):
    def __init__(self, inv: str):
        super().__init__()
        self.inv = inv
        self.add_item(discord.ui.Button(label="URL",url = self.inv))

    @discord.ui.button(label="領取按鈕",style=discord.ButtonStyle.blurple)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = 1080750234700890195
        user = interaction.user
        if role in [y.id for y in user.roles]:
            await interaction.response.send_message("你領過了，領三小!!!", ephemeral=True)
        else:
            await user.add_roles(user.guild.get_role(role))
            await interaction.response.send_message("領取成功", ephemeral=True)
    
    @discord.ui.button(label="伺服器連結",style=discord.ButtonStyle.blurple)
    async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(self.inv, ephemeral=True)
        

class welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(">>>> Welcome Is Online <<<<")

    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member = None):

        welcome_CH = member.guild.get_channel(int(jdata['welcome_channel']))

        #background = Editor("pic\welcome_pic.jpg")
        #memberavatar = member.avatar_url
        #profile_image = await load_image_async(str(memberavatar))

        #profile = Editor(profile_image).resize((150,150)).circle_image()
        #profile = Editor(background).resize((150,150)).circle_image()
        #poppins = Font.poppins(size=50, variant="bold")

        #poppins_small = Font.poppins(size=20, variant="light")

        #background.paste(profile, (325,90))
        #background.ellipse((325,90),150,150,outline="white",stroke_width=5)

        #background.text((400,260),f"WELCOME !!!",color="black",font=poppins,align="center")

        #file = File(fp=background.image_bytes,filename="pic\welcome_pic.jpg")
        await welcome_CH.send(f"Welcome <@{member.id}> ,請點選 \"領取按鈕\" 領身分組!!!")
        #await welcome_CH.send(file = file)
        inv = await welcome_CH.create_invite()#訊息所在的discord伺服器
        await welcome_CH.send(view=Menu(str(inv)))

    @commands.Cog.listener()
    async def on_member_remove(self, member:discord.Member = None):

        welcome_CH = member.guild.get_channel(int(jdata['leave_channl']))

        await welcome_CH.send(f"<@{member.id}> 離開了!!!")


async def setup(bot):
    await bot.add_cog(welcome(bot))