import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/exchangeList.nhn'

response = requests.get(url).text
print(response)
soup = BeautifulSoup(response,'html.parser')
 
# iframe이 있다면 src라고 써져있는 곳을 보면 그 뒤에 url이 있다. 그 url에서 정보를 받아오는것 
# 따라서 그 url로 가 그곳에서 선택자를 해야한다.
# soup.select_one 에서 select로 바꿔 여러개를 선택

dollar = soup.select('body > div > table > tbody > tr') # tbody 이후 tr로 세부사항이 있기때문에 tr까지 쓴다.
for tr in dollar:
    print(tr.select('td.tit')[0].text.strip()+tr.select('td.sale')[0].text.strip())

# tr.select('td.sale')[0].text) or tr.select_one('td.sale').text 둘 중 하나를 쓰면 숫자만 나타난다.



