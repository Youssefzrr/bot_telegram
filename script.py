from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    menu = "Choose an app:\n1. App Name 1\n2. App Name 2\n3. App Name 3"  # Customize with your app names
    update.message.reply_text(menu)

def get_file_path_for_choice(choice):
    # Define a mapping of choices to file paths
    file_paths = {
        1: '/home/itskaido/apps/flights.csv',
        2: '/path/to/app2_file.zip',
        3: '/path/to/app3_file.zip'
        # Add more choices and corresponding file paths as needed
    }

    # Check if the choice exists in the mapping
    if choice in file_paths:
        return file_paths[choice]
    else:
        return None  # Return None if choice is not found (optional: handle this case in your code)

def send_file(update: Update, context: CallbackContext):
    choice = int(update.message.text)
    # Logic to determine which file to send based on the user's choice
    file_path = get_file_path_for_choice(choice)  # Implement this function
    if file_path:
        update.message.reply_document(document=open(file_path, 'rb'))
    else:
        update.message.reply_text("Invalid choice. File path not found.")

def main():
    updater = Updater("YOUR_BOT_TOKEN", use_context=True, update_queue=None)  # Replace "YOUR_BOT_TOKEN" with your actual token
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("send", send_file))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
