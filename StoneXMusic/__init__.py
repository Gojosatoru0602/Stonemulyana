
from SafoneAPI import SafoneAPI
import config
import random
from StoneXmusic.core.bot import Stone
from StoneXmusic.core.dir import dirr
from StoneXmusic.core.git import git
from StoneXmusic.core.userbot import Userbot
from StoneXmusic.misc import dbb, heroku

from .logging import LOGGER

HEYEMOJI = ["PPLAY_1",
            "PPLAY_2",
            "PPLAY_3",
            "PPLAY_4",
            "PPLAY_5",
            "PPLAY_6",
            "PPLAY_7",
            "PPLAY_8",
            "PPLAY_9",
            "PPLAY_10",
            "PPLAY_11",
            "PPLAY_12",
            "PPLAY_13",
            "PPLAY_14",
            "PPLAY_15",
            "PPLAY_16",
            "PPLAY_17"]

dirr()
git()
dbb()
heroku()

app = Stone()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()