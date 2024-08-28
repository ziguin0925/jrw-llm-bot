from flask import Flask, render_template, request
from dotenv import load_dotenv

import os

from openai import OpenAI
load_dotenv()

app = Flask(__name__)

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

messages = [] #메세지들이 담기는 공간 => 챗봇 (채팅 내역 6개월동안 보관) / 유럽 진출(유로6)

#웹 서버 - Nginx (리버스 프록시)
# (1) 로드 밸런서 => 트래픽 분산
# (2) 보안 => 다이렉트로 서버에 접근하면 보안이 취약.
# 불법 토토 => VM-안에 VM안에 VM(IP우회)

# (포워드 프록시)- 속도를 위한 것
# - 우리 회사가 이번에 미국에 런칭했어.
# - (유저) 느려 => 한국서버를 안거치고 미국 웹서버(포워트 프록시 - 정적 파일)

def make_prompt(user_input):
    res = client.chat.completions.create(
        model = 'gpt-4o-mini',
        messages=[
            {"role":"user", "content": user_input},
            {"role":"system", "content":"안녕하세요. 환불 절차를 도와드리겠습니다. 고객님의 성함과 연락처를 입력해주세요."}
        ]
    )

    return res.choices[0].message.content


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method=='POST':

        user_input = request.form['user_input']
        bot_response = make_prompt(user_input)

        messages.append({"role":"user" , "text":user_input})
        messages.append({"role":"bot" , "text":bot_response})

    return render_template('index.html', messages=messages)


if __name__ == "__main__":
    app.run(debug=True)
