from flask import Flask, render_template, request
from kmp import *

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def idex():
    if request.method == 'POST':
        data = []
        data.append(request.form['stroka'])
        data.append(request.form['podstroka'])
        value = kmpSearchByCompil(data[0], data[1])
        if data:
            return render_template('rezult.html', value=value)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)