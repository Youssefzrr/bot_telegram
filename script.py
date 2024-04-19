from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Define the menu options with corresponding file paths
options = {
    "App Name 1": "/home/your_username/apps/app1_file.zip",
    "App Name 2": "/home/your_username/apps/app2_file.zip",
    "App Name 3": "/home/your_username/apps/app3_file.zip"
    # Add more choices and corresponding file paths as needed
}

# Function to display the menu with inline keyboard buttons
def start(update: Update, context: CallbackContext):
    keyboard = []
    for option_name, _ in options.items():
        keyboard.append([InlineKeyboardButton(option_name, callback_data=option_name)])
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Choose an app:", reply_markup=reply_markup)

# Function to handle button clicks and send the corresponding file
def button_click(update: Update, context: CallbackContext):
    query = update.callback_query
    selected_option = query.data
    file_path = options.get(selected_option)
    if file_path:
        query.message.reply_document(document=open(file_path, 'rb'))
    else:
        query.message.reply_text("Invalid choice. File path not found.")

def main():
    updater = Updater("Telegram Token", use_context=True)  # Replace "YOUR_BOT_TOKEN" with your actual token
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button_click))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
