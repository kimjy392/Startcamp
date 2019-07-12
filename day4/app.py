# 0. flask 패키지 가져오기
import random
from flask import Flask, render_template, request

# 1. app 설정
app = Flask(__name__)

# 2. 요청 경로(route) + 함수 만들기
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<string:name>')
def hello(name):
    return render_template('hello.html', name=name)

@app.route('/lunch')
def lunch():
    menus = ['레드코코넛누들', '소불고기', '삼계탕', '싸이버거', '치킨']
    pick = random.choice(menus)
    return render_template('lunch.html', menus=menus, pick=pick)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    # 사용자가 보낸 데이터를 받아와서
    text = request.args.get('say')
    print(request.args)
    img = "bonobono.png"
    # 템플릿에 넘겨준다.
    return render_template('pong.html', text=text, img=img)

@app.route('/random')
def random_game():
    return render_template('random.html')

@app.route('/result')
def result():
    mood = request.args.get('mood')
    weather = request.args.get('weather')
    playlist = {
        '외로움': ["https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/208094858&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"]
    }
    music = random.choice(playlist.get(mood, []))
    return render_template('result.html', mood=mood, weather=weather, music=music)   

@app.route('/lotto')
def lotto():
    return render_template('lotto.html')

@app.route('/recommend')
def recommend():
    name = request.args.get('name')
    num = request.args.get('num')
    random.seed(num)
    numbers = random.sample(range(1, 46), 6)
    return render_template('recommend.html', name=name, numbers=numbers)

if __name__ == '__main__':
    app.run(debug=True)