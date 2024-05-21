import discord
from discord.ext import commands
from room_checker import *
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def room_check(ctx):
    await ctx.send("Odanın fotografını yolla!")
    await ctx.send('Algılama başladı!')

    if ctx.message.attachments:
        await ctx.send("Resim bulundu")

        for attachment in ctx.message.attachments:

            file_name = attachment.filename
            file_path = f"images/{file_name}"

            await attachment.save(file_path)
            await ctx.send("Resim kaydedildi")

            class_name,score = room_check("converted_keras\keras_model.h5", file_path, "converted_keras\labels.txt")

            if class_name == "messy room":
                await ctx.send("""Odan malesef temiz değil. Odanızı temizlemek için şunları yapabilirsin:
                                   
                                   -Yerde orada olmaması gereken şeyler gördüğünüzde onları oradan kaldırmaya üşenmeden kaldırmak.
                                   -Yatağınızın kullanmadığınız zamanlarda derli ve toplu olması.
                                   -Kendinizi kirli ve düzensiz değil, düzenli ve tertemiz bir odaya alıştırmak.
                                  
                                  Bu tavsiyelerle sağlığınızı ve odanızı iyileştirebilirsin!""")
            
            elif class_name == "non-messy room":
                await ctx.send("Temizlik konusunda çok iyisin!")

@bot.command()
async def info(ctx):
    await ctx.send("""Düzenli bir odada yaşamanın birçok faydası vardır, bu faydalardan bazıları:
                       -Düzenli bir odada daha rahat konsantre oluruz.
                       -Düzenli bir odada gözümüz daha az yorulur.
                       -Düzenli bir odada daha ferah hissederiz.
                       -Düzenli bir oda sağlığımızı korumamıza yardımcı olur.
                       
                       Düzenli bir oda ile çok daha rahat, temiz ve ferah bir yaşama sahip oluruz.    """)
    
    good_room_list=os.listdir("images")
    img_room=random.choice(good_room_list)
    with open(f"images/{img_room}", "rb") as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def q1(ctx):
    with open(f"images_q\q1.jpg", "rb") as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

    @bot.command()
    async def a1(ctx,answer):
        if answer=="temiz" or "Temiz":
            await ctx.send("Doğru cevap!")
        else:
            await ctx.send("Yanlış cevap!")

@bot.command()
async def q2(ctx):
    with open(f"images_q\q2.jpeg", "rb") as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    
    @bot.command()
    async def a2(ctx,answer):
        if answer=="pis" or "Pis":
            await ctx.send("Doğru cevap!")
        else:
            await ctx.send("Yanlış cevap!")

@bot.command()
async def q3(ctx):
    with open(f"images_q\q3.jpg", "rb") as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    
    @bot.command()
    async def a3(ctx,answer):
        if answer=="pis" or "Pis":
            await ctx.send("Doğru cevap!")
        else:
            await ctx.send("Yanlış cevap!")

@bot.command()
async def q4(ctx):
    with open(f"images_q\q4.jpeg", "rb") as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    
    @bot.command()
    async def a4(ctx,answer):
        if answer=="temiz" or "Temiz":
            await ctx.send("Doğru cevap!")
        else:
            await ctx.send("Yanlış cevap!")

@bot.command()
async def q5(ctx):
    with open(f"images_q\q5.jpeg", "rb") as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    
    @bot.command()
    async def a5(ctx,answer):
        if answer=="temiz" or "Temiz":
            await ctx.send("Doğru cevap!")
        else:
            await ctx.send("Yanlış cevap!")

bot.run("token")