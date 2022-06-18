from flask import jsonify

from app.models.nftlist import Nft


class UserNftService:

    def user_nfts(self, address):
        nfts = Nft.query.filter_by(user_address=address).all()
        data = []
        for nft in nfts:
            data.append({
                "name": nft.name,
                "picture": nft.picture,
                "description": nft.description,
                "chain_id": nft.chain_id,
                "nft_id": nft.nft_id,
                "nft_address": nft.nft_address,
                "user_address": nft.user_address,
            })
        return jsonify(data)
