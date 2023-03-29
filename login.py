# from flask import Flask, render_template, request, jsonify
# from pymongo import MongoClient


# # app = Flask(__name__)


# # app = Flask(__name__)

# client = MongoClient('mongodb+srv://root:root@wywl.xvagz18.mongodb.net/?retryWrites=true&w=majority')
# db = client['wywl']
# users = db['th_user']

# @app.route('/login')
# def home():
#     return render_template('login.html')

# @app.route('/login', methods=['POST'])
# def login():
#     username = request.json['user_nm']
#     password = request.json['user_pw']
#     print(username)
#     print(password)
#     user = users.find_one({'user_nm': username})


#     print(user)
#     if user and user['user_pw']==password:
#         return jsonify({'status': 'success', 'message': '로그인 성공'})
#     else:
#         return jsonify({'status': 'failure', 'message': '일치하는 데이터가 없습니다.', 'username':username , 'password':password})

# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)
