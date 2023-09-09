# KHUDA 4th Machine Learning Toy Project TEAM 4
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fmini-min&count_bg=%2340B2DF&title_bg=%23B2A3A3&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)  

![Python](https://img.shields.io/badge/Python-blue?style=flat-square&logo=Python&logoColor=white)
<img src="https://img.shields.io/badge/Scikit Learn-F7931E?style=flat-square&logo=Scikit Learn&logoColor=white"/>
<img src="https://img.shields.io/badge/Google Colab-F9AB00?style=flat-square&logo=Google Colab&logoColor=white"/>

- <b> 프로젝트 명 : 탕후루 사조
- <b> 한 줄 소개 : 탕후루 가게의 입점 조건 학습을 통한 새로운 입점 장소 예측하기
- <b> Project Period: 2023.08.30 ~ 2023.09.06 (8 Days)
  
[발표 자료 PDF 보러가기](https://github.com/mini-min/ml_toy_project_team4/blob/feature/%232/%ED%83%95%ED%9B%84%EB%A3%A8%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20ppt%20%EC%B5%9C%EC%B5%9C%EC%B5%9C%EC%A2%85.pdf)

<br>

## ✍🏻 File Description

| File Name | Description |
| ------ | -------- |
| [📦 crawling](https://github.com/mini-min/ml_toy_project_team4/tree/feature/%232/crawling) | 데이터 저장용, 크롤링할 때 사용한 코드입니다. |
| [📦 data_collection](https://github.com/mini-min/ml_toy_project_team4/tree/feature/%232/data_collection) | 프로젝트 input, target 데이터로 활용한 파일들을 모아두었습니다. |
| [Visualize.ipynb](https://github.com/mini-min/ml_toy_project_team4/blob/feature/%232/Visualize.ipynb) | 최종 탕후루 예측치를 시각화하는 코드입니다. |
| [data_filter_weight.ipynb](https://github.com/mini-min/ml_toy_project_team4/blob/feature/%232/data_filter_weight.ipynb) | input 데이터들을 weight값으로 변환해 df로 저장하는 코드입니다. |
| [find_road.py](https://github.com/mini-min/ml_toy_project_team4/blob/feature/%232/find_road.py) | 직선 거리 대신, 길 찾기 거리를 계산하기 위한 코드입니다. 이번 프로젝트에서는 활용하지 못한 부분입니다. |
| [grid_final.ipynb](https://github.com/mini-min/ml_toy_project_team4/blob/feature/%232/grid_final.ipynb) | 서울을 grid 범위에 따라 h3 형태로 나누고, 데이터 프레임으로 값을 반환시켜주는 코드입니다. |
| [ml_regression.ipynb](https://github.com/mini-min/ml_toy_project_team4/blob/feature/%232/ml_regression.ipynb) | Linear Regression Modelling 코드입니다. |
| [📦 res_coordinates](https://github.com/mini-min/ml_toy_project_team4/blob/feature/%232/res_coordinates.zip) | grid resolution 값에 따른 좌표값 데이터들을 모아둔 파일입니다. |
| [📦 res_dist_weight_data](https://github.com/mini-min/ml_toy_project_team4/blob/feature/%232/res_dist_weight_data.zip) | res와 dist 값에 따라 weight 값을 적용한 df 데이터들을 모아둔 파일입니다. |
| [tanghulu_data_code](https://github.com/mini-min/ml_toy_project_team4/blob/feature/%232/tanghulu_data_code.ipynb) | res_dist_weight_data를 만들기 위한 코드입니다. |

<br>

## 🧑🏻‍💻 역할 분배

| 이름 | 깃허브 링크 | 담당한 부분 |
| ------ | -------- | ----------------	|
| 이민재 | [See GitHub Profile](https://github.com/mini-min) | 아이디어 빌딩, 데이터 전처리, Grid Map, Modelling, 발표 |
| 김원진 | [See GitHub Profile](https://github.com/wjcldply) | 아이디어 빌딩, 데이터 전처리, Grid Map, 데이터 필터링, 시각화, 모델 개선 |
| 이예원 | [See GitHub Profile](https://github.com/yewon1077) | 아이디어 빌딩, 데이터 전처리, API 활용 크롤링, PPT 제작 |
| 한주상 | [See GitHub Profile](https://github.com/H-Software224) | 아이디어 빌딩, 데이터 전처리, API 활용 크롤링, 데이터 필터링, 시각화 |
| 이상원 | [See GitHub Profile](https://github.com/LeeSangWon0916) | 아이디어 빌딩, 데이터 전처리, 모델/weight 함수 개발, 데이터 필터링, 모델 개선 |
| 한채연 | [See GitHub Profile](https://github.com/intelsally) | 아이디어 빌딩, 데이터 전처리, 모델/weight 함수 개발, Modelling |
