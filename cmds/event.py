import discord
import datetime
import random
import json
from discord.ext import commands

with open('json/setting.json','r',encoding='utf8')as jfile:
    jdata=json.load(jfile)

class event(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(">>>> Event Is Online <<<<")

    @commands.command()
    async def ping(self,ctx):
        await ctx.channel.send(f'{round(self.bot.latency * 1000)}ms (´ཀ`」 ∠)')

    @commands.command()
    async def time(self,ctx):
        now=datetime.datetime.now().strftime("%Y/%m/%d  %H:%M")
        await ctx.channel.send(f'現在時間{now}')

    @commands.command()
    async def 猜拳(self,ctx,msg):
        mora=['剪刀','石頭','布']
        random_mora=random.choice(mora)
        if random_mora == '剪刀' and msg == '石頭' or random_mora == '石頭' and msg == '布' or random_mora == '布' and msg == '剪刀':
            await ctx.channel.send(f'我出{random_mora}，你贏了(´ . .̫ . `)')
        if random_mora == '剪刀' and msg == '布' or random_mora == '石頭' and msg == '剪刀' or random_mora == '布' and msg == '石頭':
            await ctx.channel.send(f'我出{random_mora}，你輸了(σ°∀°)σ')
        if random_mora == msg:
            await ctx.channel.send('平手ಠ_ಠ')
        if msg != '剪刀' and msg != '石頭' and msg != '布':
            await ctx.channel.send('凸')

    @commands.command()
    async def lucky(self,ctx):
        name=ctx.author.name
        L_num=(random.choice(range(99,1000)))/10
        L_list=['#$%@&!......','大凶','很凶','凶','沒凶','吉','小吉','中吉','大吉','超吉']
        Lucky=L_list[int(L_num/10)]
        LV_list=[]
        for i in range(int(L_num/10)):
            LV_list+='▮'
        for i in range(10-int(L_num/10)):
            LV_list+='▯'
        LV=''.join(LV_list)
        #ctx_pic=ctx.message.author.avatar_url
        embed=discord.Embed(title=f'{name}的運勢',description=f':six_pointed_star:幸運指數:\n{LV}{L_num}%\n{Lucky}',color=0x9a36dd,
                                timestamp=datetime.datetime.now())
        embed.set_footer(text="機器人作者:DJ Russia#4355(莎醬)")
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def food(self,ctx,*msg):
        food_list = []
 
        for food in msg:
            if food not in food_list:
                food_list.append(food)
        if len(msg)==len(food_list):
            if len(msg)==0:
                await ctx.channel.send('什麼都不寫，你吃空氣喔')
            elif len(msg)==1:
                await ctx.channel.send('啊就一個，你是有什麼選擇障礙')
            else:
                R_food=random.choice(msg)
                await ctx.channel.send(f'吃{R_food}')
        else:
            await ctx.send('重複三小')

    @commands.command()
    async def bot(self,ctx):
        bot_url="https://discord.com/api/oauth2/authorize?client_id=865877544707162152&permissions=0&scope=bot"
        embed=discord.Embed(title="輔助機器人",url=bot_url,color=0xFFE4CA,
                            timestamp=datetime.datetime.now())
        #embed.set_thumbnail(discord.File(jdata['head']))
        embed.add_field(name="我是你的貼心助手\n讓Discord不無聊",value="OuO", inline=True)
        embed.set_footer(text="機器人作者:DJ Russia#4355(莎醬)")
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def message(self,ctx,user:discord.Member,*,message = None):
        msg = "abcd"
        print(user)
        embed = discord.Embed(title=msg)
        await user.send(embed = embed)

async def setup(bot):
    await bot.add_cog(event(bot))