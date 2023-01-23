from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ODP(db.Model):
    __tablename__ = 'odp'
    id = db.Column(db.Integer, primary_key=True)
    ODPName = db.Column(db.String(100),nullable=False)
    longitude = db.Column(db.Numeric(precision=10, scale=7),nullable=False)
    latitude = db.Column(db.Numeric(precision=10, scale=7),nullable=False)
    ONTs = db.relationship("Internet", backref='odp')

    def serialize(self):
        return {
            'id': self.id,
            'ODPName': self.ODPName,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'ONTs': [ont.serialize() for ont in self.ONTs]
        }

class Internet(db.Model):
    __tablename__ = 'internet'
    id = db.Column(db.Integer, primary_key=True)
    NDInternet = db.Column(db.String(100),nullable=False)
    SNONT = db.Column(db.String(100),nullable=False)
    alamat = db.Column(db.String(100),nullable=False)
    longitude = db.Column(db.Numeric(precision=10, scale=7),nullable=False)
    latitude = db.Column(db.Numeric(precision=10, scale=7),nullable=False)
    ODPId  = db.Column(db.Integer, db.ForeignKey('odp.id'))
    firstONT = db.Column(db.String(100))
    lastONT = db.Column(db.String(100))
    
    def serialize(self):
        return {
            'id': self.id,
            'NDInternet': self.NDInternet,
            'SNONT': self.SNONT,
            'alamat': self.alamat,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'ODPId': self.ODPId,
            'firstONT': self.firstONT,
            'lastONT': self.lastONT
        }