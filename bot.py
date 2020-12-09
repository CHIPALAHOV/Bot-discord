token = 'Nzg1NjE3NjQ5MDg2MjM0NjI1.X86dcw.c7CJolLG4irtMhma8QCiUrgmU_k'

import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='.')
client = discord.Client()





@bot.command()
async def prof(ctx, arg):
   if arg.lower() == 'chipalahov':
      await ctx.channel.purge(limit=1)
      emb_chip = discord.Embed(title='Profile', colour=discord.Color.from_rgb(240, 3, 252))
      emb_chip.set_author(name='CHIPALAHOV', icon_url='https://cdn.discordapp.com/avatars/674701053425352714/725c05b04cabb152f43effcbf0e1bcab.webp?size=1024')
      emb_chip.set_image(url='https://cdn.discordapp.com/avatars/674701053425352714/725c05b04cabb152f43effcbf0e1bcab.webp?size=1024')
      emb_chip.set_footer(text='''Вік цієї мразі: 12 с палавинкай
                                 Звання клоуна: Старший художник
                                 Посещаємость сервера: висока
                                 Опис: любить аніме й твою маму :3. 
                                 Любить ♂gachi♂
                                 Йобнутий ♂boy♂''')
      await ctx.send(embed=emb_chip)
   elif arg.lower() == 'zionert':
      await ctx.channel.purge(limit=1)
      emb_naz = discord.Embed(title='Profile', colour=discord.Color.from_rgb(3, 252, 19))
      emb_naz.set_author(name='Zionert',icon_url='https://cdn.discordapp.com/avatars/472409001372549130/a4ba709f073eb6f93d6aae77dbd62d07.webp?size=1024%27')
      emb_naz.set_image(url='https://cdn.discordapp.com/avatars/472409001372549130/a4ba709f073eb6f93d6aae77dbd62d07.webp?size=1024%27')
      emb_naz.set_footer(text='''Вік цієї мразі: 14
                                 Звання клоуна: модератор
                                 Посещаємость сервера: висока
                                 Короткий опис: любить аніме й осу. 
                                 Обладатель Cyberpunk 2077.
                                 Любить ♂gachi♂
                                 Норм ♂man♂''')
      await ctx.send(embed=emb_naz)
   elif arg.lower() == 'marcherov':
       await ctx.channel.purge(limit=1)
       emb_naz = discord.Embed(title='Profile', colour=discord.Color.from_rgb(181, 7, 33))
       emb_naz.set_author(name='Marcher_OV',
                          icon_url='https://cdn.discordapp.com/avatars/401065198548680704/4e6c1db806ef9d58fe5a6ae889504fde.png?size=128')
       emb_naz.set_image(url='https://cdn.discordapp.com/avatars/401065198548680704/4e6c1db806ef9d58fe5a6ae889504fde.png?size=128')
       emb_naz.set_footer(text='''Вік цієї мразі: 14
                                    Звання клоуна: Старший художник(поставте)
                                    Посещаємость сервера: пізда висока
                                    Короткий опис: любить аніме і себе)). 
                                    Обладатель Cyberpunk 2077.
                                    Любить ♂gachimuchi♂
                                    Норм ♂master♂''')
       await ctx.send(embed=emb_naz)
@bot.command()
async def dio(ctx):
    await ctx.channel.purge(limit = 1)
    emb = discord.Embed(title='Dio Brando (The World)', colour=discord.Color.red())
    emb.set_image(url='https://i.ytimg.com/vi/i5inOAXURVw/maxresdefault.jpg')
    emb.set_author(name='{0.author}'.format(ctx), icon_url=ctx.message.author.avatar_url)
    await ctx.send( embed = emb )


@bot.command()
async def jotaro(ctx):
    await ctx.channel.purge(limit = 1)
    emb2 = discord.Embed(title='Jotaro "JoJo" Kujo (Star Platinum)', colour=discord.Color.blue())
    emb2.set_image(url='https://i.redd.it/rktkvir2mgh21.jpg')
    emb2.set_author(name='{0.author}'.format(ctx), icon_url=ctx.message.author.avatar_url)

    await ctx.send ( embed = emb2 )


bot.run(token)
