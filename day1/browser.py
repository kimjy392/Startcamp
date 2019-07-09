import webbrowser

idols = ['bts', 'iu', 'obama']

for name in idols:
    webbrowser.open(f'https://search.naver.com/search.naver?query={name}')
    # string interpolation
    # 문자열 보간법 : f-string / ver 3.6 ++