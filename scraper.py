from flask import Flask, render_template, request
from flask import json
app = Flask(__name__)

import requests

@app.route('/')
def main(): 
    return render_template('index.html')
#this gets all of the subject codes, eventually this will help us in accessing specific subjects i.e computer science 
@app.route('/sniped',methods=['POST','GET'])
def sniped():
    if request.method=='POST':
        subCode = request.form['subCode']
        courCode = request.form['courCode']
        secCode = request.form['secCode']
        url = "https://sis.rutgers.edu/soc/courses.json?subject={}&semester=92019&campus=NB&level=U,G".format(subCode)
        r = requests.get(url)
        data = r.json()
        for c in data:
            if c['courseNumber']==courCode:
                for d in c['sections']:
                    print(d['number'], d['openStatus'])
                    if d['number']==secCode and d['openStatus']==True:
                        return render_template('sniperload.html',opened = "true")

        return render_template('sniperload.html',opened = "false")
    else:
        return render_template('index.html')
