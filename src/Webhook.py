import requests
import json

from src.utils.File import File

class Webhook:
    def __init__(self, url: str, username: str = None, avatar_url: str = None) -> None:
        self.url = url
        self.username = username
        self.avatar_url = avatar_url

    def getWebhook(self) -> dict:
        return requests.get(self.url).json()

    def editPost(self, messageID: str , message: str, embeds: list[dict] = None) -> None:

        content = {
            "content": message,
            "embeds": embeds
        }

        requests.patch(url=self.url + f"/messages/{messageID}?wait=true", headers={"Content-Type": "application/json"}, json=content)

    def deletePost(self, messageID: str) -> None:
        requests.delete(url=self.url + f"/messages/{messageID}?wait=true")

    def post(self, message: str, embeds: list[dict] = None,
             tts: bool = False, file: File = None) -> dict:

        content = {
            "content": message,
            "embeds": embeds,
            "username": self.username,
            "avatar_url": self.avatar_url,
            "tts": tts
        }

        if not file:
            res = requests.post(url=self.url + "?wait=true", headers={"Content-Type": "application/json"}, json=content)
        else:
            multipart = {
                "file": (file.name, file.file)
            }   

            res = requests.post(url=self.url + "?wait=true", headers={}, data={"payload_json": json.dumps(content)}, files=multipart)

        return res.json()