import logging
import keys
import json

from Services.GooglePlaces import nearyby_search
from Services.ResultParser import parse_results
from Services.generator import generate_URL_from_place_id
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

# Enable logging and writing to a log file
logging.basicConfig(
    filename="../log.txt",
    filemode='a',

    format=u'%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)
logging.getLogger().addHandler(logging.StreamHandler())

PREFERENCE, LOCATION = range(2)


def start(update: Update, context: CallbackContext) -> int:

    update.message.reply_text(
        'Hi! I will do my best to recommend a place to eat. '
        'Send /start to start from the top or /cancel to stop.\n\n'
        'Firstly, send me your location please',
    )
    user = update.message.from_user
    logger.info(f'Preference of {user.first_name}: {update.message.text}')

    return LOCATION


def location(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    user_location = update.message.location
    logger.info(
        "Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude
    )
    location = f'{user_location.latitude},{user_location.longitude}'
    result_list = nearyby_search(location, {})
    logger.info(u'\n'.join(json.dumps(d) for d in result_list))
    update.message.reply_text(
        'Querying google places api...'
    )
    sorted_places = parse_results(result_list)

    first_place = sorted_places[0]
    url = generate_URL_from_place_id(first_place.get('place_id'))
    update.message.reply_text(
        f'Check out {first_place.get("name")}! \n'
        f'It has a rating of {first_place.get("rating")} and it is located at {first_place.get("vicinity")}\n'
        f'Here is the URL: {url}\n'
    )
    return ConversationHandler.END


def skip_location(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s did not send a location.", user.first_name)
    update.message.reply_text(
        'You have to send location for recommendations!'
    )

    return ConversationHandler.END


def preference(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("Preference of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Send me your location please')

    return LOCATION


def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    TOKEN = keys.TOKEN
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add handler with the states PREFERENCE, REVIEWED, POPULAR and LOCATION
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            PREFERENCE: [MessageHandler(Filters.text & ~Filters.command, preference)],
            LOCATION: [
                MessageHandler(Filters.location, location),
                CommandHandler('skip', skip_location),
            ],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()