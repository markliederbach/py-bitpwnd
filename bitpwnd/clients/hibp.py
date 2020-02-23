import logging
import hashlib
import requests


log = logging.getLogger(__name__)

class HaveIBeenPwned:
    def __init__(self, base_url=None, range_endpoint=None):
        self.base_url = base_url or "https://api.pwnedpasswords.com"
        self.range_endpoint = range_endpoint or "/range"

    def check_password(self, plain_text):
        hashed = self.sha1(plain_text)
        query = f"{self.range_endpoint}/{hashed[:5]}"
        response = self.get(query)
        data = {item.split(":")[0]: item.split(":")[1] for item in response.text.split("\r\n")}
        return int(data.get(hashed[5:].upper(), 0))

    @staticmethod
    def sha1(plain_text):
        return hashlib.sha1(plain_text.encode()).hexdigest()
    
    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        return requests.get(url, params=params)
