# Apollo2_Data_Collection
Data extraction code for Appolo 2.0

## News extraction
Sample code:
Get news by day with keyword 'russophobia' and date range from 2022-05-01 to 2022-06-01
```
python ./news_extraction_daily.py --api_key 'your api key' --keywords 'russophobia' --start_time '2022-05-01' --end_time '2022-06-01'
```
Get news in general with keyword 'russophobia' and date range from 2022-05-01 to 2022-06-01
```
python ./news_extraction.py --api_key 'your api key' --keywords 'russophobia' --start_time '2022-05-01' --end_time '2022-06-01'
```
Get youtube metadata in general with keyword 'russophobia' and date range from 2022-05-01 to 2022-06-01
```
python ./youtube_extraction.py --api_key 'your api key' --keywords 'russophobia' --start_time '2022-05-01' --end_time '2022-06-01'
```
