import os
import time
import requests
from linkedin import linkedin
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()


class LinkedInJobNotifier:
    def __init__(self, linkedin_api_key, linkedin_api_secret, linkedin_access_token, telegram_bot_token, telegram_chat_id):
        self.linkedin_api_key = linkedin_api_key
        self.linkedin_api_secret = linkedin_api_secret
        self.linkedin_access_token = linkedin_access_token
        self.telegram_bot_token = telegram_bot_token
        self.telegram_chat_id = telegram_chat_id
        self.auth = linkedin.LinkedInAuthentication(
            self.linkedin_api_key,
            self.linkedin_api_secret,
            'https://www.example.com/auth/callback',
            linkedin.PERMISSIONS.enums.values()
        )
        self.auth.set_access_token(self.linkedin_access_token)
        self.client = linkedin.LinkedInApplication(self.auth)
        self.bot = Bot(self.telegram_bot_token)

    def run(self):
        while True:
            jobs = self.search_jobs('Google', 'us:0', 10)

            for job in jobs:
                job_title = job['title']
                job_company = job['company']['name']
                job_location = job['locationDescription']
                job_url = job['jobUrl']
                message = f"New job on LinkedIn: {job_title} at {job_company} in {job_location}\n{job_url}"
                self.send_notification(message)

            time.sleep(3600)

    def search_jobs(self, company_name, location_facet, count):
        job_search = self.client.search_job(
            company_name=company_name,
            facets=f'location,{location_facet}',
            count=count
        )
        return job_search['jobs']['values']

    def send_notification(self, message):
        self.bot.send_message(chat_id=self.telegram_chat_id, text=message)


if __name__ == '__main__':
    notifier = LinkedInJobNotifier(
        os.getenv('LINKEDIN_API_KEY'),
        os.getenv('LINKEDIN_API_SECRET'),
        os.getenv('LINKEDIN_ACCESS_TOKEN'),
        os.getenv('TELEGRAM_BOT_TOKEN'),
        os.getenv('TELEGRAM_CHAT_ID')
    )
    notifier.run()
