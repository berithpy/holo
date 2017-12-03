from flask import Flask, request, Response,render_template,redirect
from matrix import scrolling_text_flask
from werkzeug.contrib.fixers import ProxyFix
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
	return render_template('scrolling_text.html')

@app.route("/text/scrolling/", methods=['POST'])
def api():
	if hasattr(request,'form'):
		msg=request.form['texto']
		speed=(11-int(request.form.get('speed')))*0.01
		font=int(request.form.get('font'))
		print("speed {} font {}".format(speed,font))
		scrolling_text_flask(msg,speed,font)
		return redirect('/',code=302)

app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5123)
