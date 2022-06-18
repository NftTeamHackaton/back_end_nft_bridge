import os

from web3 import Web3


class AddressValidation:
    RINKEBY_URL = os.getenv("RINKEBY_URL")
    w3 = Web3(Web3.HTTPProvider(RINKEBY_URL))

    def address_validation(self, address):
        checksum_address = self.w3.isChecksumAddress(address)
        if checksum_address is True:
            print("Address is valid")
            return True
        else:
            return {
                       "code": 404,
                       "errors": [
                           {
                               "message": "User address is not valid",
                               "code": 404
                           }
                       ]
                   }, 404
