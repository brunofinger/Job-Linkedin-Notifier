
# LinkedIn Job Notifier

This is a Python script that uses the LinkedIn and Telegram APIs to notify when new job openings are posted on LinkedIn. The script searches for job openings based on a company name and location, and sends a message to a Telegram bot if a new opening is found.

## Summary

The LinkedIn Job Notifier is a Python script that uses the LinkedIn and Telegram APIs to notify when new job openings are posted on LinkedIn. The script searches for job openings based on a company name and location, and sends a message to a Telegram bot if a new opening is found. The script uses the `python-linkedin` library to authenticate with the LinkedIn API and search for job openings, and the `python-telegram-bot` library to send notifications to a Telegram bot. The script is configured using environment variables, and runs in an infinite loop that waits an hour between each search for new job openings.

## How to Use

1.  Clone the repository:
  
    
    `git clone https://github.com/brunofinger/Job-Linkedin-Notifier.git
    cd Job-Linkedin-Notifier` 
    
2.  Install the required packages:
    
    
    `pip install -r requirements.txt` 
    
3.  Set the required environment variables:
    
    
    `export LINKEDIN_API_KEY=<your_api_key>
    export LINKEDIN_API_SECRET=<your_api_secret>
    export LINKEDIN_ACCESS_TOKEN=<your_access_token>
    export TELEGRAM_BOT_TOKEN=<your_bot_token>
    export TELEGRAM_CHAT_ID=<your_chat_id>` 
    
    -   `LINKEDIN_API_KEY`: the API key for your LinkedIn app
    -   `LINKEDIN_API_SECRET`: the API secret for your LinkedIn app
    -   `LINKEDIN_ACCESS_TOKEN`: the access token for your LinkedIn app
    -   `TELEGRAM_BOT_TOKEN`: the token for your Telegram bot
    -   `TELEGRAM_CHAT_ID`: the chat ID for your Telegram bot
4.  Run the script:
    
    `python notifier.py` 
    

## How It Works

The script uses the `python-linkedin` library to authenticate with the LinkedIn API and search for job openings. It also uses the `python-telegram-bot` library to send notifications to a Telegram bot.

The script defines a `LinkedInJobNotifier` class that encapsulates the LinkedIn and Telegram functionality. The class has the following methods:

-   `__init__`: initializes the class and sets up the LinkedIn and Telegram clients
-   `run`: runs the main loop that searches for job openings and sends notifications to Telegram
-   `search_jobs`: searches for job openings based on a company name and location
-   `send_notification`: sends a notification message to a Telegram bot

The `run` method runs in an infinite loop that waits an hour between each search for new job openings. When a new job opening is found, the `send_notification` method is called to send a message to the specified Telegram chat.

