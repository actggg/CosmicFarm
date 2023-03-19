import requests
import json


def sorting(sub_li):
    sub_li.sort(key=lambda x: x[1])
    return sub_li


def get():
    mytoken = 'ntade86h'
    url = "https://dt.miet.ru/ppo_it_final"
    headers = {
             "X-Auth-Token": mytoken
        }
    response = requests.get(url, headers=headers)
    json_respons = response.json()
    r = []
    for i in json_respons['message']:
        for j in i['points']:
            r.append([j['SH'], j['distance']])
    sorting(r)
    return r
