from requests_oauthlib import OAuth1
import requests
import time

def download_data(df):
    API_KEY = "896c85ff-d691-47bc-89e7-97e877919360"
    API_KEY_SECRET = "4XadS4aoYLuO3uP9bLa5YosekDRlECVN3ky"
    ACCESS_TOKEN = "452338e4-d0c5-41b7-9e54-dd2e0d3fc20e"
    ACCESS_TOKEN_SECRET = "SBPFRsuhmHq9rdr1FtDgMT2AIbc7JQaOeD6"


    OAUTH = OAuth1(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    HEADERS = {'Content-Type': 'application/json', 'Accept': '*/*'}

    ### Get file names 
    for index, row in df.iterrows():
        print(index)
        print(row)
        url = row['callbackURL']
        file_name = row['summaryId']
        print(url)
        print(file_name)

        res = requests.get(
            url, 
            headers=HEADERS, 
            auth=OAUTH
        )
        print(res.content)

        file_path = f"/code/FIT_files/FIT_file_{file_name}.bin"

        with open(file_path, "wb") as file:
            file.write(res.content)

        time.sleep(1)