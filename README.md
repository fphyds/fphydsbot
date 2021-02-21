# X5School Python Project - fphydsbot

This telegram bot @fhydsbot can detect human's faces, determine genders and ages by photo. All you need is just send your photo to bot and wait for the result.

## Examples
![example](https://gitlab.com/Zavyalov1/fphydsbot/-/blob/master/IMG_2685.png)


## How to install

```bash
python3 setup.py install
```

## How to run the bot

```python
# simple usage
import fphydsbot

TOKEN = 'YOUR TOKEN'
fphydsbot.model.download()
bot = fphydsbot.bot.Bot(TOKEN)
bot.run()
```



