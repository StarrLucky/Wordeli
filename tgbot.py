import getopt
import logging
import sys
from telegram import Update, ForceReply, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
import wordeli 
import stardict

logger = logging.getLogger(__name__)
    
wordeli = wordeli.dict('wordeli_dict/dict.txt', "wordeli_dict/dictused.txt", "wordeli_dict/base.txt")


# Store bot screaming status
screaming = False

# Pre-assign menu text
FIRST_MENU = "New One?"

# Pre-assign button text
NEXT_BUTTON = "Next"

# Build keyboards
FIRST_MENU_MARKUP = InlineKeyboardMarkup([[
    InlineKeyboardButton(NEXT_BUTTON, callback_data=NEXT_BUTTON)
]])

def echo(update: Update, context: CallbackContext) -> None:
    # Print to console
    print(f'{update.message.from_user.first_name} wrote {update.message.text}')
    
    context.bot.send_message(
            update.message.chat_id,
            # wordeli.nxt(),
            stardict.getFromDict(),
            # To preserve the markdown, we attach entities (bold, italic...)
            entities=update.message.entities
        )


def scream(update: Update, context: CallbackContext) -> None:
    """
    This function handles the /scream command
    """

    global screaming
    screaming = True


def next(update: Update, context: CallbackContext) -> None:
   
    context.bot.send_message(
        update.message.chat_id,
        # wordeli.nxt(),
        stardict.getFromDict(),
        entities=update.message.entities
    )
   


def menu(update: Update, context: CallbackContext) -> None:
    """
    This handler sends a menu with the inline buttons we pre-assigned above
    """

    context.bot.send_message(
        update.message.from_user.id,
        FIRST_MENU,
        parse_mode=ParseMode.HTML,
        reply_markup=FIRST_MENU_MARKUP
    )


def button_tap(update: Update, context: CallbackContext) -> None:
    """
    This handler processes the inline buttons on the menu
    """

    data = update.callback_query.data
    text = ''
    markup = None

    if data == NEXT_BUTTON:
        text = FIRST_MENU
        markup = FIRST_MENU_MARKUP

    # Close the query to end the client-side loading animation
    update.callback_query.answer('')

    # Update message content with corresponding menu section
    update.callback_query.message.edit_text(
        text,
        ParseMode.HTML,
        reply_markup=markup
    )


def main() -> None:

    if len(sys.argv) > 1:
        token = sys.argv[1]
    else: 
        print("No bot token supplied")
        return 
    
    
    updater = Updater(token)

    # Get the dispatcher to register handlers
    # Then, we register each handler and the conditions the update must meet to trigger it
    dispatcher = updater.dispatcher

    # Register commands
    # dispatcher.add_handler(CommandHandler("shemdegi", scream))
    dispatcher.add_handler(CommandHandler("next", next))
    dispatcher.add_handler(CommandHandler("menu", menu))

    # Register handler for inline buttons
    # dispatcher.add_handler(CallbackQueryHandler(button_tap))

    # Echo any message that is not a command
    dispatcher.add_handler(MessageHandler(~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
    