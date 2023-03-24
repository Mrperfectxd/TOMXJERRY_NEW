import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from Romeo import LOGGER, app, userbot
from Romeo.core.call import rj
from Romeo.plugins import ALL_MODULES
from Romeo.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("Romeo").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("Romeo").warning(
            "Spotify Client Id & Secret not add."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Romeo.plugins" + all_module)
    LOGGER("Romeo.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await rj.start()
 #   try:
  #      await rj.stream_call(
  #          "https://telegra.ph/file/8d5db123638c2f6bb6ce4.mp4"
  #      )
  #  except NoActiveGroupCall:
   #     LOGGER("Romeo").error(
    #        "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group. If you ever ended voice chat in log group i will stop."
    #    )
   #     sys.exit()
 #   except:
 #       pass
    await rj.decorators()
    LOGGER("Romeo").info("Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Romeo").info("Stopping Music Bot")
