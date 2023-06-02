import discord
from discord.ext import commands
import json

with open('json/setting.json','r',encoding='utf8')as jfile:
    jdata=json.load(jfile)

def Job_name (name_ID,Profession_):

    with open('RPG_json/RPG.json','r',encoding='utf8')as jfile:
        RPG_jdata=json.load(jfile)
        job_jdata = RPG_jdata['job']

    Profession_j = job_jdata['Profession']

    P_name = []

    for i in Profession_j.keys():
        P_name.append(int(i))

    if name_ID not in P_name:
        Profession_j.setdefault(name_ID,Profession_)

    job_jdata['Profession'] = Profession_j
    RPG_jdata['job'] = job_jdata

    with open('RPG_json/RPG.json','w',encoding='utf8') as jfile:
        json.dump(RPG_jdata,jfile)

def sj_data(j_data):

    j_name = []

    for i in j_data.keys():
        j_name.append(int(i))

    return j_name

class select(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="漁夫",emoji="🐟",description="fisherman!!!"),
            discord.SelectOption(label="廚師",emoji="🍴",description="chef!!!"),
            discord.SelectOption(label="農夫",emoji="🍎",description="farmer!!!"),
            discord.SelectOption(label="筏木工",emoji="🪓",description="lumberjack!!!"),
            discord.SelectOption(label="鐵匠",emoji="⚒️",description="blacksmith!!!"),
            discord.SelectOption(label="釀酒師",emoji="🍾",description="Winemaker!!!"),
            discord.SelectOption(label="礦工",emoji="⛏️",description="miner!!!")
        ]
        super().__init__(placeholder="請選擇職業",max_values=1,min_values=1,options=options)
    async def callback(self,interaction:discord.Integration):

        user = interaction.user.id

        if str(self.values[0]) == "漁夫":
            await interaction.response.send_message("你選擇了漁夫",ephemeral=True)
            
        elif str(self.values[0]) == "廚師":
            await interaction.response.send_message("你選擇了廚師",ephemeral=True)
            
        elif str(self.values[0]) == "農夫":
            await interaction.response.send_message("你選擇了農夫",ephemeral=True)
            
        elif str(self.values[0]) == "筏木工":
            await interaction.response.send_message("你選擇了筏木工",ephemeral=True)
            
        elif str(self.values[0]) == "鐵匠":
            await interaction.response.send_message("你選擇了鐵匠",ephemeral=True)
            
        elif str(self.values[0]) == "釀酒師":
            await interaction.response.send_message("你選擇了釀酒師",ephemeral=True)
            
        elif str(self.values[0]) == "礦工":
            await interaction.response.send_message("你選擇了礦工",ephemeral=True)
        
        Job_name(user,str(self.values[0]))
            

class SelectView(discord.ui.View):
    def __init__(self, *, timeout=30):
        super().__init__(timeout=timeout)
        self.add_item(select())

class job(commands.Cog):

    @commands.command()
    async def job(self,ctx):

        name_ID=str(ctx.author.id)

        with open('RPG_json/RPG.json','r',encoding='utf8')as jfile:
            RPG_jdata=json.load(jfile)
            rpg_jdata = RPG_jdata['rpg']

        r_name = sj_data(rpg_jdata)
        print(r_name)

        if int(name_ID) in r_name and rpg_jdata[name_ID] == 1:
            await ctx.send("請選職業",view = SelectView())
        else:
            await ctx.send("尚未註冊，請輸入>>RPG指令註冊")

    @commands.command()
    async def sjob(self,ctx):
        name_ID=str(ctx.author.id)

        with open('RPG_json/RPG.json','r',encoding='utf8')as jfile:
            RPG_jdata=json.load(jfile)
            job_jdata = RPG_jdata['job']
            Profession_j = job_jdata['Profession']

        P_name = sj_data(Profession_j)
        #print(P_name)

        if int(name_ID) not in P_name:
            await ctx.send("查無資料")
        else:
            embed = discord.Embed(title="職業系統",
                                description=f'\n🔔<@{name_ID}>\n 的職業是{Profession_j[name_ID]}',
                                color=0xFF0000
                                )
            await ctx.send(embed = embed)

async def setup(bot):
    await bot.add_cog(job(bot))