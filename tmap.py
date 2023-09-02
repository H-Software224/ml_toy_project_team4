import json

import pandas as pd
from urllib.request import Request, urlopen
from urllib.parse import quote
# 데이터 값 작성
# tanghulu_position = pd.read_json('tanghulu.json')
# yuchiwon_position = pd.read_json('yuchiwon.json')
# college_coordinator = pd.read_csv('college_coordinator.csv')
# college_address = pd.read_csv('college_address.csv', encoding='cp949')
#
# arrive_list = []
# yuchiwon_list = []
# college_list = []
# for i in range(len(tanghulu_position.values)):
#     arrive_point_longitude = tanghulu_position.values[i][0]['longitude']
#     arrive_point_latitude = tanghulu_position.values[i][0]['latitude']
#     arrive_list.append([arrive_point_longitude, arrive_point_latitude])
#
# for i in range(len(yuchiwon_position.values)):
#     start_point_longitude = yuchiwon_position.values[i][0]['longitude']
#     start_point_latitude = yuchiwon_position.values[i][0]['latitude']
#     yuchiwon_list.append([start_point_longitude, start_point_latitude])

# t-map api 이용해서 학습
appkey = input('T맵 appkey를 입력하시오')
t_map_url = f'https://apis.openapi.sk.com/tmap/routes/pedestrian?version=1&appKey={appkey}'

startX = float(input())
startY = float(input())
endX = float(input())
endY = float(input())
startName = input()
startName = quote(startName)
endName = input()
endName = quote(endName)
extra_element = f'&startX={startX}&startY={startY}&endX={endX}&endY={endY}&reqCoordType=WGS84GEO&startName={startName}&endName={endName}&resCoordType=WGS84GEO'
url = t_map_url + extra_element
req = Request(url)
response = urlopen(req)
res = response.getcode()
if res == 204:
    print("No Content")
elif res == 400:
    print("Bad Request")
elif res == 500:
    print("Internal Server Error")
else:
    body = response.read().decode('utf-8')
    print(json.loads(body))


