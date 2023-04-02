import requests


class DiscordWebhook():
    def __init__(self):
        self.webhook_url = "https://discord.com/api/webhooks/1091986851964911618/SZ3m5JB4xKlzMzlk0PhGLEp078zU4wCeOSjcjb4SVTu7VF7B2KshtyIabxQGssuhtpp8"
        self.header = {
            'Content-Type':'application/json',
        }

    def send_message(self, comment:str):
        json = {"content": f"{comment}"}
        requests.post(
            url=self.webhook_url,
            headers=self.header,
            json=json,
        )
