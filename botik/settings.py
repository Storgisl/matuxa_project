from os import environ
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Bots:
    bot_token: str
    admin_id: int

@dataclass
class Settings:
    bots: Bots

def get_settings(path: str): 
    bot_token = environ.get("TOKEN")
    admin_id = int(environ.get("ADMIN_ID"))
    return Settings(
        bots=Bots(bot_token=bot_token,
                admin_id=admin_id
            )
        )
settings = get_settings(".env")
print(settings)