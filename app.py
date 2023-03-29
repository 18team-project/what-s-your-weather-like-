from flask import Flask, render_template, request, jsonify, session, redirect, url_for
app = Flask(__name__)
app.secret_key = 'user_nm'

# 크롤링
import requests
from bs4 import BeautifulSoup
import time

url = "https://www.google.com/search?q=%ED%98%84%EC%9E%AC+%EB%82%A0%EC%94%A8&sxsrf=APwXEder-3VCFE-cJgu0S-v_teumLWQmJQ%3A1680035186735&ei=ck0jZPjBLJuB2roPtqK7sAU&ved=0ahUKEwj4wo_kuv_9AhWbgFYBHTbRDlYQ4dUDCA8&uact=5&oq=%ED%98%84%EC%9E%AC+%EB%82%A0%EC%94%A8&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIMCCMQJxCdAhBGEIACMgcIABCKBRBDMgcIABCKBRBDMgoIABCABBAUEIcCMgUIABCABDIFCAAQgAQyBQgAEIAEMgQIABAeMgQIABAeMgQIABAeOgQIIxAnOgQIABADOgsIABCABBCxAxCDAToLCC4QgAQQsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOhEILhCDARDHARCxAxDRAxCABDoICAAQgAQQsQM6BQguEIAEOgoILhCKBRDUAhBDSgQIQRgAUABYoAtgtBBoAXABeAGAAYQCiAHMC5IBBjAuMTAuMZgBAKABAcABAQ&sclient=gws-wiz-serp"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
weather_type = soup.select_one('span#wob_dc').text

# DB
from pymongo import MongoClient
import certifi
ca = certifi.where()

client = MongoClient('mongodb+srv://root:root@wywl.xvagz18.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.wywl
users = db['th_user']

@app.route('/')
def home():    
    test = db.th_mood.aggregate([
        { "$lookup":{
            "from" : "tc_mood",
            "localField" : "mood_cd",
            "foreignField" : "mood_cd",
            "as" : "emoji"
            }
        },
        {"$unwind" : "$emoji"},      
    ])

    test2 = db.th_mood.aggregate([
        { "$project":{
        "user_nm":1,
        "comment":1,
        "date":1,
        "_id":0,
        "mood_cd":1
        }
        
        },
        { "$lookup":{
            "from" : "tc_mood",
            "let" : { "mood_cd" : "$mood_cd"},
            "pipeline":[
                {"$project":{
                "_id":0,
                
                "mood_nm":0,

                "mood_desc":0
                } 
                },
                {"$match": 
                    {"$expr": 
                        {"$and" : 
                            [
                                {"$eq":["$$mood_cd", "$mood_cd"]}
                            ]
                        }    
                    }
                }
            ],
            "as" : "emojiInfo"
            }
        },
        {"$unwind" : "$emojiInfo"},    

    ])
    print(list(test2))
    return render_template('home.html', weather_type = weather_type)

@app.route("/register")
def go_page_register():
    return render_template('register.html', weather_type = weather_type)

@app.route('/chk_nm', methods=["POST"])
def chk_nm():
    # 데이터받기
    user_nm_receive = request.form['user_nm']

    # 조회
    user = db.th_user.find_one({'user_nm':user_nm_receive})
    msg = ""
    chkr = False
    if user is None :
        msg = "사용 가능한 닉네임 입니다."
        chkr = True

    else :
        msg = "사용 불가능한 닉네임 입니다."
        chkr = False

    # 저장
    # user = {'name': name_receive, 'address': address_receive, 'size':size_receive}
    # db.mars.insert_one(doc)

    return jsonify({'msg':msg, 'chkr':chkr})


@app.route('/register', methods=["POST"])
def register_sign_up():
    # 데이터받기
    user_nm_receive = request.form['user_nm']
    user_pw_receive = request.form['user_pw']

    # 저장
    user = {'user_nm' :user_nm_receive,
            'user_pw':user_pw_receive }
    db.th_user.insert_one(user)
    return jsonify({'msg':'회원가입이 완료되었습니다.\n 당신의 날씨를 꾸준히 기록해주세요!'})

@app.route("/mood")
def go_page_mood():
    # 이동
    # user_nm_receive = request.form['user_nm']
    # login_yn_receive = request.form['login_yn']
    # print(user_nm_receive, login_yn_receive)
    return render_template('mood.html')

# @app.route('/mood', methods=['GET'])
# def gopagemood():
#     if 'user_nm' in session:
#         username = session['user_nm']
#         return render_template('mood.html', user_nm=username)

@app.route('/login')
def gologinpage():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.json['user_nm']
    password = request.json['user_pw']
    print(username)
    print(password)
    user = users.find_one({'user_nm': username})

    print(user)
    if user and user['user_pw'] == password:
        session['user_nm'] = username
        return jsonify({'status': 'success', 'message': '로그인 성공'})
    else:
        return jsonify({'status': 'failure', 'message': '일치하는 데이터가 없습니다.', 'username': username, 'password': password})

@app.route('/gogo', methods=['GET'])
def gogo():
    if 'user_nm' in session:
        username = session['user_nm']
        print(username)
        return render_template("mood.html")
    else:
        return redirect(url_for('gologinpage'))


if __name__ == '__main__':
    app.run('0.0.0.0', port=5002, debug=True)
