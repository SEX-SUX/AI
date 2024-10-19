import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7476540645:AAHjMhqy2vf6KBB-BBoZWZMRIjYoo2EPyCA")
API_ID = int(os.environ.get("API_ID", "28795512"))
API_HASH = os.environ.get("API_HASH", "c17e4eb6d994c9892b8a8b6bfea4042a")
PICS = os.environ.get("PICS", "https://files.catbox.moe/jutcs7.jpg").split()
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7373125778').split()]
DB_URL = os.environ.get("DB_URL", "postgres://iarfggbc:Vxzh_kG7cxa1kHR5faxcd1kuA4R-UT9E@rosie.db.elephantsql.com/iarfggbc")
DB_NAME = os.environ.get("DB_NAME", "sachin")
RemoveBG_API = os.environ.get("RemoveBG_API", "MMLEH3kH6opgSxfx7SBvqtY5")
IBB_API = os.environ.get("IBB_API", "6a143a9c8a4ed86c483de7c239ab5990")
FORCE_SUB = os.environ.get("FORCE_SUB", "All_SANATANI_BOT")
PORT = os.environ.get('PORT', '8080')          
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002460342691'))
LOG_TEXT = """<i><u>👁️‍🗨️USER DETAILS</u>

○ ID : <code>{id}</code>
○ DC : <code>{dc_id}</code>
○ First Name : <code>{first_name}<code>
○ UserName : @{username}

By = {bot}</i>"""
