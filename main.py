import discord

hello_words = ['пішов ти', 'пішов ти клоун', 'hi', 'hello']
secret_words = ['бунт', ]
true_words = ['правда', 'докажи', 'правда?', 'правда, ботяра?', 'правда, ботяра', 'правда ботяра?', 'правда, ботяра']

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()
    msg_list = msg.split()


#hello words
    if (msg in hello_words):
        await message.channel.send(f' {message.author.mention} Здоровенькі були!')

    elif (msg in true_words):
        await message.channel.send(f'{message.author.mention} Правда, правда.....')


client.run('Nzg1NjE3NjQ5MDg2MjM0NjI1.X86dcw.pusjl2w-u6JFKlj63i_6t4wtu5A')








# find_hello_words = False
# for item in find_hello_words:
#     if msg.find(item) >= 0:
#         find_hello_words = True
# if (find_hello_words) == True:
