"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')

score_sum = score['수학'] + score['국어'] + score['음악']
print(score_sum/3)

# 1. 기본 풀이

result = 0
for score_value in score.values():
    result += score_value     # result = result + score_value
print(result/len(score))

# 2. sum 함수 활용하기
result2 = sum(score.values())  # dict_values[80, 90, 100] 리스트와 비슷하다고 생각한다. sum은 나열된 것들(리스트, 튜플..etc)을 다 더해준다.
count = len(score)
print(result2/count)

# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
sums = 0
count = 0
for key in scores:
    for key2 in scores[key]:
        sums = sums + int(scores[key][key2])
        count += 1
print(sums/count)

for person_score in scores.values():
    print(person_score)                     # {'수학': 80, '국어': 90, '음악': 100} 결과값
    for score in person_score.values():
        print(score)



# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?


# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""

for city_name, temp in city.items():
    city_avg = sum(temp)/len(temp)
    print(f'{city_name} : {city_avg:.2f}') # f-string ver 3.6 +
    print('{} : {:.2f}'.format(city_name,city_avg)) # format-string
    print(city_name + ' : ' + city_avg)




# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?


# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

for city_name, temp in city.items():
    city_avg = sum(temp)/len(temp)
    city_avgs ={ {city : city_avg}}
    print(f'{city_name} : {city_avg:.2f}')


# 모든 지역의 온도를 모두 확인하면서,
min_temp = 0                    # 초기화를 주게되면 -값도 있기 때문에 힘들다.
max_temp = 0
min_city = ''
max_city = ''
count = 0

for city_name, temp in city.items():
    # 첫번째 반복때는 모두 다 저장해!      여기서는 만약 온도의 초기화 값을 주기 힘들기 때문에 처음부터 값을 넣어 비교하기 된다!
    if count == 0:                    
        min_city = city_name
        max_city = city_name
        min_temp = temp
        max_temp = temp
        count += 1
    # 가장 추우면 해당 도시와 기온을 기록하고, 
    if min(temp) < min_temp:
        min_city = city_name
        min_temp = min(temp)
    # 더울 때도 해당 도시와 기온을 기록
    if max(temp) > max_temp:
        max_city = city_name
        max_temp = max(temp)

# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')

if 2 in city['서울']: # 파이썬에서 if문의 in은 2가 city에 있는지 없는지 확인한다.
    print('네')
else:
    print('아뇨')