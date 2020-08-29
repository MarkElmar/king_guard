import mysql.connector
from discord import Client
from discord.ext import commands


class Kingdom(commands.Cog, name='Kingdom'):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='create', aliases=['c', 'make'])
    async def _create(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Just create')
        else:
            pass

    @_create.command(name='kingdom', aliases=['k', 'guild'])
    async def _kingdom(self, ctx, *, name):
        fetch = 0
        db = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='',
                                     database='kingdom')
        cursor = db.cursor()
        # Checks if kingdom_name exists
        cursor.execute(f"SELECT * FROM kingdoms WHERE kingdom_name = '{name}'")
        try:
            fetch = cursor.fetchall()
        finally:
            if len(fetch) > 0:
                await ctx.send("This kingdom name has already been used")
            else:
                # Await for confirmation name
                await ctx.send(f"Are you sure you want {name} to be your kingdoms name!")
                await ctx.send(f"Type CONFIRM to confirm the name!")

                await Client.wait_for(self.bot, timeout=60.0, event='message', check=lambda
                    message: message.author == ctx.author and message.content == 'CONFIRM')

                guild = ctx.message.guild

                # Creates Category
                category = await guild.create_category(name=name)

                cursor.execute(f"INSERT INTO kingdoms (kingdom_name, category_id) VALUES ('{name}', {category.id})")
                db.commit()
                print(category.id)
                await ctx.send("Kingdom successfully created!")
                await ctx.send("Are you a king or queen use reaction to answer!")

                msg = await Client.wait_for(self.bot, event='message', check=lambda
                    message: message.author == ctx.author and message.content == 'king' or message.content == 'queen')

    @_create.command(name='vchannel', aliases=['vc', 'voicechannel', 'voice-channel'])
    async def _voice_channel(self, ctx, *, name):
        # TODO make voice channels add able
        pass

    @_create.command(name='tchannel', aliases=['tc', 'textchannel', 'text-channel'])
    async def _text_channel(self, ctx, *, name):
        pass
