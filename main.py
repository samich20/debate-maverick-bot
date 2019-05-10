import discord
from discord.ext.commands import Bot

TOKEN = 'NDAxOTg4MzgxMjM3NTc1Njgw.XNWh7w.8Kr03hJysw_V7rfKUXcrX6Tlrp4'

client = commands.Bot(command_prefix = 'm!')

# Indicates that the BOT is ready.
@client.event
async def on_ready():
    print('Maverick Bot is ready!')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# Tells user to not use bad language
@client.event
async def on_message(message):
    author = message.author
    content = message.content
    channel = message.channel
    if message == 'fuck' or 'shit' or 'bitch':
        print('@' + author + ', Mr. Maverick is disapointed...')

# [Command] yee
@client.command()
async def yee():
    #await.client.say('haw!')

# [Command] whois
    @client.command()
    async def whois(*args):
        for word in args:
            if word == 'Agamben' or 'agamben':
                output = 'Agamben Biography'
            if word == 'Baudrillard' or 'baudrillard':
                output = 'Baudrillard Biography'
            if word == 'Hobbes' or 'hobbes':
                output = 'Hobbes Biography'
            if word == 'Kant' or 'kant':
                output = 'Kant Biography'
            if word == 'Locke' or 'locke':
                output = 'Locke Biography'
        await client.say(output)

# [Command] Tests by echoing what the user inputs
@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

client.run(process.env.TOKEN);
