## Disclaimer By Team Codexun

## Don't try to edit this file otherwise your bot will be crash.

from os import getenv

from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
get_queue = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCDJUGiSNHF9PTtNO2yaH1xfrPhU_u-Ji2u6wdwO3CyC3tlK8m6cMwpPL2OtMSONGC09zUReDBNV1Qsj5-XjMHiWJtWGyV8wiQ9k39MtqDZzM6RarTlqPVGNZmkZqH7NfH5d20yZdJQE9iIZkqI4kH6ILgxtiqoEA7NxFdJ-1UUKfAx1-w3PoowSCCXujPY4VCmYOemWNhRNe__Okf8fuozrcmkmqG83_8q0CEEU401iO6eFmjjSHNs7NFPG5-JuEPK0eM92E67xC5GV8D7hRid2f7xsfuMVeeI3WS3mrqXqzVly8H0KlTVqaydlhMBaPxip5_uWeu1v5K2_ANDH87mAAAAATCfhggA")
BOT_TOKEN = getenv("BOT_TOKEN", "5181191526:AAFIpXJ02QuCokSoidAeGMp9pYzAf_NrdmA")
BOT_NAME = getenv("BOT_NAME", "Resso Music")
BOT_USERNAME = getenv("BOT_USERNAME", "ressomusicbot")
ASSID = int(getenv("ASSID", "5110728200"))
ASSNAME = getenv("ASSNAME", "Resso Assistant")
ASSUSERNAME = getenv("ASSUSERNAME", "RessoMusicAss")
BOT_ID = int(getenv("BOT_ID", "5181191526"))
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/PavanMagar/CodexunMusicBot")
USERS = getenv("2056407064")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://codexun:TeamCodexun07@codexun.egmx5.mongodb.net/?retryWrites=true&w=majority")
API_ID = int(getenv("API_ID", "19358756"))
API_HASH = getenv("API_HASH", "08453a01e0c443ee6a3472538f2a6f02")
OWNER_ID = int(getenv("OWNER_ID", "2056407064"))
UPDATE = getenv("UPDATE", "codexun")
LOG_CHANNEL = int(getenv("LOG_CHANNEL", "-1001505526419"))
SUPPORT = getenv("SUPPORT", "TeamCodexun")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/4d2838aac3120b0e04ce7.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))
CMD_MUSIC = list(getenv("CMD_MUSIC", "/ !").split())
BG_IMG = getenv("BG_IMG", "https://telegra.ph/file/f2a2d31f60a9e0f3dbe94.png")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2056407064").split()))
ASSISTANT_NAME = getenv("ASSNAME", "Broken Assistant")
COMMAND_PREFIXES = ("/ ! .").split()
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/a085a3cea21f994264152.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
