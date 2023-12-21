import os
import sys

from environs import Env
from pathlib import Path

env = Env()


def get_cfg_path(file: str) -> str:
    if Path(file).is_file():
        return file
    if file == ".env":
        return "/srv/lionschool-bot-dev/.env"
    return "/srv/lionchool-bot/.env.prod"


try:
    if sys.argv[1] == "-d":
        env.read_env(get_cfg_path(".env"), recurse=False)
    elif sys.argv[1] == "-p":
        env.read_env(get_cfg_path(".env.prod"), recurse=False)
    else:
        env.read_env(os.path.join(os.getcwd(), ".env.local"), recurse=False)
except IndexError:
    env.read_env(os.path.join(os.getcwd(), ".env.local"), recurse=False)

# env.read_env()

env_name = env.str("ENV")

# Telegram
api_token = env.str("API_TOKEN")
# admin_ids = env.list("ADMIN_IDS")  # TODO: add
admin_id = env.str("ADMIN_ID")
