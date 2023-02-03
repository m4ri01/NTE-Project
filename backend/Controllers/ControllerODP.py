from Models.DB import db
from flask import request, jsonify
import pandas as pd
from werkzeug.utils import secure_filename
import os
ALLOWED_EXTENSIONS = set(['xlsx'])

def allowedFile(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def processData(path):
    df = pd.read_excel(path) 
    df = df[df['LATITUDE'].notna()]
    df = df[df['LONGITUDE'].notna()]
    df = df[df['LOC_ID'].notna()]
    df = df[["LOC_ID","LATITUDE","LONGITUDE"]]
    df = df.rename({"LOC_ID":"ODPName","LATITUDE":"latitude","LONGITUDE":"longitude"},axis=1)
    df.to_sql('odp', db.engine, if_exists='append', index=False)

def storeDataFrame():
    if 'file' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message' : 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and allowedFile(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join("./Uploads/data.xlsx"))
        try:
            processData("./Uploads/data.xlsx")
        except Exception as e:
            print(e)
            resp = jsonify({'message' : 'File is not valid'})
            resp.status_code = 400
            return resp
        resp = jsonify({'message' : 'File successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify({'message' : 'Allowed file xlsx'})
        resp.status_code = 400
        return resp
