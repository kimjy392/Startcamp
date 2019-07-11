# dictionary
# key - value
# key : string, integer, float, boolean
# list, dictionary는 key가 될 수 없다.
# value : 모든 값을 가질 수 있다.
lunch = {'중국집': '02-971-2312'}
print(lunch)
dinner = dict(한식='042-999-9999') #한식은 어제 name과 같이 키워드라서 '한식'이라고 쓰지 않음
print(dinner)
bf = {}
bf[ '분식' ] = '012-1231-2132'
print(bf)
menu = {'bf' : bf, 'lunch' : lunch, 'dinner' : dinner}
print(menu)
print(menu['bf']['분식'])

ssafy = {'김은정' : '학생', '김인성' : '학생', '연용흠' : '반장'}
for key in ssafy: # 반복문을 돌리면 key가 나온다.
    print(key)    # type : str
    print(ssafy[key]) # type : str

for key, value in ssafy.items(): # key와 value가 같이 쓰고싶을때
    print(key, value) # type str

print(ssafy.items()) # key와 value를 가지는 튜플들이 리스트형식으로 있다.
# ssafy.items()을 이용하여 반복문을 사용하면 key와 value를 나타낸다.
# type : dict.items
for value in ssafy.values():
    print(value) # type : str

for key in ssafy.keys():
    print(key)  # type : str