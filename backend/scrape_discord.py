import requests
import json
from tqdm import tqdm 
import os

PURPLE = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def scrape_discord():
    bar_format = f"{PURPLE}{{l_bar}}{{bar}}{RESET}| {{n_fmt}}/{{total_fmt}} {{elapsed}} < {{remaining}}"
    with tqdm(total=3, desc=f"{GREEN}Discord Scraping Progress{RESET}", unit="step", bar_format= bar_format, colour="BLUE", leave=True) as pbar:

        # get data from discord...
        url = 'https://discord.com/api/v9/channels/710138850009284681/messages?limit=100'
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': 'ODc5MTI0MTk1MzQ1MzE3OTI4.GyEInq.NSQ4xY76xpPll53ASCvr_duUhbtwaPnu3IxuCk',
            'cookie': '__Secure-recent_mfa=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3MTk2MDU1MjQsIm5iZiI6MTcxOTYwNTUyNCwiZXhwIjoxNzE5NjA1ODI0LCJpc3MiOiJ1cm46ZGlzY29yZC1hcGkiLCJhdWQiOiJ1cm46ZGlzY29yZC1tZmEtcmVwcm9tcHQiLCJ1c2VyIjo4NzkxMjQxOTUzNDUzMTc5Mjh9.ahOJ9yMbcHuxl6j5dC4UbIS8EBuEH1qKEKdPQLVxcTnzzyXLsOkrfVn1W9gwzCMcwh-VITjx-pH-HTPf9RnciA; __dcfduid=ca547cd029ec11ef851e6d75e3c3f38e; __sdcfduid=ca547cd129ec11ef851e6d75e3c3f38e20f259f2454c8b4bdcbeadb6008dbe9df6e7551e601cab268533dbd1226113bb; _gcl_au=1.1.156020024.1719259983; _ga_Q149DFWHT7=GS1.1.1719262924.2.0.1719262928.0.0.0; _ga=GA1.1.559862952.1718397454; OptanonConsent=isIABGlobal=false&datestamp=Mon+Jun+24+2024+11%3A13%3A05+GMT-1000+(Hawaii-Aleutian+Standard+Time)&version=6.33.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false; _ga_YL03HBJY7E=GS1.1.1719266914.2.0.1719266914.0.0.0; _ga_5CWMJQ1S0X=GS1.1.1719605484.12.1.1719605642.0.0.0; cf_clearance=iCkLvtWtTLE6NgvSLz5KEgIedCVniIGwvOmyu4WxKKk-1719607792-1.0.1.1-CwIhTRhcY.BvRMM7wka..D0wA2V.74JlmREkuVHdWT6Al1U.xKWGNvuXVO1puQJTGFK.lteqUhD8DFMvXQNHtw; __cfruid=56774ffc9e2616fef1ea008b8168866c5f3bfce6-1719607793; _cfuvid=CwN2_rTtAgLWKcnVlJ.9Gc6mxAWW723ASaAmSrAPHl4-1719607793646-0.0.1.1-604800000',
            'priority': 'u=1, i',
            'referer': 'https://discord.com/channels/710138849350647871/710138850009284681',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-discord-timezone': 'Pacific/Honolulu',
            'x-super-properties': 'eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCA2LjA7IE5leHVzIDUgQnVpbGQvTVJBNThOKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTI2LjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjYuMCIsInJlZmVycmVyIjoiaHR0cHM6Ly9kMmwuYXJpem9uYS5lZHUvIiwicmVmZXJyaW5nX2RvbWFpbiI6ImQybC5hcml6b25hLmVkdSIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjozMDYyMDgsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGwsImRlc2lnbl9pZCI6MH0='
        }
        pbar.update(1)

        response = requests.get(url, headers=headers)
        pbar.update(1)


        # Check if the request was successful
        if response.status_code == 200:
            messages = response.json()
            formatted_messages = []
            for message in messages:
                formatted_message = {
                    'timestamp': message['timestamp'],
                    'author': message['author']['username'],
                    'content': message['content']
                }
                formatted_messages.append(formatted_message)

            # Write to results
            current_directory = os.getcwd()
            file_path = current_directory + "/data/results.json"
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    try: existing_data = json.load(f)
                    except json.JSONDecodeError:existing_data = []
            else:
                existing_data = []
            existing_data.extend(formatted_messages)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(existing_data, f, ensure_ascii=False, indent=4)
        pbar.update(1)
        return
