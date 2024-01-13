import json
import random
from discord.ext import commands
from discord import File
from easy_pil import Editor, load_image_async, Font


async def is_guidriz(self, bot, guidriz, userr, ctx: commands.Context):
    self.bot = bot
    guidriz = self.bot.get_user(1101197019927826432)
    if userr == guidriz:
      images = ['./users/guidriz.jpg']
            
      with open("./commands/level/levels.json", "r") as f:
          data = json.load(f)
            
      xp = data[str(userr.id)]["xp"]
      lvl = data[str(userr.id)]["level"]
            
      next_lvlup_xp = (lvl+1)*100
      xp_need = next_lvlup_xp
      xp_have = data[str(userr.id)]["xp"]
            
      percentage = int(((xp_have*100)/xp_need))
            
      background = Editor(f"./images/level/{random.choice(images)}")
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
      return

async def is_yesbody(self, bot, yesbody, userr, ctx: commands.Context):
    self.bot = bot
    yesbody = self.bot.get_user(1069286899140792411)
    if userr == yesbody:
      images = ['./users/yesbody.jpg']
            
      with open("./commands/level/levels.json", "r") as f:
          data = json.load(f)
            
      xp = data[str(userr.id)]["xp"]
      lvl = data[str(userr.id)]["level"]
            
      next_lvlup_xp = (lvl+1)*100
      xp_need = next_lvlup_xp
      xp_have = data[str(userr.id)]["xp"]
            
      percentage = int(((xp_have*100)/xp_need))
            
      background = Editor(f"./images/level/{random.choice(images)}")
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
      return

async def is_moguel(self, bot, moguel, userr, ctx: commands.Context):
    self.bot = bot
    moguel = self.bot.get_user(680737419141971977)
    if userr == moguel:
      images = ['./users/moguel.jpg']
            
      with open("./commands/level/levels.json", "r") as f:
          data = json.load(f)
            
      xp = data[str(userr.id)]["xp"]
      lvl = data[str(userr.id)]["level"]
            
      next_lvlup_xp = (lvl+1)*100
      xp_need = next_lvlup_xp
      xp_have = data[str(userr.id)]["xp"]
            
      percentage = int(((xp_have*100)/xp_need))
            
      background = Editor(f"./images/level/{random.choice(images)}")
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
      return

async def is_sky(self, bot, sky, userr, ctx: commands.Context):
    self.bot = bot
    sky = self.bot.get_user(1120072052968267860)
    if userr == sky:
      images = ['./users/sky.jpg']
            
      with open("./commands/level/levels.json", "r") as f:
          data = json.load(f)
            
      xp = data[str(userr.id)]["xp"]
      lvl = data[str(userr.id)]["level"]
            
      next_lvlup_xp = (lvl+1)*100
      xp_need = next_lvlup_xp
      xp_have = data[str(userr.id)]["xp"]
            
      percentage = int(((xp_have*100)/xp_need))
            
      background = Editor(f"./images/level/{random.choice(images)}")
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
      return

async def is_gabexs(self, bot, gabexs, userr, ctx: commands.Context):
    self.bot = bot
    gabexs = self.bot.get_user(1089552095037902949)
    if userr == gabexs:
      images = ['./users/gabexs.jpg']
            
      with open("./commands/level/levels.json", "r") as f:
          data = json.load(f)
            
      xp = data[str(userr.id)]["xp"]
      lvl = data[str(userr.id)]["level"]
            
      next_lvlup_xp = (lvl+1)*100
      xp_need = next_lvlup_xp
      xp_have = data[str(userr.id)]["xp"]
            
      percentage = int(((xp_have*100)/xp_need))
            
      background = Editor(f"./images/level/{random.choice(images)}")
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
      return


def setup(bot):
    pass