import json
import time
from time import sleep
from pyproj import Proj, transform
from urllib import parse
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import HTTPError
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://map.naver.com/p/'
# driver
driver = webdriver.Chrome()  # 드라이버 경로

client_id = input("본인의 Client_ID를 입력하세요 ")
client_secret = input("본인의 Clinet_Secret를 입력하세요 ")

naver_api_url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query='

# UTM-K
proj_UTMK = Proj(init='epsg:5178')

# WGS1984
proj_WGS84 = Proj(init='epsg:4326')

# css 찾을때 까지 10초대기
def time_wait(num, code):
    try:
        wait = WebDriverWait(driver, num).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, code)))
    except:
        print(code, '태그를 찾지 못하였습니다.')
        driver.quit()
    return wait

# frame 변경 메소드
def switch_frame(frame):
    driver.switch_to.default_content()  # frame 초기화
    driver.switch_to.frame(frame)  # frame 변경

# 페이지 다운
def page_down(num):
    body = driver.find_element(By.CSS_SELECTOR, 'body')
    body.click()
    for i in range(num):
        body.send_keys(Keys.PAGE_DOWN)

def crawl_word(key_word, important, json_file):
    driver.get(url)

    # css를 찾을때 까지 10초 대기
    time_wait(10, 'div.input_box > input.input_search')

    # (1) 검색창 찾기
    search = driver.find_element(By.CSS_SELECTOR, 'div.input_box > input.input_search')
    search.send_keys(key_word)  # 검색어 입력
    search.send_keys(Keys.ENTER)  # 엔터버튼 누르기

    sleep(1)

    # (2) frame 변경
    switch_frame('searchIframe')
    page_down(40)
    sleep(3)

    # 페이지 리스트
    next_btn = driver.find_elements(By.CSS_SELECTOR, '.zRM9F> a')

    # 탕후루 마켓 디렉터리 생성
    market_dict = {important: []}

    # 시작시간
    start = time.time()
    print("크롤링 시작!!")
    message_count = 1

    # crawling (페이지 리스트 만큼)
    for btn in range(len(next_btn))[1:]:
        # 마켓 명단 리스트
        market_list = driver.find_elements(By.CSS_SELECTOR, 'li.UEzoS.rTjJo')

        # 마켓 간판 제목 리스트
        market_name = driver.find_elements(By.CSS_SELECTOR, 'span.place_bluelink.TYaxT')

        for data in range(len(market_list)):
            print(f'{message_count}번째')
            try:
                # 지번 주소, 도로명 초기화
                road_address = ''

                # (3) 시장명 가져오기
                shop_name = market_name[data].text
                if (shop_name.find(important) >= 0):
                    print(shop_name)

                    # 주소 버튼 누르기
                    address_buttons = driver.find_elements(By.CSS_SELECTOR, '.Q8Zql > a')
                    address_buttons.__getitem__(data).click()

                    # 로딩 기다리기
                    sleep(1)

                    # (6) 주소 눌렀을 때 도로명, 지번 나오는 div
                    addr = driver.find_elements(By.CSS_SELECTOR, 'div.jg1ED > div')

                    # 도로명만 있는 경우
                    if len(addr) == 1 and addr.__getitem__(0).text[0:2] == '도로':
                        road = addr.__getitem__(0).text
                        last_index = road.find('복사우')
                        road_address = road[3:last_index]
                        print("도로명 주소:", road_address)

                    # 도로명, 지번 둘 다 있는 경우
                    else:
                        # 도로명
                        road = addr.__getitem__(0).text
                        road_address = road[3:(len(road) - 2)]
                        print("도로명 주소:", road_address)

                    # dict에 데이터 집어넣기
                    parse_road_address = parse.quote(road_address)
                    address_api_url = naver_api_url + parse_road_address

                    # 위도 경도 추출하기
                    res = Request(address_api_url)
                    res.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
                    res.add_header('X-NCP-APIGW-API-KEY', client_secret)

                    try:
                        response = urlopen(res)
                    except HTTPError as e:
                        print('HTTP Error!')
                        latitude = None
                        longitude = None
                    else:
                        rescode = response.getcode()
                        if rescode == 200:
                            response_body = response.read().decode('utf-8')
                            response_body = json.loads(response_body)
                            if response_body['addresses'] == []:
                                latitude = None
                                longitude = None
                            else:
                                latitude = response_body['addresses'][0]['y']
                                longitude = response_body['addresses'][0]['x']
                                # utm-k x, y값
                                x, y = transform(proj_WGS84, proj_UTMK, longitude, latitude)
                                dict_temp = {
                                    'market_name': shop_name,
                                    'road_address': road_address,
                                    'latitude': latitude,
                                    'longitude': longitude,
                                    'utm-k.x': x,
                                    'utm-k.y': y
                                }
                                market_dict[important].append(dict_temp)
                        else:
                            print(f'Response error code : {rescode}')
                            latitude = None
                            longitude = None
                    print(f'{market_name} ... 완료!')
                    sleep(1)
                    message_count+=1
            except Exception as e:
                print(e)
                print('ERROR!' * 3)
                sleep(1)
        # 다음 페이지 버튼 누를 수 없으면 종료
        if not next_btn[-1].is_enabled():
            break

        if market_name[-1]: # 마지막 주차장일 경우 다음버튼 클릭
            next_btn[-1].click()
            sleep(2)
        else:
            print('페이지 인식 못함')
            break

    print('데이터 수집 완료\n 소요 시간: ', time.time() - start)
    driver.quit()

    # json 파일로 저장
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(market_dict, f, indent=4, ensure_ascii=False)

 # 검색어
key_word2 = '서울스타벅스'
important2 = '스타벅스'
crawl_word(key_word2, important2, 'E:\\codeitpython\\starbucks.json')









