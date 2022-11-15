##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()
get_queue = {}
SESSION_NAME = getenv('SESSION_NAME', 'BQBvt9k5eJzQemumFqB3T-gHEjUulet39UyuYAdwvP9mfQTwg-wzWAFtHHHDo8wQysXbBh3MQ0wrf5u6brIbRCP7aFpkPDUw6iIiGbAcuQgIbcTt0XDDXR7kv7_m-qF6V6uAE-7EMn4MJ-WhAZ3Zr1XT-RBbZxEesJEL_Ms2oFMPxZx8WFALiyIfd17pGSIUucJEf6IPqHSGUiGUxM4RAbyiG8oHauQT1TYB4Ah_Kcfsv_zHBF50E-B2zLrHLd_LgWTeaWiX63HoOxhI41djSPCleWiu2Ksy609jPYMdwYqXZpHh0SGfnqkB6l3ox2QeklgfCK66uV6MpObmstgvdUKCezVv_wA')
BOT_TOKEN = getenv('5051175427:AAEIJdwr1PMWBm6A6x0I09DBC_DdRRP4JjA')
API_ID = getenv('16179045')
API_HASH = getenv('dc99c86a0b38365fd6c8b35ae9c577b9')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '3600'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ . , : ; ! ?').split())
MONGO_DB_URI = getenv("mongodb+srv://al:achil234@al.odhu4.mongodb.net/?retryWrites=true&w=majority")
OWNER = list(map(int, getenv('OWNER', '1441342342').split()))
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '1441342342').split()))
LOG_GROUP_ID = getenv("-1001835456207")
ASS_ID = int(getenv("ASS_ID", '2067099647'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '1441342342').split()))
GROUP = getenv("GROUP", 'ruangdiskusikami')
CHANNEL = getenv("CHANNEL", 'ruangprojects')
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/arsyabot/Music2")
AUTO_LEAVE = int(getenv("AUTO_LEAVE", "1500"))
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
OWNER_ID.append(1663258664)
OWNER_ID.append(1607338903)
