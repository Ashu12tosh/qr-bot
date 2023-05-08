import discord
import qrcode

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!qr'):
        text = message.content[4:].strip()
        if not text:
            await message.channel.send('Please enter some text to generate QR code!')
            return
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save('qr.png')
        await message.channel.send(file=discord.File('qr.png'))

client.run('YOUR_DISCORD_BOT_TOKEN_HERE')
