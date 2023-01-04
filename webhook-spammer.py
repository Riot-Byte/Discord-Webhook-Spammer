import time
import requests
import os

os.system("cls")
os.system("color 0a")
os.system("title Webhook Spammer")

msg = input("Message to spam : ")
webhook = input("Webhook : ")
amountToSend = input("Amount of messages to send before deleting hook : ")

os.system("cls")
print("Msg : "+msg)
print("Webhook : "+webhook)
print("")
prompt = input("Is this correct? (y/n)")

if prompt == "y":
    def spam(msg, webhook):
        counter = 0
        while True:
            counter = counter + 1
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent {msg}")
            if data.status_code == 404:
                print(f"Sent {msg}")
                break
            if counter == int(amountToSend):
                    time.sleep(3)
                    requests.delete(webhook)
                    exit()
            else:
                try:
                    time.sleep(data.json()["retry_after"]/1000)
                except:
                    pass

    spam(msg, webhook)
elif prompt == "n":
    exit()
