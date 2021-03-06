from flask import Flask, request, jsonify,render_template
import os
from flask_cors import CORS, cross_origin
from wsgiref import simple_server
import speechToText
from com_in_ineuron_ai_utils.utils import decodeSound

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index2.html')


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['sound']
    decodeSound(image, "audio123.wav")
    result = speechToText.speech2Text("audio123.wav")
    return jsonify({"Result" : str(result)})

if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    host = '0.0.0.0'
    httpd = simple_server.make_server(host=host,port=port, app=app)
    httpd.serve_forever()
