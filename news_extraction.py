import requests
import json
import datetime
import argparse
import time
import os

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument
    parser.add_argument('--start_time', type=str, default=str(datetime.datetime.now()-datetime.timedelta(days=10))[0:10], help='Data extraction start time.')
    parser.add_argument('--end_time', type=str, default=str(datetime.datetime.now()-datetime.timedelta(days=1))[0:10], help='Data extraction end time.')
    parser.add_argument('--api_key', type=str, default='ff51fd89-b23b-4bbe-81d1-d22a4d16ac73')
    parser.add_argument('--keywords', type=str, default='', help='keywords want to extract, each keyword in a bracket pair and multiple keywords concat by OR, if you want the words to appear together in a keyword, use AND to concat words/')

    args = parser.parse_args()
    return args

args = parse_args()

try:
    os.mkdir('./test')
except:
    print('folder already exists')


# '(Russian AND ukraine AND war) OR (Russian AND ukraine AND conflict) OR (Russian AND ukraine AND invasion) OR (Russophobia) OR (Russophobic ) OR (RussiaPhobia) OR ("Demonise Russia") OR ("stand with Russia") OR ("I stand with Russia") OR ("I stand with Putin") OR (Nazi AND ukraine) OR (Denazify AND Ukraine) OR (Ukraine AND Nazis) OR (Ukraine AND Terrorist AND State) OR (Azov AND Nazi) OR (Minsk AND Accords) OR (Minsk AND Agreements) OR (Zelensky AND Regime) OR (Zelensky AND War AND Criminal) OR (NATO AND Russia AND War) OR (NATO AND War AND Crimes) OR (Protest AND NATO) OR (No AND To AND NATO) OR (Western AND hegemony) OR (US AND neocons) OR ("Biden War") OR ("global South" AND Russia) OR (BRICS AND G7) OR ("BRICS bloc") OR (Prague AND anti-Russian) OR ("Ukrainian Orthodox Church") OR (Minsk AND Merkel)'

def get_data(url, page):
    resp = requests.get(f"{ALL_URL}&size=100&page={str(page)}")
    all_info = resp.json()
    result_cnt = all_info['numResults']
    return all_info, result_cnt
    

ALL_URL = f'https://api.goperigon.com/v1/all?apiKey={args.api_key}&from={args.start_time}&to={args.end_time}&sourceGroup=top10&source=eautocheck.de&showNumResults=true&showReprints=false&excludeLabel=Non-news&excludeLabel=Opinion&excludeLabel=Paid News&excludeLabel=Roundup&excludeLabel=Press Release&sortBy=date&source=nytimes.com&source=oryxspioenkop.com&source=mate.substack.com&source=wsj.com&source=pravda.com&source=reuters.com&source=thetimes.co.uk&source=bbc.co.uk&source=cnn.com&source=rt.com&source=reddit.com&source=youtube.com&source=theguardian.com&q={args.keywords}'
# print(all_info.keys())
while True:
    try:
        all_info, result_cnt = get_data(ALL_URL,0)
        break
    except:
        print("I'm sleeping...")
        time.sleep(10)
file_name = './test/' + args.start_time + '_' + args.end_time + '_page0' + '_total' + str(result_cnt) + '.json'
with open(file_name, "w") as f:
    json.dump(all_info, f)
if result_cnt > 100:
    next_page = 1
    current_cnt = result_cnt
    current_cnt -= 100
    while current_cnt > 0:
        while True:
            try:
                all_info, result_cnt = get_data(ALL_URL, next_page)
                file_name = './test/' + args.start_time + '_' + args.end_time + '_page' + str(next_page) + '_total' + str(result_cnt) + '.json'
                with open(file_name, "w") as f:
                    json.dump(all_info, f)
                next_page += 1
                current_cnt -= 100
#                 print(args.start_time)
                break
            except:
                print("I'm sleeping...")
                time.sleep(10)



# API_KEY = "ff51fd89-b23b-4bbe-81d1-d22a4d16ac73"


