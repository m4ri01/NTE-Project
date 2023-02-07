def Obj2Json(obj):
    return {
        'id': obj.Internet.id,
        'name': obj.Internet.Name,
        'NDInternet': obj.Internet.NDInternet,
        'SNONT': obj.Internet.SNONT,
        'alamat': obj.Internet.alamat,
        'longitude': obj.Internet.longitude,
        'latitude': obj.Internet.latitude,
        'ODP': obj.ODP.ODPName,
        'firstONT': obj.Internet.firstONT,
        'lastONT': obj.Internet.lastONT,
        'statusONT': obj.Internet.statusONT,
    }