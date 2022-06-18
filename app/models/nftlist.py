from app import db


class Nft(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(255))
    picture = db.Column(db.String(255))
    description = db.Column(db.String(255))
    chain_id = db.Column(db.String(255))
    nft_address = db.Column(db.String(255))
    user_address = db.Column(db.String(255))