import discord
from discord.ext import commands
import json
import datetime

with open('json/setting.json','r',encoding='utf8')as jfile:
    jdata=json.load(jfile) 

def sj_data(j_data):

    j_name = []

    for i in j_data.keys():
        j_name.append(int(i))

    return j_name  

class rank(commands.Cog):
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(">>>> Help Is Online <<<<")

    @commands.Cog.listener()
    async def on_message(self, msg):

        with open('RPG_json/RPG.json','r',encoding='utf8')as jfile:
            RPG_jdata=json.load(jfile)
            rank_jdata = RPG_jdata['rank']

        xp = 0

        str = msg.content#讀取訊息文字
        name_ID = msg.author.mention#使用者ID

        name_ID = ''.join(filter(lambda name_ID:name_ID in'0123456789',name_ID))

        r_name = rank_jdata.keys()

        for i in str:#讓經驗值不要超過50
            if '\u4e00' <= i <= '\u9fa5':
                xp+=1
            if xp>49:
                break
        #print(msg.author.name)
        #print(xp)
        #print('----')

        if name_ID not in r_name:
            rank_jdata.setdefault(name_ID,[xp,0])
            print()
        else:
            rank_jdata[name_ID][0] += xp

        if rank_jdata[name_ID][0] >= ((rank_jdata[name_ID][1]+1)**2)*100:
            rank_jdata[name_ID][1]=int((rank_jdata[name_ID][0]/100)**0.5)

            embed=discord.Embed(title="等級", description=f'<@{name_ID}>升為{rank_jdata[name_ID][1]}等！', color=0xFFE4CA,
                                timestamp=datetime.datetime.now())
            embed.set_footer(text="機器人作者:DJ Russia#4355(莎醬)")
            await msg.channel.send(embed=embed)
            rank_jdata[name_ID][0] = 0

            RPG_jdata['rank'] = rank_jdata

        with open('RPG_json/RPG.json','w',encoding='utf8') as jfile:
            json.dump(RPG_jdata,jfile)

    @commands.command()
    async def rank (self,ctx):

        with open('RPG_json/RPG.json','r',encoding='utf8')as jfile:
            RPG_jdata=json.load(jfile)
            rank_jdata = RPG_jdata['rank']

        r_name = sj_data(rank_jdata)

        name_ID=str(ctx.author.id)

        if int(name_ID) in r_name:

            next_xp = ((rank_jdata[name_ID][1]+1)**2)*100
            now_xp = rank_jdata[name_ID][0]

            need_xp = next_xp - now_xp
            xp_percent = int((now_xp / next_xp)*100)

            LV_list=[]

            for i in range(int(xp_percent/10)):
                LV_list+='▮'
            for i in range(int(10-xp_percent/10)):
                LV_list+='▯' 

            LV=''.join(LV_list)

            #ctx_pic=ctx.message.author.avatar_url
            embed=discord.Embed(title="等級系統", description=f'Discord玩家\n<@{name_ID}>\n{LV}{xp_percent}%', color=0xFFE4CA,
                                    timestamp=datetime.datetime.now())
            #embed.set_thumbnail(url=ctx_pic)
            embed.add_field(name="等級", value=rank_jdata[name_ID][1], inline=True)
            embed.add_field(name="目前經驗", value=rank_jdata[name_ID][0]+((rank_jdata[name_ID][1])**2)*100, inline=True)
            embed.add_field(name="距離一下一等還要", value=f'{need_xp}XP', inline=True)
            embed.add_field(name="玩家ID", value=ctx.author.id, inline=True)

            embed.set_footer(text="機器人作者:DJ Russia#4355(莎醬)")
            await ctx.channel.send(embed=embed)
        else:
            await ctx.send("查無資料")

    
async def setup(bot):
    await bot.add_cog(rank(bot))