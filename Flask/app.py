import json

from flask import Flask, request
app = Flask(__name__)
list=[]
@app.route('/')
def index_page():
    return "<h1> Concatenate strings</h1><br>" \
           "To input : Change url to http://127.0.0.1:5000/input/'Enter Your String Here'<br><br>" \
           "For output : Change url to http://127.0.0.1:5000/output"

@app.route('/input/<string:str>',methods = ['GET','POST'])
def take_input(str):
    list.append(str)
    return str + "is added successfully"

@app.route('/output',methods = ['GET','POST'])
def give_output():
    out=""
    for li in list:
        li=li+" "
        out=out+li
    return out + "is your concatenated string"

if __name__ == '__main__':
    app.run()