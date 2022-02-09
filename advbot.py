import discord
from discord import colour
from discord import embeds
from discord.ext import commands
import random
from aiohttp import request
import json
from discord.member import Member
import requests


from discord.flags import alias_flag_value
    

tokenid="ODY3ODEzOTk5MzE5NDQ5NjAw.YPmkxA.77iXB2azezS-rUFd9ItOviKCUws"
client=commands.Bot(command_prefix="!")
ans_list=["Harsh is odin spammer",'offical odin spammer']
@client.command()
async def ping2(ctx):
    await ctx.send("pong")
@client.command(aliases=['ques'])
async def rand(ctx,*,question):
    ans=random.choice(ans_list)
    await ctx.send(ans)
@client.command()
async def catfact(ctx):
    data=requests.get("https://catfact.ninja/fact").json()
    embed=discord.Embed(colour=0x2bc7ff,title=f"Cat Fact",description=f'{data["fact"]} ')
    await ctx.send(embed=embed)
@client.command()
async def dogfact(ctx):
    data=requests.get("https://some-random-api.ml/facts/dog").json()
    embed=discord.Embed(colour=0x2bc7ff,title=f"Dog Fact",description=f'{data["fact"]} ')
    await ctx.send(embed=embed)
@client.command()
async def Tellmejoke(ctx):
    data=requests.get("https://some-random-api.ml/joke").json()
    embed=discord.Embed(colour=0x2bc7ff,title=f"Joke",description=f'{data["joke"]} ')
    await ctx.send(embed=embed)
@client.command()
async def Hug(ctx):
    data=requests.get("https://some-random-api.ml/animu/hug").json()
    embed=discord.Embed(colour=0x2bc7ff,title="Hug",description=f'{data["link"]} ')
    await ctx.send(embed=embed)

@client.command()
async def hug(ctx):
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/animu/hug")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
        embed=discord.Embed(colour=0x2bc7ff,title="Hug",description=f'{content}')
        await ctx.send(content.get("link"))

    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    print(content)
@client.command()    
async def get_meme(ctx):
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/meme")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
        await ctx.send(content.get("image"))
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    print(content)
@client.command()    
async def meme(ctx):
    #making a GET request to the endpoint.
    resp = requests.get("https://reddit-meme-api.herokuapp.com/")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
        await ctx.send(content.get("url"))
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    print(content)
@client.command()    
async def memes(ctx):
    #making a GET request to the endpoint.
    resp = requests.get("https://meme-api.herokuapp.com/gimme")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
        data=requests.get("https://meme-api.herokuapp.com/gimme").json()
        embed=discord.Embed(colour=0x2bc7ff,title=f'{data["title"]} ')
        # await ctx.send(embed=embed)
        #await ctx.send(content.get("url"))
        embed.set_image(url=content.get("url"))
        await ctx.send(embed=embed)
        
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    # print(content)
@client.command()
async def userinfo(ctx,member:discord.Member=None):
    member=ctx.author if not member else member
    embed=discord.Embed(colour=member.color,timestamp=ctx.message.created_at)
    embed.set_author(name=f"User info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)

    embed.add_field(name="Username:" ,value=member.display_name)
    # embed.add_field(name="Created at:" ,value=member.display_name)
    # embed.add_field(name="Username:" ,value=member.display_name)
    embed.add_field(name="ID:" ,value=member.id)
    embed.add_field(name="Bot?:" ,value=member.bot)

    await ctx.send(embed=embed)
@client.command()
async def urband(ctx, *,word):
    data = requests.get(f'https://api.urbandictionary.com/v0/define?term={word}').json()
    defi=data["list"][0]["definition"]
    final=defi.replace("["," ")
    final=final.replace("]"," ")
    word=word.replace("%20"," ")
    embed=discord.Embed(title=f'**{word.capitalize()}**',description=f'{final.capitalize()}',colour=0x2bc7ff)
    embed.set_footer(text="")
    await ctx.send(embed=embed)
@client.command()
async def ud(ctx, *, word):
    data = requests.get(f'https://api.urbandictionary.com/v0/define?term={word}').json()
    mean = data["list"][0]["definition"]
    des = mean.replace("[", " ")
    des = des.replace("]", " ")

    embed = discord.Embed(color=0x2bc7ff, title=f'{word}', description=f'{des.capitalize()}')
    embed.set_footer(text="")
    await ctx.send(embed=embed)
@client.command()
async def trivi(ctx):
    resp = requests.get("https://opentdb.com/api.php?amount=1&type=boolean")
    #checking if resp has a healthy status code.
    if resp.status_code == 200:
        content = resp.json() #We have a dict now.
        mean=content["results"][0]["question"]
        ans=content["results"][0]["correct_answer"]
        embed=discord.Embed(colour=0x2bc7ff,title="Question",description=f'{mean}')
        await ctx.send(embed=embed)
        def check(msg): 
            return msg.author == ctx.author and msg.channel == ctx.channel and \
            msg.content in ["True", "False"]

        msg =await client.wait_for("message", check=check)
        if msg.content == f'{ans}':
            await ctx.send("Correct:white_check_mark:")
        else:
            await ctx.send("Incorrect:x:")
        # await ctx.send(content.get("question"))
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    print(content)
    

client.run(tokenid)