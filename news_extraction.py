import requests
import json
import datetime
import argparse
import time

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument
    parser.add_argument('--start_time', type=str, default=str(datetime.datetime.now()-datetime.timedelta(days=4))[0:10], help='Data extraction start time.')
    parser.add_argument('--end_time', type=str, default=str(datetime.datetime.now()-datetime.timedelta(days=1))[0:10], help='Data extraction end time.')
    parser.add_argument('--api_key', type=str, default='ff51fd89-b23b-4bbe-81d1-d22a4d16ac73')
    parser.add_argument('--keywords', type=str, default='', help='keywords want to extract, each keyword in a bracket pair and multiple keywords concat by OR, if you want the words to appear together in a keyword, use AND to concat words/')

    args = parser.parse_args()
    return args

args = parse_args()

# exit()

def get_date(date):
    year = int(date[0:4])
    if date[5] == 0:
        month = int(date[6:7])
    else:
        month = int(date[5:7])
    if date[8] == 0:
        day = int(date[9:10])
    else:
        day = int(date[8:10])
    return year, month, day

start_time_info = get_date(args.start_time)
start_year, start_month, start_day = start_time_info[0], start_time_info[1], start_time_info[2]
end_time_info = get_date(args.end_time)
end_year, end_month, end_day = end_time_info[0], end_time_info[1], end_time_info[2]
start_date = datetime.date(start_year, start_month, start_day)
end_date = datetime.date(end_year, end_month, end_day)
delta = datetime.timedelta(days=1)

# '(Russian AND ukraine AND war) OR (Russian AND ukraine AND conflict) OR (Russian AND ukraine AND invasion) OR (Russophobia) OR (Russophobic ) OR (RussiaPhobia) OR ("Demonise Russia") OR ("stand with Russia") OR ("I stand with Russia") OR ("I stand with Putin") OR (Nazi AND ukraine) OR (Denazify AND Ukraine) OR (Ukraine AND Nazis) OR (Ukraine AND Terrorist AND State) OR (Azov AND Nazi) OR (Minsk AND Accords) OR (Minsk AND Agreements) OR (Zelensky AND Regime) OR (Zelensky AND War AND Criminal) OR (NATO AND Russia AND War) OR (NATO AND War AND Crimes) OR (Protest AND NATO) OR (No AND To AND NATO) OR (Western AND hegemony) OR (US AND neocons) OR ("Biden War") OR ("global South" AND Russia) OR (BRICS AND G7) OR ("BRICS bloc") OR (Prague AND anti-Russian) OR ("Ukrainian Orthodox Church") OR (Minsk AND Merkel)'
print(start_date)
print(end_date)
while (start_date <= end_date):
    print(start_date)
    ALL_URL = f'https://api.goperigon.com/v1/all?apiKey={args.api_key}&from={start_date.strftime("%Y-%m-%d")}&to={start_date.strftime("%Y-%m-%d")}&sourceGroup=top10&source=eautocheck.de&showNumResults=true&showReprints=false&excludeLabel=Non-news&excludeLabel=Opinion&excludeLabel=Paid News&excludeLabel=Roundup&excludeLabel=Press Release&sortBy=date&source=nytimes.com&source=oryxspioenkop.com&source=mate.substack.com&source=wsj.com&source=pravda.com&source=reuters.com&source=thetimes.co.uk&source=bbc.co.uk&source=cnn.com&source=rt.com&source=reddit.com&source=youtube.com&source=theguardian.com&q={args.keywords}'
    resp = requests.get(f"{ALL_URL}&size=100&page=0")
    all_info = resp.json()
    # print(all_info.keys())
    try:
        result_cnt = all_info['numResults']
    except:
        print("I'm sleeping...")
        time.sleep(10)
    file_name = './test/' + start_date.strftime("%Y-%m-%d") + '_page0' + '_total' + str(result_cnt) + '.json'
    with open(file_name, "w") as f:
        json.dump(all_info, f)
    if result_cnt > 100:
        next_page = 1
        current_cnt = result_cnt
        current_cnt -= 100
        while current_cnt > 0:
            resp = requests.get(f"{ALL_URL}&size=100&page={next_page}")
            all_info = resp.json()
            file_name = './test/' + start_date.strftime("%Y-%m-%d") + '_page' + str(next_page) + '_total' + str(result_cnt) + '.json'
            with open(file_name, "w") as f:
                json.dump(all_info, f)
            next_page += 1
            current_cnt -= 100
    start_date += delta


# API_KEY = "ff51fd89-b23b-4bbe-81d1-d22a4d16ac73"
