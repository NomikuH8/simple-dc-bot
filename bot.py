from discord.ext import commands
import json
import os

TOKEN = open('dc-token.txt', 'r').read()
configs = json.loads(open('dc-cfg.json', 'r').read())
prefix = configs['prefix']
comms = configs['commands']

bot = commands.Bot(command_prefix=prefix)

for i in comms.keys():
    @bot.command(name=i, help=comms[i]['help'])
    async def comm(ctx):
        resp = comms[i]['resp']
        await ctx.send(resp)

bot.run(TOKEN)
