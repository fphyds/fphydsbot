import fphydsbot

TOKEN = 'YOUR TOKEN'
fphydsbot.model.download()
bot = fphydsbot.bot.Bot(TOKEN)
bot.run()
