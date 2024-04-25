from telethon import TelegramClient
import datetime
import pandas as pd

# api e hash da generare qui:https://core.telegram.org/api/obtaining_api_id

# Inserire l'ID API di 7 caratteri.
api_id = 'XXXXXXX'
# Inserire l'hash API di 32 caratteri
api_hash = 'XXXXXXXXXXXXXXXXXX'
# Inserire il numero di telefono con cui sono stati creati ID e HASH.
phone = '+39XXXXXXX'

client = TelegramClient(phone, api_id, api_hash)

group = input("inderisci il nome del gruppo (nel formato @nome_gruppo):")
chats = [group]
file_name = "messaggi_scaricati da"+group

df = pd.DataFrame()

for chat in chats:
    with TelegramClient('test', api_id, api_hash) as client:
        for message in client.iter_messages(chat, reverse=True):
            
            print(message.text)
            data = { "group" : chat, "sender_id" : message.sender_id, "text" : message.text, "date" : message.date}

            temp_df = pd.DataFrame(data, index=[1])
            df = df._append(temp_df)

df['date'] = df['date'].dt.tz_localize(None)

df.to_excel(file_name+".xlsx".format(datetime.date.today()), index=False)
print("generato il file",file_name+".xlsx")


