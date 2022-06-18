import os
import tweepy
from app import db
from app.models.transaction import Transaction
from app.validation.address_validation import AddressValidation


class TwitterTokenShareService:
    API_KEY = os.getenv("API_KEY")
    API_SECRET = os.getenv("API_SECRET")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    ACCESS_SECRET = os.getenv("ACCESS_SECRET")

    def __init__(self):
        self.auth = tweepy.OAuthHandler(self.API_KEY, self.API_SECRET)
        self.auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_SECRET)
        self.api = tweepy.API(self.auth)

    def twitter_repost(self, address, twitter_username):
        validation = AddressValidation()
        if validation.address_validation(address) is True:
            amount = 0
            article = 1538081897137508352
            retweets_list = self.api.get_retweets(article)
            list1 = []
            try:
                twitter_user_id = self.api.get_user(screen_name=twitter_username)
                print("twitter_user_id", twitter_user_id.screen_name)
            except tweepy.errors.NotFound:
                return {
                           "code": 404,
                           "errors": [
                               {
                                   "message": f"User with this username: {twitter_username} not found",
                                   "code": 404
                               }
                           ]
                       }, 404
            subscribe = self.api.get_friendship(source_screen_name=twitter_username, target_screen_name='@TMQtoday')
            if not subscribe[0].following:
                print("FOLLOWING TWITTER", subscribe[0].following)
                return {
                           "code": 404,
                           "errors": [
                               {
                                   "message": f"User with this username: {twitter_username} not subscribe to the "
                                              f"@TMQtoday",
                                   "code": 404
                               }
                           ]
                       }, 404
            else:
                amount += 7
            for retweet in retweets_list:
                list1.append(retweet.user.screen_name)
            check_user = Transaction.query.filter_by(twitter_username=twitter_username, address=address).first()
            if str(twitter_user_id.screen_name) in list1 and check_user is None:
                amount += 7
                tx = Transaction()
                tx.address = address
                tx.twitter_username = twitter_username
                tx.amount = amount
                db.session.add(tx)
                db.session.commit()
                db.session.flush()
                return {
                           "code": 200,
                           "status": [
                               {
                                   "message": "Success",
                                   "code": 200
                               }
                           ]
                       }, 200
            else:
                return {
                           "code": 403,
                           "errors": [
                               {
                                   "message": f"User with this username: {twitter_username}  and address {address} already get free tokens ",
                                   "code": 403
                               }
                           ]
                       }, 403
