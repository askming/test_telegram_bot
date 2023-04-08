import telegram
from github import Github
from github import InputFileContent

# Initialize the Telegram bot
bot = telegram.Bot('6128791021:AAEFtYY4wdTaqSIUG6COiYUUv74RLsSQu8k')

# Initialize the GitHub client
g = Github('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')

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
