from AnshikaMusic.core.bot import Anshika
from AnshikaMusic.core.dir import dirr
from AnshikaMusic.core.git import git
from AnshikaMusic.core.userbot import Userbot
from AnshikaMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anshika()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
