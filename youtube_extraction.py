import requests
import json
import datetime
import argparse
import time
import os

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument
    parser.add_argument('--start_time', type=str, default=str(datetime.datetime.now()-datetime.timedelta(days=30))[0:10], help='Data extraction start time.')
    parser.add_argument('--end_time', type=str, default=str(datetime.datetime.now()-datetime.timedelta(days=1))[0:10], help='Data extraction end time.')
    parser.add_argument('--api_key', type=str, default='AIzaSyCjvTWICzSBU0m4Z9PL1IEhNd1LW34BnhE')
    parser.add_argument('--keywords', type=str, default='', help='https://developers.google.com/youtube/v3/docs/search/list')

    args = parser.parse_args()
    return args

args = parse_args()

try:
    os.mkdir('./test')
except:
    print('folder already exists')

page_idx = 0

ALL_URL = f"https://www.googleapis.com/youtube/v3/search?key={args.api_key}&part=snippet&maxResults=50&q={args.keywords}&type=video&publishedBefore={args.end_time}T00:00:00Z&publishedAfter={args.start_time}T00:00:00Z"
resp = requests.get(ALL_URL)
all_info = resp.json()
file_name = './test/' + args.start_time + '_' + args.end_time + '_' + args.keywords + '_page' + str(page_idx) + '.json'
with open(file_name, "w") as f:
    json.dump(all_info, f)


while True:
    try:
        page_idx += 1
        nextPageToken = all_info['nextPageToken']
        print(args.start_time)
        print(nextPageToken)
        ALL_URL = f"https://www.googleapis.com/youtube/v3/search?key={args.api_key}&part=snippet&maxResults=50&q={args.keywords}&type=video&publishedBefore={args.end_time}T00:00:00Z&publishedAfter={args.start_time}T00:00:00Z&pageToken={nextPageToken}"
        resp = requests.get(ALL_URL)
        all_info = resp.json()
        file_name = './test/' + args.start_time + '_' + args.end_time + '_' + args.keywords + '_page' + str(page_idx) + '.json'
        with open(file_name, "w") as f:
            json.dump(all_info, f)
    except:
        break
