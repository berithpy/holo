from flask import Flask, request, Response, render_template, redirect, url_for
from flask_cors import CORS
from matrix import test_scrolling_text_flask, scrolling_text_flask
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('scrolling_text.html')


@app.route('/text/scrolling/', methods=['POST'])
def text_scrolling():
    if hasattr(request, 'form'):
        msg = request.form['text']
        speed = (11 - int(request.form['speed'])) * 0.01
        font = int(request.form['font'])
        print('speed {} font {}'.format(speed, font))
        scrolling_text_flask(msg, speed, font)
        return redirect(url_for('index'), code=302)


@app.route('/test/text/scrolling/', methods=['POST'])
def test_text_scrolling():
    if hasattr(request, 'form'):
        msg = request.form['text']
        speed = int(request.form['speed'])
        font = int(request.form['font'])

        test_scrolling_text_flask(msg, speed, font)

        return Response(msg)


app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5123)
