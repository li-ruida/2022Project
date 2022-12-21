import flask
from flask import Flask
from flask import request
from crawler import mysearch

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return flask.render_template("index.html")
@app.route('/search',methods = ['POST', 'GET'])
def search():  # put application's code here
    linkstr="q="
    if request.method == 'POST':
        stars = request.form.get('stars')
        owners = request.form.get('owners')
        language = request.form.get('language')
        license = request.form.get('license')
        date=request.form.get('date')
    if request.method == 'GET':
        owners = None
        language = None
        license = None
        date=None
        stars = str(10000)
    print(stars,owners,language,license,date)
    if owners != None and owners !='':
        linkstr+='user%3A'+owners+'+'
    if date!=None and date != '':
        linkstr+='created%3A%3E'+date+'+'
    if stars!=None and stars!='':
        linkstr+='stars%3A%3E'+stars+'+'
    if license!=None and license!='':
        linkstr+='license%3A'+license+'+'
    if linkstr[-1]=='+':
        linkstr=linkstr[0:-1]
    print(linkstr)
    tmp1= mysearch.searchAdvanced(linkstr)
    print(len(tmp1))
    print('####')
    for ii in tmp1:
        ii.__repr__()
    return linkstr
if __name__ == '__main__':

    app.run()

