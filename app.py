from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# DB
from pymongo import MongoClient
import certifi
ca = certifi.where()

client = MongoClient('mongodb+srv://root:root@wywl.xvagz18.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.wywl

@app.route('/')
def home():
    collection_list = db.list_collection_names()
    print(collection_list)

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
    print("-----------")
    print(list(test2))
    return render_template('mood.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5002, debug=True)