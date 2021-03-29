import logging
from Services import TelegramBot

logging.basicConfig(level=logging.DEBUG)

logging.debug('Starting Telegram Bot service')

TelegramBot.main()

logging.info('Exit Main')

