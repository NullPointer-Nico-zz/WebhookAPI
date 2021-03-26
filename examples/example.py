import json
import time
import sys
import sys
import os

sys.path.append(os.pardir)
sys.path.append(os.path.join(os.pardir, os.pardir))

from src.Webhook import Webhook

settings = json.load(open("settings.json"))

webhook = Webhook(
    url=settings["webhook"],
    username=settings["username"],
    avatar_url=settings["avatar_url"]
)

res = webhook.post(message="Coutdown")

for i in reversed(range(6)):
    webhook.editPost(messageID=res["id"], message=i)
    time.sleep(1)
