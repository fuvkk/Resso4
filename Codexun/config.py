## Disclaimer By Team Codexun

## Don't try to edit this file otherwise your bot will be crash.

from os import getenv

from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
get_queue = {}
SESSION_NAME = getenv("SESSION_NAME", "BQA78jgwOEwSxKoAtm2CqQxPHSNSzV-_8x03hpVSCfRxOJNFoc0CIe2xuwzao5Awgudit72iBDqRr6WnxH8QKSS-NJur6BryIwo52z7CaFTdSjtweIMAjLYDXUacGucN_5h1zQLfx88XIwMS-RlrivxvLqgcxx3vVTNNq3VjXBmTB4fF9_OcdrVtk9kYPyX_lRnlEox2Dx0bOhLPzIE8rCd7qAnoqBu3d9jKSep1x3bHkR8ICQKaDE353DYvDjZgTQH7Vw-Y3OAi2mYUH-GLw7rM5DBucerUIRajQ61XBmuTozaxtlDdTwvgwHs84VB8ohrc_SrPEmwJenaZyL70jRjeAAAAAUQujzgA")
BOT_TOKEN = getenv("BOT_TOKEN", "2031768448:AAFOKiCJMnyRd9X2GppHbJgKrcxrZ1VJJng")
BOT_NAME = getenv("BOT_NAME", "Broken Music")
BOT_USERNAME = getenv("BOT_USERNAME", "crepanrobot")
ASSID = int(getenv("ASSID", "5438869304"))
ASSNAME = getenv("ASSNAME", "Broken Assistant")
ASSUSERNAME = getenv("ASSUSERNAME", "BrokenMusicAs")
BOT_ID = int(getenv("BOT_ID", "2031768448"))
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
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/d9c07e35a85d5e869dad6.jpg")
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
