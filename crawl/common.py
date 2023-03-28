import requests

class Common:
    def __init__(self):
        pass
    
    def get_html_by_url(self, url:str) -> str:
        response = requests.get(
            url=url,
        )

        return response.text