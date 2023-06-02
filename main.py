import discord
import asyncio
import os
import json
import datetime
import time
#import keep_alive
from pypresence import Presence
from tqdm import tqdm, trange
from discord.ext import commands


with open('json/setting.json','r',encoding='utf8')as jfile:
    jdata=json.load(jfile)

intents = discord.Intents.all()
intents.members = True
 
bot=commands.Bot(command_prefix='>>',intents=intents, help_command=None)

client_id = "865877544707162152"
RPC = Presence(client_id)
RPC.connect()

RPC.update(
        large_image="海倫",
        large_text="discord bot",
        details="海倫 is discord bot",
        state="啊哈",
        start=time.time(),
        small_image="https://c.tenor.com/TgKK6YKNkm0AAAAi/verified-verificado.gif",
        buttons=[
            {"label":"我的 YouTube :)","url":"https://www.youtube.com/channel/UCUGIrGewFVh6QVexQlSs1_Q"},
            {"label":"加入海倫","url":"https://reurl.cc/zZjGYa"}
            ]
        )

def wlaod(file):
    fun = 0
    for filename in tqdm(os.listdir('./cmds')):
        if filename.endswith(".py"):
            if filename[:-3] == file:
                fun = "cmds"
    for filename in tqdm(os.listdir('./RPG_cod')):
        if filename.endswith(".py"):
            if filename[:-3] == file:
                fun = "RPG_cod"

    return fun

@bot.event
async def on_ready():
    print(">>>> Discord Bot Is Online <<<<")
    online_CH = bot.get_channel(int(jdata['online_channel']))
    #await online_CH.send('Discord Bot Is Online')

    embed=discord.Embed(title="DISCORD", color=0xFFE4CA,
                                timestamp=datetime.datetime.utcnow())
    embed.add_field(name=":white_check_mark:Discord Bot Is Online",value="", inline=True)
    #embed.set_footer(text="機器人作者:DJ Russia#4355(莎醬)")
    await online_CH.send(embed=embed)

@bot.command()
async def stop(ctx):
    jdata['Load'] = 0
    await load()
    await ctx.send('All Code Is Unload')

@bot.command()
async def start(ctx):
    jdata['Load'] = 1
    await load()
    await ctx.send('All Code Is Load')

@bot.event
async def on_message(msg):
    if jdata['Load'] == 0:
        if '>>' in msg.content:
            await msg.channel.send("維護中...")

    await bot.process_commands(msg)
    if msg[0] == '>>':
        return
    if msg.author.id == bot.user.id:
        return
    await msg.channel.send("Hello friend")

@bot.command()
async def load(ctx, extension):
    file = wlaod(extension)
    await bot.load_extension(f'{file}.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    file = wlaod(extension)
    await bot.unload_extension(f'{file}.{extension}')
    await ctx.send(f'Un-Loaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    file = wlaod(extension)
    await bot.reload_extension(f'{file}.{extension}')
    await ctx.send(f'Re-Loaded {extension} done.')

async def setup():
    print("Setting Up...")

async def load():
    for filename in tqdm(os.listdir('./cmds')):
        if filename.endswith(".py"):
            if jdata['Load'] == 1:
                await bot.load_extension(f"cmds.{filename[:-3]}")
            else:
                await bot.unload_extension(f"cmds.{filename[:-3]}")

    for filename in tqdm(os.listdir('./RPG_cod')):
        if filename.endswith(".py"):
            if jdata['Load'] == 1:
                await bot.load_extension(f"RPG_cod.{filename[:-3]}")
            else:
                await bot.unload_extension(f"RPG_cod.{filename[:-3]}")


async def main():
    await load()
    await setup()
    #keep_alive.keep_alive()
    
    await bot.start(jdata['TOKEN'])

asyncio.run(main())