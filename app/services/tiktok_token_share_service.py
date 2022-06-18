from app import app, db
import requests
from app.validation.address_validation import AddressValidation
from app.models.transaction import Transaction


class TiktokTokenShareService:

    def tiktok(self, address, video_url):
        try:
            validation = AddressValidation()
            validation.address_validation(address)

            url = "https://social-media-data-tt.p.rapidapi.com/live/post/meta"

            querystring = {
                "video": str(video_url)
            }

            headers = {
                "X-RapidAPI-Key": "8ab0694abamsh382af471e889bc1p1b8246jsn08b98ca05f70",
                "X-RapidAPI-Host": "social-media-data-tt.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring).json()
            return self.response(response, address, video_url)
        except Exception as e:
            print(f"error {e}")
            return {
                       "code": 403,
                       "status": [
                           {
                               "message": "Error",
                               "code": 403
                           }
                       ]
                   }, 403

    def response(self, response, address, video_url):
        response_hashtags = response['hashtags']
        validate_tx = Transaction.query.filter_by(address=address, tiktok=video_url).first()
        if validate_tx is None:
            for i in response_hashtags:
                print(i)
                tags = i.get('name')
                if tags == 'tmqtoday':
                    tx = Transaction()
                    tx.tiktok = video_url
                    tx.address = address
                    tx.amount = 6
                    db.session.add(tx)
                    db.session.commit()
                    return {
                               "code": 200,
                               "status": [
                                   {
                                       "message": "Success",
                                       "code": 200
                                   }
                               ]
                           }, 200
            return {
                       "code": 403,
                       "status": [
                           {
                               "message": "No valide hashtag",
                               "code": 403
                           }
                       ]
                   }, 200
        else:
            return {
                       "code": 403,
                       "status": [
                           {
                               "message": "User with address and this tiktok already exists",
                               "code": 403
                           }
                       ]
                   }, 200
