import logging
import hashlib
import requests


log = logging.getLogger(__name__)

class HaveIBeenPwned:
    def __init__(self):
        pass

    @staticmethod
    def sha1(plain_text):
        return hashlib.sha1(plain_text.encode()).hexdigest()
