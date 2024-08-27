from flask import Flask, request
from routes import register_routes




app = Flask(__name__ )
register_routes(app)

@app.route('/')
def index():
    #화면에 JSON형태로 띄어줌.
    return{"Hello ": "Flask"}

@app.route('/api/v1/feeds', methods=['GET']) #Rest API : [GET] /api/v1/feeds
def show_all_feeds():
    data = {'result':'success', 'data':{'feed1':'data1', 'feed2':'data2'}}

    return data #jsonigy


@app.route('/api/v1/feeds/<int:feed_id>',methods =['GET'])
def show_one_feed(feed_id):
    data = {'result': 'success' , 'data':f'feed ID:{feed_id}'} #f-string 적용
    return data

#게시글 만들기- feed_id =auto_increment라서 따로 지정 안해줌.
@app.route('/api/v1/feeds', methods=['POST'])
def create_feed():
    email = request.form['email']
    content = request.form['content']

    data = {'result':'success', 'data' :{'email':email, 'content' : content}}
    return data


if __name__ == "__main__":
    app.run()

    #마이크로서비스 아키텍처 -> 왜 이렇게 할까? -> 하나 터져도 다른 기능은 문제가 없다.
    #배달의 민족
    # -결제 기능 => 기능 하나당 서버 하나