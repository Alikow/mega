from program import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/100Days')
def p100Days():
    return render_template('100Days.html')
  
 
@app.route('/PJ_1')
def PJ_1():
    return render_template('PJ_1.html')