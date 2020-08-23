from flask import Flask
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
   return "Hello World"

@app.route('/qrcode')
def qrcode():
   return "Another page"


if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0',port=5001)
