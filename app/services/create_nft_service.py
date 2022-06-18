from app import db
from app.models.nftlist import Nft


class CreateNftService:

    def create_nft(self, name, picture, description, chain_id, address, user_address):
        nft_exists = Nft.query.filter_by(nft_address=address).first()
        if nft_exists is not None:
            return {"Error nft already exists"}
        nft = Nft()
        nft.name = name
        nft.picture = picture
        nft.description = description
        nft.chain_id = chain_id
        nft.nft_address = address
        nft.user_address = user_address
        db.session.add(nft)
        db.session.commit()
        return "Success"

    def edit_nft(self, address, chain_id):
        nft_view = Nft.query.filter_by(nft_address=address).first()
        nft_view.chain_id = chain_id
        db.session.commit()
        return "Success"