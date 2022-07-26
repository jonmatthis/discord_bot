# main_bot.py
# originally based on this tutorial - https://realpython.com/how-to-make-a-discord-bot-python/
import os
import random
from typing import Union

import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

print('creating bot')
bot = commands.Bot(command_prefix='$')

@bot.command(name='99', help= "Reponds with randome Brooklyn 99 quote")
async def nine_nine(context):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await context.send(response)

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(context, channel_name='new-channel'):
    guild = context.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if existing_channel:
        await context.send(f"there is already a channel named: {channel_name}")
    else:
        await context.send(f"creating channel: {channel_name}")
        print(f"Creating new channel: {channel_name}")
        await guild.create_text_channel(channel_name)


@bot.command(name='convert-temperature')
async def create_channel(context, degrees: Union[int,float], temperature_units: str):
    """
    convert temperatures from Celsius to Fahrenheit
    input should come int he form `$ [integer or float temperature] [either 'c' for celsius or 'f' for Fahrenheit]

    e.g. `$ 15 C` to convert 15 degrees celsius to fahrenheit
    """

    #convert input string to lower case and pull out the first character
    temperature_units = temperature_units.lower()
    temperature_units = temperature_units[0]

    if temperature_units == 'c':
        converted_temp = (degrees * (9/5)) + 32
        await context.send(f"{degrees} in Celsius is {converted_temp} in Fahrenheit")
    elif temperature_units == 'f':
        converted_temp = (degrees - 32) * (5/9)
        await context.send(f"{degrees} in Fahrenheit is {converted_temp} in Celsius")
    else:
        await context.send(f"temperture units {temperature_units} not recognized, please input in units `C`, `Celsius`, `F`, or `Fahrenheit`")


print(f'running with TOKEN for server: {GUILD}')
bot.run(TOKEN)
