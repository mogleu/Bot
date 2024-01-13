import discord
import json
import random
from discord import File
from discord.ext import commands
from discord import Option
from easy_pil import Editor, load_image_async, Font

# Custom Backgrounds
from commands.level.custom_backgrounds import is_guidriz
from commands.level.custom_backgrounds import is_yesbody
from commands.level.custom_backgrounds import is_moguel
from commands.level.custom_backgrounds import is_sky
from commands.level.custom_backgrounds import is_gabexs
# End Custom Backgrounds

class Levelsys(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
  
    @commands.Cog.listener()
    async def on_message(self, message):
  
      #the bot's prefix is ? that's why we are adding this statement so user's xp doesn't increase when they use any commands
      if not message.content.startswith("."):
  
        #checking if the bot has not sent the message
        if not message.author.bot:
          with open("./commands/level/levels.json", "r") as f:
            data = json.load(f)
          
          #checking if the user's data is already there in the file or not
          if str(message.author.id) in data:
            xp = data[str(message.author.id)]['xp']
            lvl = data[str(message.author.id)]['level']
  
            #increase the xp by the number which has 100 as its multiple
            increased_xp = xp+10
            new_level = int(increased_xp/200)
  
            data[str(message.author.id)]['xp']=increased_xp
  
            with open("./commands/level/levels.json", "w") as f:
              json.dump(data, f)
  
            if new_level > lvl:
              await message.channel.send(f"Parabéns! {message.author.mention} acabou de subir para o nível {new_level}!")
  
              data[str(message.author.id)]['level']=new_level
              data[str(message.author.id)]['xp']=0
  
              with open("./commands/level/levels.json", "w") as f:
                json.dump(data, f)
              
          else:
            data[str(message.author.id)] = {}
            data[str(message.author.id)]['xp'] = 0
            data[str(message.author.id)]['level'] = 1
  
            with open("./commands/level/levels.json", "w") as f:
              json.dump(data, f)
              

    @commands.slash_command(name="level", description="Manda informações do level de um membro.")
    async def level(self, ctx: commands.Context, membro: Option(discord.Member, description="O membro a ter as informações enviadas", required=False)):
        await ctx.defer()
        try:
            userr = membro or ctx.author
          
            yesbody = self.bot.get_user(1069286899140792411)            
            if userr == yesbody:
                await is_yesbody(self=self, bot=self.bot, yesbody=yesbody, userr=userr, ctx=ctx)
                return

            moguel = self.bot.get_user(680737419141971977)
            if userr == moguel:
                await is_moguel(self=self, bot=self.bot, moguel=moguel, userr=userr, ctx=ctx)
                return

            sky = self.bot.get_user(1120072052968267860)
            if userr == sky:
                await is_sky(self=self, bot=self.bot, sky=sky, userr=userr, ctx=ctx)
                return

            gabexs = self.bot.get_user(1089552095037902949)
            if userr == gabexs:
                await is_gabexs(self=self, bot=self.bot, gabexs=gabexs, userr=userr, ctx=ctx)
                return

            guidriz = self.bot.get_user(1101197019927826432)
            if userr == guidriz:
                await is_guidriz(self=self, bot=self.bot, guidriz=guidriz, userr=userr, ctx=ctx)
                return
                
            
            images = ['zIMAGE.png', 'telephone.jpg', 'buildings.jpg', 'city_cathedral.jpg', 'trees.jpg', 'forest.jpg', 'city_blur.jpg', 'bridge.jpg', 'sea.jpg', 'city.jpg', 'forest_trees.jpg', 'mountain.jpg']
        
            with open("./commands/level/levels.json", "r") as f:
                data = json.load(f)
        
            xp = data[str(userr.id)]["xp"]
            lvl = data[str(userr.id)]["level"]
        
            next_lvlup_xp = (lvl+1)*100
            xp_need = next_lvlup_xp
            xp_have = data[str(userr.id)]["xp"]
        
            percentage = int(((xp_have*100)/xp_need))
        
            background = Editor(f"./images/level/default/{random.choice(images)}")
            profile = await load_image_async(str(userr.display_avatar))
        
            profile = Editor(profile).resize((150, 150)).circle_image()
        
            poppins = Font.poppins(size=40)
            poppins_small = Font.poppins(size=30)
        
            ima = Editor("./images/level/zBLACK.png")
            background.blend(image=ima, alpha=.5, on_top=False)
        
            background.paste(profile.image, (30, 30))
        
            background.rectangle((30, 220), width=650, height=40, fill="#fff", radius=20)
            background.bar(
                (30, 220),
                max_width=650,
                height=40,
                percentage=percentage,
                fill="#ff9933",
                radius=20
            )
            background.text((200, 40), str(userr.name), font=poppins, color="#ff9933")
        
            background.rectangle((200, 100), width=350, height=2, fill="#ff9933")
            background.text(
                (200, 130),
                f"Level : {lvl} "
                + f"XP : {xp} / {(lvl+1)*100}",
                font=poppins_small,
                color="#ff9933"
            )
        
            card = File(fp=background.image_bytes, filename="./images/level/zCARD.png")
            await ctx.edit(file=card)
        except KeyError:
            await ctx.edit(content="Você **//** Este membro não tem uma conta, você **//** ele precisa mandar uma mensagem para eu criar uma conta para ele!")


class Rank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
  
    @commands.slash_command(name="rank", description="Manda o ranking de membros do servidor.")
    async def rank(self, ctx):
        await ctx.defer()
        range_num = 5
        with open("./commands/level/levels.json", "r") as f:
            data = json.load(f)
            
        l = {}
        total_xp = []

        for userid in data:
            xp = int(data[str(userid)]['xp']+(int(data[str(userid)]['level'])*100))

            l[xp] = f"{userid};{data[str(userid)]['level']};{data[str(userid)]['xp']}"
            total_xp.append(xp)
            
        total_xp = sorted(total_xp, reverse=True)
        index = 1

        mbed = discord.Embed(
            title="Ranking",
            color=discord.Color.blurple()
        )

        for amt in total_xp:
            id_ = int(str(l[amt]).split(";")[0])
            level = int(str(l[amt]).split(";")[1])
            xp = int(str(l[amt]).split(";")[2])

            member = await self.bot.fetch_user(id_)

            if member is not None:
                name = member.name
                mbed.add_field(name=f"{index}. {name}",
                value=f"**Level: {level} | XP: {xp}**",
                inline=False)

                if index == range_num:
                    break
                else:
                    index += 1

        await ctx.edit(embed=mbed)


def setup(bot):
    bot.add_cog(Levelsys(bot))
    bot.add_cog(Rank(bot))