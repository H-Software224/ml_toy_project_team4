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
appkey = input('T맵 appkey를 입력하시오 ')
t_map_url = f'https://apis.openapi.sk.com/tmap/routes/pedestrian?version=1&appKey={appkey}'

# t-map을 이용하여 최적의 경로의 총시간과 총 거리 구하기
def find_road_list(start_x, start_y, end_x, end_y, start_name, end_name):
    extra_element = f'&startX={start_x}&startY={start_y}&endX={end_x}&endY={end_y}&reqCoordType=WGS84GEO&startName={start_name}&endName={end_name}&resCoordType=WGS84GEO'
    url = t_map_url + extra_element
    req = Request(url)
    response = urlopen(req)
    res = response.getcode()
    if res == 204:
        print("No Content")
        return None
    elif res == 400:
        print("Bad Request")
        return None
    elif res == 500:
        print("Internal Server Error")
        return None
    else:
        body = response.read().decode('utf-8')
        json_dict = json.loads(body)
        return [json_dict['features'][0]['properties']['totalDistance'], json_dict['features'][0]['properties']['totalTime']]
input_list = [x for x in input("데이터 입력해주세요").split()]
startX = input_list[0]
startX = float(startX)
startY = input_list[1]
startY = float(startY)
endX = input_list[2]
endX = float(endX)
endY = input_list[3]
endY = float(endY)
startName = input("시작 주소를 입력해주세요 ")
startName = quote(startName)
endName = input("끝 주소를 입력해주세요 ")
endName = quote(endName)
print(find_road_list(startX, startY, endX, endY, startName, endName))





