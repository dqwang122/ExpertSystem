#-*-coding:UTF-8-*-
from __future__ import print_function
from flask import Flask, render_template, session, request, redirect, flash, g

import sys
sys.path.append("engine")
import Interaction

app=Flask(__name__)
app.secret_key ='123456'

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/', methods=['POST'])
def home_data():
    action = request.form['submit']

    if action == "infer":
        info = {}
        info['weather'] = request.form.get("weather")
        info['temperature'] = request.form.get("temperature")
        info['humidity'] = request.form.get("temperature")
        info['wind'] = request.form.get("wind")
        info['gender'] = request.form.get("gender")
        info['cold'] = request.form.get("cold")
        info['style'] = request.form.get("style")

        ret = Interaction.GetRet(info)

        return render_template('index.html', Suggestion=ret[0], Rules=ret[1], Description=ret[2])
    elif action == "all_check":
        
        return render_template('index.html')
    elif action == "add":
        return render_template('index.html')
    elif action == "delete":
        return render_template('index.html')
    elif action == "modify":
        return render_template('index.html')
    else:
        return render_template('index.html')



    
if __name__ == '__main__':
    app.run(debug=True)