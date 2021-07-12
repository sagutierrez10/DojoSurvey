from flask import Flask, redirect, url_for, render_template, request, session
app = Flask(__name__)
app.secret_key = 'survey'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process')
def process():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name= request.form['nm']
    location= request.form['place']
    language= request.form['lan']
    comment= request.form['comment']

    session['name']=name
    session['location']=location
    session['language']=language
    session['comment']=comment
    
    return render_template ("result.html", name=name, location=location, language = language, comment = comment)

if __name__ == '__main__':
    app.run(debug=True)