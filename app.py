from flask import Flask

UPLOAD_FOLDER = '/home/harsh/micro/Python-Flask-Docker/Wav2Lip/sample_data/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024