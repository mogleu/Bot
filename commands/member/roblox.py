import discord
import json
import requests
from discord.ext import commands
from discord import Option


class Roblox(commands.Cog):
    roblox = discord.SlashCommandGroup(name="roblox")

    @roblox.command(name="user", description="Fornece informações sobre um usuário do Roblox.")
    # IGNORE THIS SYNTAX ERROR, IT'S THE DESCRIPTION FOR THE OPTION
    # IGNORE THIS SYNTAX ERROR, IT'S THE DESCRIPTION FOR THE OPTION
    # IGNORE THIS SYNTAX ERROR, IT'S THE DESCRIPTION FOR THE OPTION
    # IGNORE THIS SYNTAX ERROR, IT'S THE DESCRIPTION FOR THE OPTION
    async def user(self, interaction: discord.Interaction, username: Option(description="O username do usuário do Roblox.")):
        await interaction.response.defer()
    
        users_json = requests.get(f"https://www.roblox.com/search/users/results?keyword={username}&maxRows=1&startIndex=0")
        users = json.loads(users_json.text)
        user_id = users['UserSearchResults'][0]['UserId']
    
    
    
        profile_json = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
        profile = json.loads(profile_json.text)
        display_name = profile["displayName"]
        description = profile["description"]
    
        thumbnail_json = requests.get(f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={user_id}&size=100x100&format=Png&isCircular=false")
        thumbnail = json.loads(thumbnail_json.text)
        thumbnail_url = thumbnail['data'][0]['imageUrl']
    
        embed = discord.Embed(title=f"{username}", url=f"https://www.roblox.com/users/{user_id}/profile", color=0x00b3ff)

        if description == "":
            description = "Nenhuma descrição"
    
        embed.add_field(name="ID", value=f"`{user_id}`", inline=True)
        embed.add_field(name="Display Name", value=f"`{display_name}`", inline=True)
        embed.add_field(name="Descrição", value=f"`{description}`", inline=False)
        embed.set_thumbnail(url=f"{thumbnail_url}")
        await interaction.followup.send(embed=embed)


def setup(bot):
    bot.add_cog(Roblox())