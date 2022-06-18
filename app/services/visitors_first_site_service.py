from app import db
from app.models.transaction import Transaction
from app.validation.address_validation import AddressValidation


class VisitorsFirstSiteService:

    def first_visit(self, address, ip_address):
        tx = Transaction.query.filter_by(address=address, ip_address=ip_address).first()
        if tx is None:
            transaction = Transaction()
            transaction.ip_address = ip_address
            transaction.address = address
            transaction.amount = 11
            db.session.add(transaction)
            db.session.commit()
            db.session.flush()
            return "Success"
        else:
            return "Address with this IP already exists."
