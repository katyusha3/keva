import discord
from discord.ext import commands
import json

with open('json/setting.json','r',encoding='utf8')as jfile:
    jdata=json.load(jfile)

def sj_data(j_data):

    j_name = []

    for i in j_data.keys():
        j_name.append(int(i))

    return j_name

class Menu(discord.ui.View):
    def __init__(self, inv: str):
        super().__init__()
        self.inv = inv
        self.add_item(discord.ui.Button(label="server URL",url = self.inv))

    @discord.ui.button(label="註冊按鈕",style=discord.ButtonStyle.blurple)
    async def Btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        #1顆按鈕用Btn
        #兩顆以上用menu1、2、3....
        await interaction.response.send_message("你已經是我的了",ephemeral=True)#ephemeral=True 只有點按鈕的人才能看到這訊息

        user = interaction.user.id

        with open('RPG_json/RPG.json','r',encoding='utf8')as jfile:
            RPG_jdata=json.load(jfile)
            rpg_jdata = RPG_jdata['rpg']

        r_name = sj_data(rpg_jdata)

        if int(user) not in r_name:
            rpg_jdata.setdefault(user,1)

        RPG_jdata['rpg'] = rpg_jdata

        with open('RPG_json/RPG.json','w',encoding='utf8') as jfile:
            json.dump(RPG_jdata,jfile)


class RPG_main(commands.Cog):
    
    @commands.command()
    async def RPG(self,ctx:commands.Context):
        inv = await ctx.channel.create_invite()#訊息所在的discord伺服器
        await ctx.send("請點選按鈕註冊RPG遊戲", view=Menu(str(inv)))


async def setup(bot):
    await bot.add_cog(RPG_main(bot))