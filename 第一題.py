# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 00:37:44 2024

@author: user
"""

from datetime import datetime, timedelta

# 1. 取得今日的timestamp
today_timestamp = datetime.now().timestamp()

# 2. 將timestamp轉換為時間格式
today_time_format = datetime.fromtimestamp(today_timestamp)

# 3. 顯示今日
today = datetime.now().date()

# 4. 顯示昨日
yesterday = today - timedelta(days=1)

# 5. 顯示昨日的timestamp
yesterday_timestamp = datetime.combine(yesterday, datetime.min.time()).timestamp()

# 6. 將字串轉換為時間格式
# 例：假設字串是 '2024-06-13 12:34:56'
time_string = '2024-06-13 12:34:56'
time_format_from_string = datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')

# 7. 將時間格式轉換為字串
time_string_from_format = time_format_from_string.strftime('%Y-%m-%d %H:%M:%S')

# 8. 將今天顯示為YYMMDD的日期
today_YYMMDD = today.strftime('%y%m%d')

# 9. 計算明年你的生日是星期幾
# 假設你的生日是1月1日
birthday_next_year = datetime(today.year + 1, 1, 1)
birthday_next_year_weekday = birthday_next_year.strftime('%A')

# 10. 將你的生日顯示為西元年與中華民國年
birthday_western = birthday_next_year.strftime('%Y-%m-%d')
birthday_republic_of_china = f"民國{birthday_next_year.year - 1911}年{birthday_next_year.month}月{birthday_next_year.day}日"

{
    "today_timestamp": today_timestamp,
    "today_time_format": today_time_format,
    "today": today,
    "yesterday": yesterday,
    "yesterday_timestamp": yesterday_timestamp,
    "time_format_from_string": time_format_from_string,
    "time_string_from_format": time_string_from_format,
    "today_YYMMDD": today_YYMMDD,
    "birthday_next_year_weekday": birthday_next_year_weekday,
    "birthday_western": birthday_western,
    "birthday_republic_of_china": birthday_republic_of_china
}
