import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

# This dictionary will store the text for each member
member_text = {}

@bot.command(name='bob')
async def bob(ctx, uid=None, *, text=None):
    if uid is None:
        await ctx.send('Please provide a user ID.')
        return
    if text is None:
        if uid not in member_text:
            await ctx.send(f"No text found for user with ID {uid}.")
        else:
            await ctx.send(f"Text for user with ID {uid}: {member_text[uid]}")
    else:
        try:
            member = await commands.MemberConverter().convert(ctx, uid)
        except commands.errors.MemberNotFound:
            await ctx.send(f"No user found with ID {uid}.")
            return
        member_text[str(member.id)] = text
        await ctx.send(f"Saved text for {member.mention}")

bot.run('MTA4NjY3NTk1NjkzNDExNTM3MA.Gn8fuU.q_YCxID-JlV0G86ja_NzBnfF37v54VR1QXtTJ0')
