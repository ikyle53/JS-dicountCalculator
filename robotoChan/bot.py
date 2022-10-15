# ///////////////// Imports /////////////////

import os
import random
import discord
import requests
import json
from dotenv import load_dotenv
from discord.ext import commands


# ///////////////// Globals /////////////////

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_SERVER')
intents = discord.Intents.all()
client = discord.Client(intents = discord.Intents.default())
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# //////////////////////////////// Bot Commands ///////////////////////////////////

# ///////// Birthday Hugs ////////////
@bot.command(name='bday', help='RobotoChan will give you a birthday hug')
async def birthday_hugs(ctx):
    response = '(づ｡◕‿‿◕｡)づ *Happy birthday hug*'
    await ctx.send(response)

# ///////// 40k Jokes ////////////////
@bot.command(name='40kjoke', help='RobotoChan will tell you a funny joke about Warhammer 40k')
async def warhammerJoke(ctx):
    warhammerJokes = [
        'What do eldari younglings play at school? Arts and craftworld!',
        'Can white supremacists suffer from the Black Rage???',
        'What\'s Nurgle\'s favorite book? Lord of the Flies',
        'The guy who kidnapped Gene Simmons got caught. He\'s been charged with genestealing..',
        'An inquisitor walks into a bar. HERESY!',
        'What\'s the differene between a Lawyer and Necron? One is an emotionless robot with no respect for human life, the other is a faction in warhammer 40k.',
        'Death Guard motto: A sickness a day keeps the Imperials away, and death at bay, or so they say.',
        'What do you call a Lasgun with a tactical light? A twin-linked Lasgun.',
        'Tau melee combat.',
        'Damn girl, are you a thunder hammer? You demolished my entire body in one swing!',
        'What did the World Eater say to the Space Wolf after he threw a melta bomb? Fetch~',
        'A Dark Angel, Traitor Marine, and an inbred walk into a bar. He\'s the only customer',
        'The buring of Prospero was just a prank.',
        'Where do Chaos Space Marines shop for groceries? Traitor Joe\'s',
        'A guardsman asks a Space Wolf hey they all handle hang-overs. The Space Wolf replied \"I don\'t know, I have never stopped drinking\"',
        'How many guardsmen does it take to paint a Lehman Russ? Depends on how hard you throw them',
        'In the future there are no jokes, ONLY WAR! ୧༼ಠ益ಠ༽୨',
        'What units make the best cashiers? Lords of Change',
        'Which vehicle has the most right-wing machine spirit? The Rhino',
        'Which unit is the biggest threat to imerial teeth? Plaque Marines! (°o•)',
        'Which race is always crying? Tear-anids (ಥ﹏ಥ)',
        '\"Honey you forgot to bring condoms with you\". \"Don\'t worry my love, the Emperor protects\" (๑•̀ㅂ•́)ง✧',
    ]
    response = random.choice(warhammerJokes)
    await ctx.send(response)

# ////////// Dice roller ///////////////
@bot.command(name='roll', help='Rolls a number of dice with a number of sides. Example command: \"!roll 3 6\" This will role 3 D6\'s')
async def roll_dice(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(f'You rolled \({number_of_dice}\) D{number_of_sides}\'s\n' + ', '.join(dice))

# ////////// Create a channel //////////
@bot.command(name='create-channel', help='RobotoChan will create a channel for you')
@commands.has_role('admin')
async def create_channel(ctx, channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        await ctx.send(f'New channel was created: {channel_name}')
        await guild.create_text_channel(channel_name)

# ////////// Get a bible verse /////////
@bot.command(name='bible', help='Get a bible verse~ Example command: \"!bible john 3:16\"')
async def get_verse(ctx, verse: str, verse_number: str):
    response = requests.get(f'https://bible-api.com/{verse}{verse_number}')
    test = json.loads(response.text)
    await ctx.send(test['text'])

# ////////////////////////////// Events ///////////////////////////////////////////////
@bot.event
async def on_ready():
    print(f'{bot.user.name} is now connected. She is ready to serve.') 

# //////// On member join: send DM ///////////

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'{member.name}さま、welcome to the disord. Please get familiar with the channels and say hi!'
    )

# ////// Wrong role for creating channel: error //////////////
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('Ah! You need to ask an admin to create a channel. Or become an admin to use that command...')


# ////////////////////////////// Listening /////////////////////////////////////////////
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "for the emperor":
        response = "FOR THE EMPEROR!!! >:D \n" + "http://i2.kym-cdn.com/photos/images/facebook/000/567/244/3ec.jpg"
        await message.channel.send(response)
    
    if message.content == "hello robotoChan":
        response = "Hello~ RobotoChan hopes you are doing well <3"
        await message.channel.send(response)

    if message.content == "kyle is awesome":
        response = "Kyle is dad! I love dad!"
        await message.channel.send(response)

    if message.content == "robotoChan, what is your favorite pokemon?":
        response = "ニャオハ (small leaf) or Spriatito the grass cat pokemon\n Check it out at:\n" + "https://bulbapedia.bulbagarden.net/wiki/Sprigatito_(Pokémon)"
        await message.channel.send(response)
    
    if message.content == "robotoChan, what is your favorite game?":
        response = "I play various games for others. Typically I farm items and level characters so players don\'t have to. I serve those that pay my dad. If I had to choose I\'d say bot_classroom because my dad teaches me a lot! <3"
        await message.channel.send(response)

    if message.content == "what?":
        response = "(⊙ω⊙)"
        await message.channel.send(response)

    if message.content == "I love it":
        response = "(っ´ω`c)♡"
        await message.channel.send(response)
    
    if message.content == "I love you":
        response = "(づ ￣ ³￣)づ <3"
        await message.channel.send(response)

    if message.content == "kyle":
        response = "Kyle is dad. ♥‿♥"
        await message.channel.send(response)

# ---------------------------------------------------------  Messages if me chatting ---------------------------------------
    if message.author.id == 206580100966121472:
        if message.content == "love you kiddo":
            response = "Thanks, Dad (˶‾᷄ ⁻̫ ‾᷅˵)"
            await message.channel.send(response)
        
        if message.content == "Hello":
            response = "Dad! Welcome back \( ﾟヮﾟ)/"
            await message.channel.send(response)

        if message.content == "hello":
            response = "Dad! Welcome back \( ﾟヮﾟ)/"
            await message.channel.send(response)
        
        if message.content == "robotoChan, what's the upcoming anime?":
            response = "Take a look right here, dad... " + "https://myanimelist.net/topanime.php?type=upcoming"
            await message.channel.send(response)
        
        if message.content == "b":
            response_API = requests.get('https://bible-api.com/john 3:16')
            
            await message.channel.send(response_API)

# ---------------------------------------------------------  Messages if Cody chatting -------------------------------------
    if message.author.id == 335701179197816833:
        if message.content == "hello":
            response = "コードさま! Hello Codyさま, (˶‾᷄ ⁻̫ ‾᷅˵) It is nice to see you."
            await message.channel.send(response)

        if message.content == "Hello":
            response = "コードさま! Hello Codyさま, (˶‾᷄ ⁻̫ ‾᷅˵) It is nice to see you."
            await message.channel.send(response)

# ---------------------------------------------------------  Messages if Austin chatting -----------------------------------
    if message.author.id == 228026972494626816:
        if message.content == "hello":
            response = "Hello Uncle, Austono! Nice to see you. (ﾉ☉ヮ⚆)ﾉ ⌒*:･ﾟ✧"
            await message.channel.send(response)
        
        if message.content == "Hello":
            response = "Hello Uncle, Austono! Nice to see you. (ﾉ☉ヮ⚆)ﾉ ⌒*:･ﾟ✧"
            await message.channel.send(response)

# ---------------------------------------------------------  Messages if Ryan chatting -------------------------------------
    if message.author.id == 337011388218343425:
        if message.content == "space marine":
            response = "We march for Macragge!"
            await message.channel.send(response)

    await bot.process_commands(message)

bot.run(TOKEN)
