from flask import Flask, request, Response
app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def basic_api():
    return Response(response={}, status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5123)
