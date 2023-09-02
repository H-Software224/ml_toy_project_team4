import pandas as pd
import json
import urllib
from urllib.request import Request, urlopen


naver_client_id = '0b2hd38u2v'
naver_client_secret = 'H56l93DfgQbQ2bFLhOTAcTHSDCAeuIUO2AHFxSKC'
yuchiwon_dataframe = pd.read_json('yuchiwon.json')
tanghulu_dataframe = pd.read_json('practice.json')
naver_map_api_source_url = "https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving?"

find_tangulu_road_dict = {'tangulu_road': []}
find_yuchiwon_road_dict = {'yuchiwon_road': []}
def optimal_route(start, goal):
    url = f"{naver_map_api_source_url}start={start[0]},{start[1]}&goal={goal[0]},{goal[1]}"
    req = Request(url)
    req.add_header('X-NCP-APIGW-API-KEY-ID', naver_client_id)
    req.add_header('X-NCP-APIGW-API-KEY', naver_client_secret)

    response = urlopen(req)
    res = response.getcode()
    if res == 200:
        response_body = response.read().decode('utf-8')
        return json.loads(response_body)
    else:
        print('ERROR')

def answer(start, goal):
    source = optimal_route(start, goal)
    path = source['route']['traoptimal'][0]['path']
    section = source['route']['traoptimal'][0]['section']
    guide = source['route']['traoptimal'][0]['guide']
    section_list = []
    guide_list = []
    for i in section:
        word = ""
        word = word + i['name'] + " "
        word = word + str(i['distance'] // 1000) + 'km'
        section_list.append(word)
    for i in guide:
        word2 = ""
        word2 = word2 + str(i['distance']) + "m "
        word2 = word2 + i['instructions']
        guide_list.append(word2)
    correct_dict = {
        'section': section_list,
        'guide': guide_list,
        'path': path
    }
    return correct_dict


# 내 자취방 경도, 위도
start_point_list = [127.0772013, 37.2488594]

# 탕후루 데이터프레임 JSON 파일로 저장하기
for i in range(len(tanghulu_dataframe.values)):
    arrive_point_longitude = tanghulu_dataframe.values[i][0]['longitude']
    arrive_point_latitude = tanghulu_dataframe.values[i][0]['latitude']
    print(answer(start_point_list, [arrive_point_longitude, arrive_point_latitude]))
    find_tangulu_road_dict['tangulu_road'].append(answer(start_point_list, [arrive_point_longitude, arrive_point_latitude]))

with open('E:\\codeitpython\\tanghulu_road.json', 'w', encoding='utf-8') as f:
    json.dump(find_tangulu_road_dict, f, indent=4, ensure_ascii=False)

# 유치원 데이터프레임 JSON 파일로 저장하기
for i in range(len(yuchiwon_dataframe.values)):
    arrive_point_longitude = yuchiwon_dataframe.values[i][0]['longitude']
    arrive_point_latitude = yuchiwon_dataframe.values[i][0]['latitude']
    print(answer(start_point_list, [arrive_point_longitude, arrive_point_latitude]))
    find_yuchiwon_road_dict['yuchiwon_road'].append(answer(start_point_list, [arrive_point_longitude, arrive_point_latitude]))

with open('E:\\codeitpython\\yuchiwon_road.json', 'w', encoding='utf-8') as f:
    json.dump(find_yuchiwon_road_dict, f, indent=4, ensure_ascii=False)


