import config
import logging
import sys

from aiogram import Dispatcher
from aiogram.types import AllowedUpdates
from aiogram.utils import executor
from utils.set_bot_commands import set_default_commands

logger = logging.getLogger(__name__)


async def startup(dp: Dispatcher):
    msg = f'Bot started in {config.env_name} mode'
    logger.info(msg)
    await set_default_commands(dp)


async def shutdown(dp: Dispatcher):
    msg = f'Bot stopped in {config.env_name} mode'
    logger.info(msg)
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    try:
        if sys.argv[1] not in ["-p", "-d", "-l"]:
            raise Exception
    except IndexError:
        logger.error("Argument -d (dev), -l (local) or -p (prod) should be provided")
        sys.exit(1)
    from handlers import dp

    executor.start_polling(dp, on_startup=startup, on_shutdown=shutdown,
                           allowed_updates=AllowedUpdates.all())
