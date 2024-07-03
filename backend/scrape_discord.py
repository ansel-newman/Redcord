import requests
import json

def scrape_discord():
    # Define the headers and URL
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

    # Send the GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse JSON response
        messages = response.json()

        # Initialize list to store formatted messages
        formatted_messages = []

        # Iterate through messages and format each one
        for message in messages:
            formatted_message = {
                'timestamp': message['timestamp'],
                'author': message['author']['username'],
                'content': message['content']
            }
            formatted_messages.append(formatted_message)

        # Write formatted messages to JSON file
        # with open('data/results_discord.json', 'w') as f:
        with open('data/results.json', 'w') as f:
            json.dump(formatted_messages, f, indent=4)
            
        print(f"Messages successfully saved to 'results_discord.json'.")
    else:
        print(f"Failed to retrieve messages. Status code: {response.status_code}")
    return
