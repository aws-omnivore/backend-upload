#S3에 파일 업로드

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from botocore.client import Config
import boto3
import os
from dotenv import load_dotenv
load_dotenv()

S3_BUCKET_NAME='uploadbk123'

s3=boto3.client(
    's3',
    aws_access_key_id = os.environ.get('aws_access_key_id'),
    aws_secret_access_key = os.environ.get('aws_secret_access_key')
)

#------------s3 연동끝---------


app = Flask(__name__)


@app.route('/')
def render_file():
    return render_template('upload.html')


@app.route('/upload', methods=['GET','POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        s3.upload_fileobj(file, S3_BUCKET_NAME, filename)
        return 'File upload successfully', 200
    else:
        return 'No file selected', 404
    
    

if __name__ == '__main__':
    app.run(debug = True)       
       