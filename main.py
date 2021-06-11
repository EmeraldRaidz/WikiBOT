import discord
import wikipedia
from discord.ext import commands
from token import *

print("ONLINE")
activity = discord.Game(name="Just")


client = commands.Bot(command_prefix='!')
client.remove_command("help")


@client.group(invoke_without_command=True)
async def help(ctx):

    em = discord.Embed(title= "Help", description="Use !help command for extended info")
    em.add_field(name="fun",value="9ac")

    await ctx.send(embed=em)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('!search stuff - Made by ATOM, EmeraldRaidz'))
    print("BOt ready")

@client.command(aliases=["look","wiki","wikipedia"])
async def search(ctx,*,query):
    try:
        query = query.replace("wikipedia", "")
        query = query.replace("search", "")
        query = query.replace("what", "")
        query = query.replace("when", "")
        query = query.replace("where", "")
        query = query.replace("who", "")
        query = query.replace("is", "")
        result = wikipedia.summary(query, sentences=2)

        return_ = str(query)
        ret = return_.upper()
        result_embed = discord.Embed(title=ret,description=result,colour=0x00ff00)
        result_embed.add_field(
            name="Source: ",
            value=f"https://en.wikipedia.org/wiki/{query}",
            inline=False,)

        await ctx.send(embed=result_embed)
        print(result)

    except:
        error_embed = discord.Embed(title="ERROR 109",description="No results found [Make sure it is spelled perfectly] ",colour=0xFF0000)
        error_embed.set_footer(text=f"Query: {query}")
        await ctx.send(embed=error_embed)

# Setting `Playing ` status


client.run(token)


