ssafy = {
    'location': ['서울', '대전', '구미', '광주'],
    'language': {
        'python': {
            'python standard library': ['os', 'random', 'webbrowser'],
            'frameworks': {
                'flask': 'micro',
                'django': 'full-functioning'
            },
            'data_science': ['numpy', 'pandas', 'scipy', 'sklearn'],
            'scraping': ['requests', 'bs4'],
        },
        'web' : ['HTML', 'CSS']
    },
    'classes': {
        'dj': {
            'lecturer': 'tak',
            'manager': '노구하',
            'class president': '연용흠',
            'groups': {
                'A': ['송지영', '최성철', '박진희', '박태수', '염동환', '연용흠'],
                'B': ['홍순범', '김준영', '양혜진', '서현택', '최무연', '조선행'],
                'C': ['김태우', '이승열', '장은비', '조병준', '김인성'],
                'D': ['김은정', '이지민', '이경호', '정지수', '염겨레'],
            }
        },
        'gj': {
            'lecturer': 'change',
            'manager': 'gj-pro'
        }
    }
}


"""
난이도* 1. 지역(location)은 몇 개 있나요?
출력예시)
4
"""
for key,value in ssafy.items():
    if key == 'location':
        print(len(value))


"""
난이도** 2. python standard library에 'requests'가 있나요?
출력예시)
False
"""
# for key,value in ssafy.items():
#     if key == 'language':
#         for key, value in key.itmes()


"""
난이도** 3. dj 반의 반장의 이름을 출력하세요.
출력예시)
연
"""


"""
난이도*** 4. ssafy에서 배우는 언어들을 출력하세요.
출력 예시)
python
web
"""



"""
난이도*** 5 ssafy gj반의 강사와 매니저의 이름을 출력하세요.
출력 예시)
change
pro-gj
"""


"""
난이도***** 6. framework 들의 이름과 설명을 다음과 같이 출력하세요.
출력 예시)
flask는 micro이다.
django는 full-functioning이다.
"""



"""
난이도***** 7. 오늘 당번을 뽑기 위해 groups의 D 그룹에서 한명을 랜덤으로 뽑아주세요.
출력예시)
오늘의 당번은 김준호
"""



dictionary = {'apple': '사과', 'banana': '바나나'}
# print(dictionary['cat'])
dictionary.get('cat')  # .get('cat')은 오류가 뜨지않는다.
print(dictionary.get('apple',0)) # .get('cat',0)은 'cat'이 없으면 0를 반환한다. 있으면 dictionary에 있는 값을 반환