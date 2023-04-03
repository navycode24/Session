

from ast import parse
from pyrogram import (
    Client,
    __version__,
    enums
)
from bot import LOGGER
from config import (
    API_HASH,
    APP_ID,
    TG_BOT_WORKERS
)


class User(Client):
    """ modded client for SessionMakerUser """

    def __init__(self):
        super().__init__(
            name="tu",
            api_hash=API_HASH,
            api_id=APP_ID,
            workers=TG_BOT_WORKERS,
            in_memory=True,
            parse_mode=enums.ParseMode.HTML
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} based on Pyrogram v{__version__} "
        )
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
