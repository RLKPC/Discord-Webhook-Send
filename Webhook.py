#Discord読み込み
import requests
import json
import time
import colorama
from colorama import Fore, Back, Style


#Webhook Send Creator
colorama.init(autoreset=True)
print("")
print("")
time.sleep(1)
print(Fore.RED +"               _     _                 _         ______                 _    _______                                    ")
print(Fore.RED +"              | |   | |               | |       / _____)               | |  (_______)                    _              ")
time.sleep(1)
print(Fore.RED +" _  _  _ _____| |__ | |__   ___   ___ | |  _   ( (____  _____ ____   __| |   _        ____ _____ _____ _| |_ ___   ____ ")
time.sleep(1)
print(Fore.RED +"| || || | ___ |  _ \|  _ \ / _ \ / _ \| |_/ )   \____ \| ___ |  _ \ / _  |  | |      / ___) ___ (____ (_   _) _ \ / ___)")
time.sleep(1)
print(Fore.RED +"| || || | ____| |_) ) | | | |_| | |_| |  _ (    _____) ) ____| | | ( (_| |  | |_____| |   | ____/ ___ | | || |_| | |    ")
time.sleep(1)
print(Fore.RED +" \_____/|_____)____/|_| |_|\___/ \___/|_| \_)  (______/|_____)_| |_|\____|   \______)_|   |_____)_____|  \__)___/|_|    ")
time.sleep(1)
print(Fore.RED +"                                                                                                                        ")
time.sleep(2)
print(Fore.GREEN +"product by Runa")
time.sleep(1)
print("")
print("--------------------------------")
print("")
print("")
webhook_url=input("Webhook URLを入力してください：")
print("")
print("")
print("-----------------------------------------")
print("")
print("")
username=input("Webhookの名前を入力してください：")
print("")
print("")
print("----------------------------------------")
print("")
print("")
avatar_url=input("WebhookのアイコンURLを送信してください \n(指定しない場合はそのままEnte)：")
print("")
print("")
print("-------------------------------------------------------------------------------")
print("")
print("")
select_option=str(input("通常メッセージの場合は 1  \nembedでの送信の場合は 2 を送信してください："))
print("")
print("")
print("------------------------------------------------------------------------------------")
print("")
print("")
if select_option=="1":
    send_embed=False
    None
    print(Fore.BLUE + "通常メッセージを選択しました。")
    print("")
    print("")
    print("---------------------------")
    print("")
    print("")
    content=input("送信したいメッセージを入力してください：")
    print("")
    print("")
    print("--------------------------------------------")
    print("")
    print("")


elif select_option=="2":
    send_embed=True
    print(Fore.BLUE + "Embedメッセージを選択しました。")
    print("")
    print("")
    print("-----------------------------")
    print("")
    print("")
    embed_title=input("embedのタイトルを入力してください：")
    print("")
    print("")
    print("--------------------------------------------")
    print("")
    print("")
    description=input("embedのdescriptionを入力してください\n(指定しない場合はそのままEnte)：")
    print("")
    print("")
    print("--------------------------------------------")
    print("")
    print("")



main_content = {
  "username":username,
  "avatar_url":avatar_url,
}

if send_embed:
    main_content["embeds"]=[{"color": 0x33e7ff,"title": embed_title,"description": description}]
else:
    main_content["content"]=content


response=requests.post(webhook_url,data=json.dumps(main_content),headers={"Content-Type": "application/json"})


print(Fore.BLUE + "送信が完了しました。5秒後にWebhook Send Creatorは閉じられます。")
time.sleep(5)