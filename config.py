from os import getenv


API_ID = int(getenv("API_ID", "18618422"))
API_HASH = getenv("API_HASH", "f165b1caec3cfa4df943fe1cbe82d22a")
BOT_TOKEN = getenv("BOT_TOKEN", "6331627404:AAFmXuPUywE0aXxBPrL6rEToysrIGZwrQmU")
OWNER_ID = int(getenv("OWNER_ID", "6050277919"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6050277919 2112898623").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://mohitag24082006:ge3z5sQOsr6NiTTt@cluster0.xxrppe5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002099606627"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002104143278"))


