import telegram
from github import Github
from github import InputFileContent
from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
GITHUB_PERSONAL_ACCESS_TOKEN = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
# Initialize the Telegram bot
bot = telegram.Bot(TELEGRAM_API_TOKEN)

# Initialize the GitHub client
g = Github(GITHUB_PERSONAL_ACCESS_TOKEN)

# Define the repository and file information
repo_name = 'test_telegram_bot'
file_name = 'article.md'

# Listen for messages sent to the bot
def handle_message(update, context):
    # Extract the text from the message
    text = update.message.text

    # Save the article to a file on your local machine
    with open(file_name, 'w') as f:
        f.write(text)

    # Create a new commit to the repository with the article file
    repo = g.get_repo(repo_name)
    contents = InputFileContent(content=text)
    repo.create_file(file_name, 'Committing new article', contents)

    # Respond to the user in Telegram
    update.message.reply_text('Article saved to GitHub!')

# Start the bot and listen for messages
updater = telegram.ext.Updater('YOUR_TELEGRAM_API_TOKEN', use_context=True)
updater.dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()
