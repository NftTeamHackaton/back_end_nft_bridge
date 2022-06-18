from app import db


class Transaction(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    address = db.Column(db.String(255))
    twitter_username = db.Column(db.String(255), nullable=True)
    tiktok = db.Column(db.String(255), nullable=True)
    amount = db.Column(db.Integer)
    ip_address = db.Column(db.String(255))
    send_status = db.Column(db.BOOLEAN, default=False)
