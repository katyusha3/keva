import discord
from discord.ext import commands
#from discord.ui import Select

class select(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Blue",emoji="🟦",description="Blue role"),
            discord.SelectOption(label="Red",emoji="🟥",description="Red role"),
            discord.SelectOption(label="Green",emoji="🟩",description="Green role")
        ]
        super().__init__(placeholder="AAA",max_values=1,min_values=1,options=options)
    async def callback(self,interaction:discord.Integration):

        user = interaction.user
        guild = interaction.guild
        print(self.values[0],type(str(self.values[0])))

        if str(self.values[0]) == "Blue":
            print(2111)
            #role = await guild.create_role(name="Blue",colour=discord.Colour.blue())
            #await user.edit(roles = [role])
            await interaction.response.send_message("777",ephemeral=False)

class SelectView(discord.ui.View):
    def __init__(self, *, timeout=30):
        super().__init__(timeout=timeout)
        self.add_item(select())

class Menu(discord.ui.View):
    def __init__(self, inv: str):
        super().__init__()
        self.inv = inv
        self.add_item(discord.ui.Button(label="but-1",url = self.inv))

    @discord.ui.button(label="but-1",style=discord.ButtonStyle.blurple)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
        #1顆按鈕用Btn
        #兩顆以上用menu1、2、3....
        await interaction.response.send_message(self.inv, ephemeral=True)#ephemeral=True 只有點按鈕的人才能看到這訊息

    @discord.ui.button(label="but-2",style=discord.ButtonStyle.blurple)
    async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(self.inv, ephemeral=True)

class UI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def role(self,ctx):
        await ctx.send("Menus!",view = SelectView())

    @commands.Cog.listener()
    async def on_ready(self):
        print(">>>> UI Is Online <<<<")

    @commands.command()
    async def invite(self, ctx: commands.Context):
        inv = await ctx.channel.create_invite()#訊息所在的discord伺服器
        await ctx.send("Click the buttons below to invite someone!", view=Menu(str(inv)))

    @commands.command()##加入身分組
    async def addrole (self, ctx, role: discord.Role, user: discord.Member):
        if ctx.author.guild_permissions.administrator:
            await user.add_roles(role)
            await ctx.send(f"Successfully given {role.mention} to {user.mention}")
            print(role,type(role))

    @commands.command()##清除身分組
    async def remove (self, ctx, role: discord.Role, user:discord.Member):
        if ctx.author.guild_permissions.administrator:
            await user.remove_roles(role)
            await ctx.send(f"Successfully remove {role.mention} to {user.mention}")

async def setup(bot):
    await bot.add_cog(UI(bot))