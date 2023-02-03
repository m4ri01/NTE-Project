from Models.DB import db,ODP,Internet
from flask import request, jsonify
from Utils.Distance import Distance
from Utils.Serializer import Obj2Json
def store():
    data = request.get_json()
    Name = data['name']
    NDInternet = data['NDInternet']
    SNONT = data['SNONT']
    alamat = data["alamat"]
    longitude = data["longitude"]
    latitude = data["latitude"]
    ODPData = data["ODP"]

    ODPCheck = db.session.query(ODP).filter_by(ODPName=ODPData).first() 
    if ODPCheck is None:
         return jsonify({'error': 'ODP not found'}), 404
    distance = Distance.haversine(ODPCheck.latitude, ODPCheck.longitude, latitude, longitude)
    if distance >= 250:
        return jsonify({'error': 'ONT is not in range'}), 400
    if db.session.query(Internet).filter_by(NDInternet=NDInternet).first() is None:
        db.session.add(Internet(Name=Name, NDInternet=NDInternet, SNONT=SNONT, alamat=alamat, longitude=longitude, latitude=latitude, ODPId=ODPCheck.id, firstONT=SNONT))
    else:
        data = db.session.query(Internet).filter_by(NDInternet=NDInternet).first()
        data.Name = Name
        data.NDInternet = NDInternet
        data.SNONT = SNONT
        data.alamat = alamat
        data.longitude = longitude
        data.latitude = latitude
        data.ODPId = ODPCheck.id
        data.lastONT = SNONT
    db.session.commit()
    return jsonify({'success': 'ONT stored'}), 200

def read():
    data = request.args
    name = data["name"]
    dataType = data["dataType"]
    if name is None or dataType is None:
        return jsonify({'error': 'name and dataType are required'}), 400
    if dataType == 'SNONT':
        data = db.session.query(ODP, Internet).filter(ODP.id == Internet.ODPId).filter(Internet.SNONT == name).first()
    else:
        data = db.session.query(ODP, Internet).filter(ODP.id == Internet.ODPId).filter(Internet.NDInternet == name).first()
    if data is None:
        return jsonify({'error': 'data not found'}), 404
    return jsonify(Obj2Json(data)), 200


